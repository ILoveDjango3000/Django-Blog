import os
import sys
import uuid
from io import BytesIO

from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("uploads/images", filename)


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    content = RichTextField()
    is_draft = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20]


@receiver(pre_save, sender=Article)
@transaction.atomic
def compress_uploaded_image(sender, instance, **kwargs):
    print(instance)
    try:
        article = sender.objects.select_for_update().get(pk=instance.pk)
    except sender.DoesNotExist:
        # Its a new object
        instance.image = compress_image(instance.image)
    else:
        if article.image != instance.image:
            instance.image = compress_image(instance.image)


def compress_image(uploaded_image):
    image = Image.open(uploaded_image)
    temp_image = image.convert("RGB")
    temp_image = temp_image.resize((900, 570))
    output_io_stream = BytesIO()
    temp_image.save(output_io_stream, format="JPEG", quality=60)
    output_io_stream.seek(0)
    compressed = InMemoryUploadedFile(
        output_io_stream,
        "ImageField",
        "%s.jpg" % uploaded_image.name.split(".")[0],
        "image/jpeg",
        sys.getsizeof(output_io_stream),
        None,
    )
    return compressed

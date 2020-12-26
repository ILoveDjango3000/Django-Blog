import os
import uuid

from ckeditor.fields import RichTextField
from django.db import models


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

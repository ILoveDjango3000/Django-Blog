from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()
	content = RichTextField()
	is_draft = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title[:20]
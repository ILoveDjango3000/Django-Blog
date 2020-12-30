from ckeditor.widgets import CKEditorWidget
from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name="custom"))

    class Meta:
        model = Article
        fields = ["title", "slug", "image", "content"]

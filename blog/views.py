from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView

from .forms import ArticleForm
from .models import Article


class HomePageView(ListView):
    model = Article
    queryset = Article.objects.filter(is_draft=False)
    template_name = "blog/article_list.html"


class ArticleCreate(CreateView):
    form_class = ArticleForm
    success_url = reverse_lazy("index")
    template_name = "blog/article_create.html"

from django.urls import path

from .views import HomePageView, ArticleCreate

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("create/", ArticleCreate.as_view(), name="create-article"),
]

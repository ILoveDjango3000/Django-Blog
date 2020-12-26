from django.urls import path

from .views import ArticleCreate
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("create/", ArticleCreate.as_view(), name="create-article"),
]

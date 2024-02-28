from django.urls import path, include
from news.views import (
    home,
    news_details,
    categories_form,
    news_form,
    CategoryViewSet,
    UserViewSet,
    NewsViewSet,
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"users", UserViewSet)
router.register(r"news", NewsViewSet)

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("news", news_form, name="news-form"),
    path("categories", categories_form, name="categories-form"),
    path("api/", include(router.urls)),
]

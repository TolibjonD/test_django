from django.urls import path
from .views import home, detail_page, create_news, change_news

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug:slug>/", detail_page, name="detail"),
    path("create/", create_news, name="create"),
    path("edit/<int:id>/", change_news, name="edit")
]

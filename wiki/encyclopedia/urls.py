from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name = "search"),
    path("create", views.create_new_page, name = "create"),
    path("edit/<str:entry>", views.edit_page, name = "edit"),
    path("random", views.random_page, name = "random")
]

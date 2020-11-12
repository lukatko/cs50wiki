from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("wiki/search/found", views.search, name = "search"),
    path("create", views.create_new_page, name = "create")
]

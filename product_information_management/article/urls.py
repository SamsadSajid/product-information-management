from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_article, name="create_article"),
    path('edit', views.edit_article, name="edit_article"),
    path('delete', views.delete_article, name="delete_article"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_category, name="create_category"),
    path('delete', views.delete_category, name="create_delete"),
    path('edit', views.edit_category, name="edit_category"),
    path('get-all-categories', views.get_all_categories, name="all_categories"),
]

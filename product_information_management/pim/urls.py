from django.urls import path
from . import views

urlpatterns = [
    path('category/create', views.create_category, name="create_category"),
]

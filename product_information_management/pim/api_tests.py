import pytest
from rest_framework.test import APIRequestFactory

from pim.models import Category
from pim.views import create_category, edit_category


@pytest.fixture
def create_dummy_category():
    return Category.objects.create(name="a category")


@pytest.fixture
def create_dummy_parent_category():
    return Category.objects.create(name="a parent")


@pytest.mark.django_db
def test_create_category_should_return_status_code_200():
    factory = APIRequestFactory()
    request = factory.post('api/category/create', {'name': 'a category'}, format='json')
    response = create_category(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_category_should_return_status_code_400():
    factory = APIRequestFactory()
    request = factory.post('api/category/create', {'parent': 'a category'}, format='json')
    response = create_category(request)

    assert response.status_code == 400


@pytest.mark.django_db
def test_edit_category_should_return_status_code_200(create_dummy_category):
    _ = create_dummy_category

    factory = APIRequestFactory()
    request = factory.post('api/category/edit', {'name': 'a category', 'parent': 'a parent'}, format='json')
    response = edit_category(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_category_should_create_a_new_parent_category(create_dummy_category):
    _ = create_dummy_category

    factory = APIRequestFactory()
    request = factory.post('api/category/edit', {'name': 'a category', 'parent': 'a new parent'}, format='json')
    _ = edit_category(request)

    newly_created_parent_category = Category.objects.filter(name='a new parent').first()
    assert newly_created_parent_category is not None


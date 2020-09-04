import pytest
from rest_framework.test import APIRequestFactory

from article.models import Article
from article.views import create_article, delete_article, edit_article, get_all_articles
from pim.models import Category


@pytest.fixture
def create_dummy_category():
    return Category.objects.create(name="a category")


@pytest.fixture
def create_dummy_article():
    return Article.objects.create(name="an article")


@pytest.mark.django_db
def test_create_article_should_return_status_code_200():
    factory = APIRequestFactory()
    request = factory.post('api/article/create', {'name': 'an article', 'category_name': 'Led Zepplin'}, format='json')
    response = create_article(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_article_should_return_status_code_400():
    factory = APIRequestFactory()
    request = factory.post('api/article/create', {'category_name': 'Led Zepplin'}, format='json')
    response = create_article(request)

    assert response.status_code == 400


@pytest.mark.django_db
def test_update_article_should_return_status_code_200(create_dummy_article):
    article = create_dummy_article

    factory = APIRequestFactory()
    request = factory.post('api/article/create', {'name': article.name, 'category_name': 'Led Zepplin'}, format='json')
    response = edit_article(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_article_should_return_status_code_400(create_dummy_article):
    article = create_dummy_article

    factory = APIRequestFactory()
    request = factory.post('api/article/create', {'name': "article.name", 'category_name': 'Led Zepplin'}, format='json')
    response = edit_article(request)

    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_article_should_return_status_code_200(create_dummy_article):
    article = create_dummy_article

    factory = APIRequestFactory()
    request = factory.post('api/article/delete', {'name': article.name}, format='json')
    response = delete_article(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_article_should_return_status_code_400(create_dummy_article):
    article = create_dummy_article

    factory = APIRequestFactory()
    request = factory.post('api/article/delete', {'name': article.name}, format='json')
    delete_article(request)
    response = delete_article(request)

    assert response.status_code == 400


@pytest.mark.django_db
def get_all_articles_should_return_data_length():
    category = Category.objects.create(name='a category')

    article1 = Article.objects.create(name='article 1', price=100.00, stock_quantity=10)
    article1.category.add(category)

    article2 = Article.objects.create(name='article 2', price=200.00, stock_quantity=20)
    article2.category.add(category)

    article3 = Article.objects.create(name='article 3', price=300.00, stock_quantity=30)
    article3.category.add(category)

    factory = APIRequestFactory()
    request = factory.post('api/article/get-all-articles?page=1', {'name': 'a category'}, format='json')
    response = get_all_articles(request)

    assert len(response.data) == 2

    request = factory.post('api/article/get-all-articles?page=2', {'name': 'a category'}, format='json')
    response = get_all_articles(request)

    assert len(response.data) == 1

import uuid

import pytest

from pim.models import Category
from .models import Article
from .views import create_article


"""
The following is an integration test that make connection to
the database and tries to create an entry for an Article
"""


@pytest.mark.django_db
def test_create_article_should_create_an_article_without_category():
    Article.objects.create(
        sku=uuid.uuid4(),
        ean=uuid.uuid4(),
        name="an article"
    )

    assert Article.objects.count() == 1

    article = Article.objects.get(name="an article")
    assert article.category.exists() is False


@pytest.mark.django_db
def test_create_article_should_create_an_article_with_category():
    category = Category.objects.create(name="a_category")

    article = Article.objects.create(
        sku=uuid.uuid4(),
        ean=uuid.uuid4(),
        name="an article"
    )

    article.category.add(category)

    assert Article.objects.count() == 1

    article = Article.objects.get(name="an article")
    assert article.category.get(name="a_category") == category

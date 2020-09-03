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
    assert Article.objects.get(name="an article").category is None


@pytest.mark.django_db
def test_create_article_should_create_an_article_with_category():
    category = Category.objects.create(name="a_category")

    Article.objects.create(
        sku=uuid.uuid4(),
        ean=uuid.uuid4(),
        name="an article",
        category=category
    )

    assert Article.objects.count() == 1
    assert Article.objects.get(name="an article").category == category


# def test_details(rf):
#     request = rf.get('api/article/create')
#     response = create_article(request)
#
#     assert response.status_code == 200
#
# @pytest.fixture
# def smtp_connection():
#     import smtplib
#
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#
#
# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 250

import json

from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response

from article.models import Article
from pim.models import Category


def convert_request_body_to_json(request):
    unicode_body = request.body.decode('utf-8')

    body = json.loads(unicode_body)

    print(body)

    return body


def generate_invalid_req_body_error_message_response():
    data = {
        "message": "Invalid request body"
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def map_create_category(req_body):
    category_name, parent = req_body.get('name', None), req_body.get('parent', None)

    return category_name, parent


def generate_bad_req_body_error_message_response():
    data = {
        "message": "This category already exists"
    }
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def object_exists_with_this_category(category_name):
    return Category.objects.filter(name=category_name).exists()


def map_create_article(req_body):
    sku = req_body.get('sku', None)
    ean = req_body.get('ean', None)
    name = req_body.get('name', None)
    stock_quantity = req_body.get('stock_quantity', None)
    price = req_body.get('price', None)
    category_name = req_body.get('category_name', None)

    return sku, ean, name, stock_quantity, price, category_name


def object_exists_with_this_article(sku, ean, name):
    return Article.objects.filter(sku=sku, ean=ean, name=name).exists()


def get_category_for_article_or_none(category_name):
    try:
        return Category.objects.get(name=category_name, isDeleted=0)
    except Category.DoesNotExist:
        return None

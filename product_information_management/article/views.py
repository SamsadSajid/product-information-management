from rest_framework.decorators import api_view
from rest_framework.response import Response

from article.models import Article
from utility.enums import EntityType
from utility.request_validation import is_invalid_create_article_request_body
from utility.utility import (convert_request_body_to_json, generate_invalid_req_body_error_message_response,
                             map_create_article, object_exists_with_this_article,
                             generate_bad_req_body_error_message_response, get_category_for_article_or_none)


@api_view(['POST'])
def create_article(request):
    body = convert_request_body_to_json(request)

    if is_invalid_create_article_request_body(body):
        return generate_invalid_req_body_error_message_response()

    name, stock_quantity, price, category_name = map_create_article(body)

    if object_exists_with_this_article(name):
        return generate_bad_req_body_error_message_response(EntityType.ARTICLE.value)

    category = get_category_for_article_or_none(category_name)

    article = Article.objects.create(name=name, stock_quantity=stock_quantity, price=price,
                                     category=category)

    article.save()

    data = {
        "message": "Category saved successfully"
    }

    return Response(data=data)


@api_view(['POST'])
def edit_article(request):
    body = convert_request_body_to_json(request)

    if is_invalid_create_article_request_body(body):
        return generate_invalid_req_body_error_message_response()

    name, stock_quantity, price, category_name = map_create_article(body)

    article = Article.objects.filter(name=name)
    if not article.exists():
        return generate_bad_req_body_error_message_response(EntityType.ARTICLE.value)

    category = get_category_for_article_or_none(category_name)

    article.update(category=category)

    data = {
        "message": "Category updated successfully"
    }

    return Response(data=data)

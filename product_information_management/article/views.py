from rest_framework.decorators import api_view
from rest_framework.response import Response

from article.models import Article
from utility.enums import EntityType
from utility.request_validation import is_invalid_create_article_request_body
from utility.utility import (convert_request_body_to_json, generate_invalid_req_body_error_message_response,
                             map_create_article, object_exists_with_this_article,
                             generate_bad_req_body_error_message_response, get_category_for_article_or_none,
                             generate_success_deletion_message, generate_success_message, get_category_list_or_none)


@api_view(['POST'])
def create_article(request):
    body = convert_request_body_to_json(request)

    if is_invalid_create_article_request_body(body):
        return generate_invalid_req_body_error_message_response()

    name, stock_quantity, price, category_name = map_create_article(body)

    if object_exists_with_this_article(name):
        return generate_bad_req_body_error_message_response(EntityType.ARTICLE.value)

    article = Article.objects.create(name=name, stock_quantity=stock_quantity, price=price)

    article.save()

    category_list = get_category_list_or_none(category_name)

    # TODO: Optimize the following operation to minimize the db call
    if category_list:
        for category in category_list:
            article.category.add(category)

    return generate_success_message(EntityType.ARTICLE.value)


@api_view(['POST'])
def edit_article(request):
    body = convert_request_body_to_json(request)

    if is_invalid_create_article_request_body(body):
        return generate_invalid_req_body_error_message_response()

    name, stock_quantity, price, category_name = map_create_article(body)

    article = Article.objects.filter(name=name)
    if not article.exists():
        return generate_bad_req_body_error_message_response(EntityType.ARTICLE.value)

    if price != 0:
        article.update(price=price)

    if stock_quantity != 0:
        article.update(stock_quantity=stock_quantity)

    article = Article.objects.get(name=name, isDeleted=0)

    category_list = get_category_list_or_none(category_name)

    if category_list:
        for category in category_list:
            article.category.add(category)

    data = {
        "message": "Article updated successfully"
    }

    return Response(data=data)


@api_view(['POST'])
def delete_article(request):
    body = convert_request_body_to_json(request)

    name, stock_quantity, price, category_name = map_create_article(body)

    article = Article.objects.filter(name=name, isDeleted=0)
    if article.exists():
        article.update(isDeleted=1)

        return generate_success_deletion_message(EntityType.ARTICLE.value)

    return generate_invalid_req_body_error_message_response()


@api_view(['GET'])
def get_all_articles(request):
    return Article.objects.all().order_by('-price')

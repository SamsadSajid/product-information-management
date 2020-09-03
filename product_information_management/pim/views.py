from rest_framework.decorators import api_view
from rest_framework.response import Response

from utility.enums import EntityType
from utility.request_validation import is_invalid_create_category_request_body
from utility.utility import (
    convert_request_body_to_json, generate_invalid_req_body_error_message_response,
    map_create_category, generate_bad_req_body_error_message_response, object_exists_with_this_category
)
from .models import Category


@api_view(['POST'])
def create_category(request):
    body = convert_request_body_to_json(request)

    if is_invalid_create_category_request_body(body):
        return generate_invalid_req_body_error_message_response()

    category_name, parent = map_create_category(body)

    if object_exists_with_this_category(category_name):
        return generate_bad_req_body_error_message_response(EntityType.CATEGORY.value)

    if parent:
        parent_of_the_category = Category.objects.get(name=parent)
        category = Category.objects.create(name=category_name, parent=parent_of_the_category)
        category.save()

    else:
        category = Category.objects.create(name=category_name)
        category.save()

    data = {
        "message": "Category saved successfully"
    }
    return Response(data=data)


@api_view(['POST'])
def delete_category(request):
    body = convert_request_body_to_json(request)
    category_name, _ = map_create_category(body)

    category = Category.objects.filter(name=category_name, isDeleted=0)
    if category.exists():
        category.update(isDeleted=1)

        data = {
            "message": "Category deleted successfully"
        }
        return Response(data=data)

    return generate_invalid_req_body_error_message_response()

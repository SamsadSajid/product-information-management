import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utility.request_validation import is_valid_create_category_request_body
from utility.utility import (
    convert_request_body_to_json,
    generate_invalid_req_body_error_message_response,
    map_create_category, generate_bad_req_body_error_message_response
)
from .models import Category


@api_view(['POST'])
def create_category(request):
    body = convert_request_body_to_json(request)

    if is_valid_create_category_request_body(body):
        return generate_invalid_req_body_error_message_response()

    category_name, parent = map_create_category(body)

    category = Category.objects.filter(name=category_name).exists()
    if category:
        return generate_bad_req_body_error_message_response()

    if parent:
        parent_of_the_category = Category.objects.get(name=parent)
        category = Category.objects.create(name=category_name, parentId=parent_of_the_category)
        category.save()

    else:
        category = Category.objects.create(name=category_name)
        category.save()

    data = {
        "message": "Category saved successfully"
    }
    return Response(data=data)

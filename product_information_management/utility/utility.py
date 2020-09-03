import json

from rest_framework import status
from rest_framework.response import Response

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


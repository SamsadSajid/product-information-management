from utility.utility import map_create_category


def is_valid_create_category_request_body(req_body):
    category_name, _ = map_create_category(req_body)

    if not category_name:
        return True

from utility.utility import map_create_category, map_create_article


def is_invalid_create_category_request_body(req_body):
    category_name, _ = map_create_category(req_body)

    if not category_name:
        return True
    return False


def is_invalid_create_article_request_body(req_body):
    name, stock_quantity, price, category_name = map_create_article(req_body)

    if not name:
        return True

    return False


def is_invalid_edit_category_request_body(req_body):
    category_name, parent = map_create_category(req_body)

    if not category_name or not parent:
        return True

    return False

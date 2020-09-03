from utility.request_validation import is_invalid_create_category_request_body


def test_is_valid_create_category_request_body_should_return_true_for_invalid_request_body():
    req_body = {
        "parent": "a category"
    }

    is_invalid_req_body = is_invalid_create_category_request_body(req_body)

    assert is_invalid_req_body == True, "The req body must contain the param `name`"


def test_is_valid_create_category_request_body_should_return_false_for_valid_request_body():
    req_body = {
        "name": "a category"
    }

    is_invalid_req_body = is_invalid_create_category_request_body(req_body)

    assert is_invalid_req_body == False, "The req body has the param `name`"


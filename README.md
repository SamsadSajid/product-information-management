# Product Information Management (PIM) - MVP

# Features
- As a user I can add a Category
- As a user I can add a Category to another category
- As a user I can update category
- As a user I can delete a Category
- As a user I can add an Article
- As a user I can add a category to an article
- As a user I can add multiple categories to an article
- As a user I can update an article
- As a user I can delete an article

# API Document
Request Header

|Header Name|Header Content|
|---|---|
|Content-Type|`application/json`|
|Accept|`application/json`|
|Authorization|`<accessToken>`|

## Create a Category
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/category/create` |

Request Body Field Description

| Field Name | Field Type | Mandatory|
|----------|-----------|----------|
|  `name`    | `String`   | YES|
|  `parent`    | `String`   | NO|


HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Post|
|400|Category already exists/Bad Request|

Sample Request Body
```
{
    "name":"Towel",
    "parent":"accessories"
}
```
Sample Response Body

```
{
    "message": "Category saved successfully"
}
```

## Update a Category
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/category/edit` |

Request Body Field Description

| Field Name | Field Type | Mandatory|
|----------|-----------|----------|
|  `name`  | `String`  | YES|
|  `parent`  | `String`  | YES|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Category updated successfully|
|400|Bad Request|

Sample Request Body
```
{
    "name":"jeans",
    "parent":"pants"
}
```
Sample Response Body

```
{
    "message": "Category updated successfully"
}
```

## Delete a Category
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/category/delete` |

Request Body Field Description

| Field Name | Field Type | Mandatory|
| ---------- | -----------|----------|
|  `name`    | `String`   | YES|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Deletion|
|400|Category already deleted/Bad Request|

Sample Request Body
```
{
    "name":"Towel"
}
```
Sample Response Body

```
{
    "message": "Category deleted successfully"
}
```

## Create an Article
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/article/create` |

Request Body Field Description

| Field Name | Field Type | Mandatory| Notes|
| ---------- | -----------|----------|----------|
|  `name`    | `String`   | YES|-|
|  `category_name`| `List<String>`   | NO|-|
|  `price`    | `Float`   | NO |max_digits=6, decimal_places=2|
|  `stock_quantity`    | `Integer`| NO |-|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Post|
|400|Article already exists/Bad Request|

Sample Request Body
```
{
    "name": "Kitchen Sink",
    "category_name": ["accessories","kitchenware"],
    "price": 212,
    "stock_quantity": 519
}
```
Sample Response Body

```
{
    "message": "Article saved successfully"
}
```

## Update an Article
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/article/edit` |

Request Body Field Description

| Field Name | Field Type | Mandatory| Notes|
| ---------- | -----------|----------|----------|
|  `name`    | `String`   | YES|-|
|  `category_name`| `List<String>`   | NO|-|
|  `price`    | `Float`   | NO |max_digits=6, decimal_places=2|
|  `stock_quantity`    | `Integer`| NO |-|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Post|
|400|Article does not exist/Bad Request|

Sample Request Body
```
{
    "name": "Kitchen Sink",
    "price": 350.12,
    "stock_quantity": 1024
}
```
Sample Response Body

```
{
    "message": "Article updated successfully"
}
```

## Delete an Article
| Request Method | Request Path |
| -------------- | -------------|
|      POST      | `api/article/delete`|

Request Body Field Description

| Field Name | Field Type | Mandatory|
|----------|-----------|----------|
|  `name`  | `String`  | YES|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Deletion|
|400|Article already exists/Bad Request|

Sample Request Body
```
{
    "name": "Kitchen Sink"
}
```
Sample Response Body

```
{
    "message": "Article deleted successfully"
}
```

## Get all articles for a category
| Request Method | Request Path |
| -------------- | -------------|
|      GET      | `api/article/get-all-articles?page=1`|

Request Body Field Description

| Field Name | Field Type | Mandatory|
|----------|-----------|----------|
|  `name`  | `String`  | YES|

HTTP Status Code

| Status Code | Type|
|---|---|
|200|Successful Deletion|
|400|Bad Request|

Sample Request Body
```
{
    "name":"kitchenware"
}
```
Sample Response Body

```
{
    "data": [
        {
            "sku": "50e1d0ef-ef8a-490a-930e-65f4cf8f0f94",
            "ean": "98b375b9-838c-461d-b3f0-3a199cc5303c",
            "price": 212.0,
            "name": "Oven",
            "stock_quantity": 519
        },
        {
            "sku": "c03620a6-9010-4fbc-b8f4-962d7d076406",
            "ean": "b3ea2c02-64a7-42fc-ace7-08d8037c8834",
            "price": 212.0,
            "name": "Kitchen Sink",
            "stock_quantity": 519
        }
    ],
    "hasNextPage": true,
    "pageSize": 2
}
```

# System Design

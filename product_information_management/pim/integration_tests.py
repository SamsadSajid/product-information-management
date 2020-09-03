# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()


import pytest

from pim.models import Category


"""
The following is an integration test that make connection to
the database and tries to create an entry for a Category
"""


@pytest.mark.django_db
def test_nested_category_should_create_one_parent_category_object():
    Category.objects.create(name="a_category")

    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_nested_category_should_create_one_parent_one_child_category_object():
    parent_category = Category.objects.create(name="parent_category")

    Category.objects.create(name="child_category", parent=parent_category)

    assert Category.objects.count() == 2

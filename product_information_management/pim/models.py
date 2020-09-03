from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    parentId = models.ForeignKey('self', null=True, related_name="parentRelationshipId", on_delete=models.SET_NULL)


# class CategoryRelationShip(models.Model):
#     categoryId = Category
#     parentCategoryId = Category

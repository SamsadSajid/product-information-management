from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    parent = models.ForeignKey('self', null=True, related_name="parentRelationshipId", on_delete=models.SET_NULL)
    isDeleted = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.isDeleted)

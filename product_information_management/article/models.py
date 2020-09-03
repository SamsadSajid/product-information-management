import uuid

from django.db import models
from django.utils import timezone

from pim.models import Category


class Article(models.Model):
    sku = models.UUIDField(default=uuid.uuid4(), editable=False)
    ean = models.UUIDField(default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, unique=True)
    stock_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    category = models.ForeignKey(Category, null=True, related_name="categoryRelationship", on_delete=models.SET_NULL)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.sku = uuid.uuid4()
            self.ean = uuid.uuid4()
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku + " " + self.ean + " " + self.name + " " + str(self.stock_quantity) + " " + self.price

from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=30)
    category_id = models.PositiveIntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name = models.ForeignKey(
        'ProductCategory', related_name='ProductCategory', on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    #!  3000.45
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

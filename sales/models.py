from django.db import models

class SalesData(models.Model):

    product_name = models.CharField(max_length=100)

    quantity = models.IntegerField()

    price = models.FloatField()

    sales_date = models.DateField()

    revenue = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):

        self.revenue = self.quantity * self.price

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
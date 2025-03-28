from django.db import models


class BaseModel(models.Model):
    cdate = models.DateTimeField(auto_now_add=True, verbose_name="created data")
    mdate = models.DateTimeField(auto_now=True, verbose_name="modified data")

    class Meta:
        abstract = True


class Dish(BaseModel):
    name = models.CharField(max_length=255, verbose_name="dish name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")

    def __str__(self) -> str:
        return self.name + "-" + str(self.price)


class Orders(BaseModel):
    CHOICES = {"w": "wait", "r": "ready", "p": "paid"}
    table_number = models.IntegerField(verbose_name="table number")
    items = models.ManyToManyField(Dish, related_name="order_items", verbose_name="items")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="total price", null=True, blank=True
    )
    status = models.CharField(max_length=2, choices=CHOICES, verbose_name="status", default="w")

    def __str__(self) -> str:
        return str(self.id)

from django.contrib.auth.models import User
from django.db import models
from product_list_page.models import *

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    note = models.CharField(max_length=200, null=True)

    def get_price_total(self):
        orderitems = self.orderitem_set.all()
        customitems = self.custommask_set.all()
        total = sum([item.get_total() for item in orderitems])
        totalcustom = sum([item.get_total() for item in customitems])
        return total + totalcustom

    def get_items_total(self):
        orderitems = self.orderitem_set.all()
        customitems = self.custommask_set.all()
        total = sum([item.quantity for item in orderitems])
        totalcustom = sum([item.quantity for item in customitems])
        return total + totalcustom

class OrderItem(models.Model):
    product = models.ForeignKey(ProdukMasker, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total = self.product.harga * self.quantity
        return total
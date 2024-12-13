from django.db import models
from django.conf import settings
from products.models import Product
from shippinfo.models import ShipInfo

class Order(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    shippingaddress = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pending', 'Pending'), 
            ('processing', 'Processing'), 
            ('shipped', 'Shipped'), 
            ('delivered', 'Delivered'), 
            ('cancelled', 'Cancelled'),
            ('completed', 'Completed')
        ], 
        default='pending'
    )
    total_price = models.FloatField(default=0)
    ship_info = models.OneToOneField(ShipInfo, null=True, blank=True, on_delete=models.SET_NULL)  

    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

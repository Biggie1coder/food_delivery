
from django.db import models
from django.contrib.auth import get_user_model


User= get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=45)
    phone_number = models.CharField(unique=True, max_length=11)
    
    
class FoodItem(models.Model):
    food_items = models.CharField(max_length=40)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class Orders(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    food_id = models.ForeignKey(to=FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivered = models.BooleanField()
    order_time = models.DateTimeField(auto_now_add=True)
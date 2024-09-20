from django.contrib import admin
from .models import Customer, FoodItem, Orders

admin.site.register(Customer)
admin.site.register(FoodItem)
admin.site.register(Orders)

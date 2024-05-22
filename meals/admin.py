from django.contrib import admin
from .models import MainCategory, GroupCategory, CuisineType, OrderItem

admin.site.register(MainCategory)
admin.site.register(GroupCategory)
admin.site.register(CuisineType)
admin.site.register(OrderItem)

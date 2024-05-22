from django.db import models
from datetime import timedelta

class MainCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class GroupCategory(models.Model):
    group_category_id = models.AutoField(primary_key=True)
    categories = models.ManyToManyField(MainCategory, related_name='group_categories')

    def __str__(self):
        return f"Group {self.group_category_id}"

class CuisineType(models.Model):
    id = models.AutoField(primary_key=True)
    cuisine_type = models.CharField(max_length=255)

    def __str__(self):
        return self.cuisine_type

class OrderItem(models.Model):
    MEAL_TYPE_CHOICES = [
        ('b', 'Breakfast'),
        ('d', 'Dinner'),
        ('l', 'Lunch')
    ]
    
    order_item_id = models.AutoField(primary_key=True)
    ingredients = models.TextField()  # Assuming ingredients are stored as a comma-separated string
    order_id = models.CharField(max_length=255)
    dish_name = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPE_CHOICES)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.CASCADE)
    dish_info = models.TextField()
    preparation_time = models.DurationField(default=timedelta(minutes=10))
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(GroupCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_name

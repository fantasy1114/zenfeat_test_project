from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class OrderItem(models.Model):
    dish_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    meal_type = models.CharField(max_length=1, choices=(('D', 'Dinner'), ('L', 'Lunch')))
    cuisine_type = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='order_items')

    def __str__(self):
        return self.dish_name

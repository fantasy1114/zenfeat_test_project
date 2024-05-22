from django.shortcuts import render
from django.core.cache import cache
from .models import OrderItem

def get_meals_by_category(request, category_id):
    cache_key = f'meals_{category_id}'
    meals = cache.get(cache_key)
    
    if not meals:
        meals = list(OrderItem.objects.filter(main_category_id=category_id).values())
        cache.set(cache_key, meals, timeout=300)  # Cache for 5 minutes

    return render(request, 'meals/list.html', {'meals': meals})

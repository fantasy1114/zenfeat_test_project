from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:category_id>/meals/', views.get_meals_by_category, name='meals_by_category'),
]

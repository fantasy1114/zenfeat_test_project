from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls')),  # Include URLs from the meals app
]
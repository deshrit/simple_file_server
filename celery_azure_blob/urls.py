from django.urls import path
from .views import index, delete, refresh

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:id>/', delete, name="delete"),
    path('refresh/', refresh, name="refresh"),
]
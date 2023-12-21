from django.urls import path, include
from .views import Home_lest

urlpatterns = [
    path('', Home_lest, name='home'),
]

from django.urls import path
from .views import multiply

urlpatterns = [
    path('multiply/', multiply),
]

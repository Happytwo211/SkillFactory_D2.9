from .views import multiply
from django.urls import path


urlpatterns = [
   path('', multiply),
]
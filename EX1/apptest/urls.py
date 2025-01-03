from django.urls import path
from .views import ProductsList, ProductDetail
from django.http import HttpResponse

urlpatterns = [
   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),


]
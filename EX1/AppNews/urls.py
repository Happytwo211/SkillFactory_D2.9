from django.urls import path
from .views import News_Detail,News_List

urlpatterns =[
    path('',News_List.as_view()),
    path('<int:pk>', News_Detail),
]
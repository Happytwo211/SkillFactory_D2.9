from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class News_List(ListView):
    model = News
    ordering = 'news_name'
    template_name = 'app_news.html'
    context_object_name = 'news'





# Create your views here.
class News_Detail(DetailView):
    model = News
    template_name = 'app_news_id.html'
    context_object_name = 'newsid'
    def get_context_data(self,  **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['publish_date'] = News.news_publish_date
        return contex


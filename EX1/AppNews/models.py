from django.db import models

class News(models.Model):
    news_name = models.CharField(max_length=50)
    news_body_text = models.TextField(max_length=500)
    news_category = models.ForeignKey('News_Category', on_delete=models.CASCADE, related_name='News')
    news_publish_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.news_name.title()}'
                # f'{self.news_body_text[:30]}')
    #
    # def __str__(self):
    #     return f'{self.news_publish_date}'

# Create your models here.
class News_Category(models.Model):
    category_news_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_news_name.title()
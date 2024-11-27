from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    author_to_user = models.OneToOneField('User', on_delete=models.CASCADE, default=True)
    user_rating = models.IntegerField(default=0.0)

    def update_rating(self):
        for i in Post.sum_post_rating_storage:
            sum_author_post_rating = sum(i)
            sum_author_post_rating * 3
            return sum_author_post_rating

        for i in Comment.sum_comment_rating_storage:
            sum_author_comments_rating = sum(i)
            return sum_author_comments_rating

        for i in Comment.sum_comment_to_user_rating_storage:
            sum_comments_to_author_post = sum(i)
            return sum_comments_to_author_post


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=50)

class Post(models.Model):
    author_to_post = models.ForeignKey('Author', on_delete=models.CASCADE)
    article = "AR"
    news = "NW"
    POSITION = [
        (article,'Article'),
        (news,'News')
    ]
    choose = models.CharField(max_length=2, choices=POSITION, null=False)
    time_add = models.DateTimeField(auto_now=True)
    date_add = models.DateTimeField(auto_now_add=True)
    post_to_post_category = models.ManyToManyField('PostCategory', default=True)
    post_title_name = models.CharField(max_length=100, null=False, default='...')
    post_body_text = models.TextField(max_length=10000, null=False, default='...')
    post_rating = models.IntegerField(default=0.0)
    sum_post_rating_storage = []


    def post_like(self):
        self.post_rating = self.post_rating + 1
        self.save()


    def post_dislike(self):
        self.post_rating = self.post_rating - 1
        self.save()

    sum_post_rating_storage.append(post_rating)


    # def post_rating_sum_storage(self):
    #     self.sum_post_rating.append(self.post_rating)
    #     self.save()

class PostCategory(models.Model):
    post_category_to_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    post_category_to_category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Comment(models.Model):
    comment_to_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_to_user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment_body = models.CharField(max_length=255)
    comment_time = models.DateTimeField(auto_now=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0.0)
    sum_comment_rating_storage = []
    sum_comment_to_user_rating_storage = []
    def comment_like(self):
        self.comment_rating = self.comment_rating + 1
        self.save()

    def comment_dislike(self):
        self.comment_rating = self.comment_rating - 1
        self.save()

    sum_comment_rating_storage.append(comment_rating)
    sum_comment_to_user_rating_storage.append(comment_to_user)
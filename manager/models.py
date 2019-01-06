from django.db import models
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    screen_name = models.CharField(max_length=50, default=None, unique=True)
    # refine_keyword = models.CharField(max_length=200)
    # regist_date = models.DateTimeField(default=timezone.now)


class RefineTweet(models.Model):
    created_at = models.CharField(max_length=200)
    text = models.CharField(max_length=280)
    url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='refine_tweets', default=None)


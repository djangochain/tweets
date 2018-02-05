from django.db import models
from django.utils.translation import ugettext_lazy as _
from tweetapp.manager import TweetManager

class HashTags(models.Model):
    name = models.CharField(max_length=255,unique=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)
    class Meta:
        db_table = "tweets_hashtags"
        ordering = ['modified_date']


class Tweets(models.Model):
    screen_name = models.CharField(max_length=200,blank=True,null=True)
    user_name = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    source_device = models.CharField(max_length=200,blank=True,null=True)
    is_retweeted = models.BooleanField(default=False)
    retweet_count = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=200,blank=True,null=True)
    country_code = models.CharField(max_length=200,blank=True,null=True)
    reply_count = models.PositiveIntegerField(default=0)
    favorite_count = models.PositiveIntegerField(default=0)
    tweet_text = models.TextField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField()
    timestamp_ms = models.CharField(max_length=200)
    lang = models.CharField(max_length=200,blank=True,null=True)
    tweet_id = models.CharField(max_length=255,unique=True)
    hash_tags = models.ManyToManyField(HashTags)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)
    objects = TweetManager()

    class Meta:
        db_table = "tweets_data"
        ordering = ['modified_date']


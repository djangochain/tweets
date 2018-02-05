from rest_framework.response import Response
# from django.conf import settings
from rest_framework import serializers
from tweetapp.models import Tweets

class TweetsListingSerializer(serializers.ModelSerializer):
    hash_tags = serializers.SerializerMethodField()
    class Meta:
        model = Tweets
        fields = (

            'screen_name', 'user_name', 'location', 'source_device', 'is_retweeted', 'retweet_count', 'country', 'country_code',
            'reply_count', 'favorite_count', 'tweet_text', 'created_at', 'timestamp_ms',
            'lang', 'tweet_id','hash_tags')

    def get_hash_tags(self,obj):
        return obj.hash_tags.all().values_list("name",flat=True)






from django.db import models


class TweetManager(models.Manager):
    def create_tweet(self, data,hash_tags):
        try:
            self.get(tweet_id=data["tweet_id"])
        except:
            del(data["hashtags"])
            try:
                obj = self.create(**data)
                obj.hash_tags.add(*hash_tags)
            except:
                pass

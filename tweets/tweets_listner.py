from tweepy.streaming import StreamListener
from tweetapp.models import Tweets,HashTags

class TweetsDataListener(StreamListener):
    # on success
    def on_status(self, status):
        hashtags = []
        for hashtag in status.entities['hashtags']:
            hashtags.append(hashtag['text'])

        tags = []
        for hashtag in hashtags:
            tag, create = HashTags.objects.get_or_create(name=hashtag)
            tags.append(tag)

        country = status.place.country if status.place is not None else ""
        country_code = status.place.country_code if status.place is not None else ""
        doc = {
            "screen_name": status.user.screen_name,
            "user_name": status.user.name,
            "location": status.user.location,
            "source_device": status.source,
            "is_retweeted": status.retweeted,
            "retweet_count": status.retweet_count,
            "country": country,
            "country_code": country_code,
            "reply_count": status.reply_count,
            "favorite_count": status.favorite_count,  # likes
            "tweet_text": status.text,
            "created_at": status.created_at,
            "timestamp_ms": status.timestamp_ms,
            "lang": status.lang,
            "hashtags": hashtags,
            "tweet_id":status.id_str
        }
        Tweets.objects.create_tweet(doc,hash_tags=tags)
        # Updates mapping958753336668426240
        # mapping_res = es.indices.put_mapping(index="tweets_index", doc_type="tweet", body=es_mappings.get("tweet_index"))

        # mappings = es_mappings.get("tweet_index")
        # # Creates mapping
        # mapping_res = es.indices.create(index="tweets_index", ignore=400,
        #                                 body=json.dumps(mappings))
        # c_res = es.index(index="tweets_index", doc_type="tweet", body=doc)
        return True

    # on failure
    def on_error(self, status):
        print status

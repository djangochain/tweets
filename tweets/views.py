from rest_framework.views import APIView
from rest_framework.response import Response
from tweets.fetch_tweets import Tweety
from tweets.query_builder import *
from tweetapp.models import Tweets
from tweetapp.serializers import TweetsListingSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class GetWoiedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tweety = Tweety()
        woied = tweety.get_woied()
        return Response(woied)


class StartStreamingAPIView(APIView):
    def get(self, request, *args, **kwargs):
        keyword = request.GET.get("keyword",None)
        woeid = request.GET.get("woeid", "1")
        tweety = Tweety()
        tweety.filter(keyword,woeid)
        return Response({"success":True})


class FilterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        search_text = request.data
        a = QueryBuilder(search_text)
        sort_by = search_text["sort"]
        b = Tweets.objects.filter(*a.get_query()).order_by(*sort_by)
        page = request.data.get('page','1') #current page number
        per_page_records = request.data.get('no_records', '20') # No of records in a page
        paginator = Paginator(b,per_page_records)
        try:
            tweets = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            tweets = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            tweets = paginator.page(paginator.num_pages)
        serializer = TweetsListingSerializer(tweets, many=True)
        return Response({"tweets":serializer.data,"total_no_records":paginator.count,"per_page_records":per_page_records
                            ,"current_page":page,"total_pages":paginator.num_pages})
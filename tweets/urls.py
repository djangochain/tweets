"""tweets URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from tweets.views import StartStreamingAPIView,FilterAPIView,GetWoiedAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get-woied/$', GetWoiedAPIView.as_view()),
    url(r'^start-stream/$', StartStreamingAPIView.as_view()),
    url(r'^get-filter-data/$', FilterAPIView.as_view()),
]


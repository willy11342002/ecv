from django.conf.urls import include
from django.urls import path
from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^lineitem/summary/(?P<usageaccountid>\d+)/?$', views.SummaryItem.as_view()),
    re_path(r'^lineitem/summary/day/(?P<usageaccountid>\d+)/?$', views.SummaryItemByDays.as_view()),
]
from django.conf.urls import include
from django.urls import path
from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^lineitem/(?P<usageaccountid>\d+)/products/summary/unblendedcost/?$', views.SummaryItem.as_view()),
    re_path(r'^lineitem/(?P<usageaccountid>\d+)/products/summary/daily/usageamount/?$', views.SummaryItemByDays.as_view()),
]
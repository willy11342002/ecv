from django.db.models import Count, Avg, Sum, Min, Max, Q
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from itertools import groupby
from . import models
import datetime


class SummaryItem(View):
    def get(self, request, usageaccountid):
        items = models.LineItem.objects
        items = items.select_related('product')
        items = items.filter(UsageAccountId=usageaccountid)
        items = items.values('product__ProductName')
        items = items.annotate(Sum('UsageAmount'))
        items = {
            item['product__ProductName']: f"{item['UsageAmount__sum']:.2f}"
            for item in items
        }

        return JsonResponse(items)


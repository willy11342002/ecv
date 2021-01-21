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


class SummaryItemByDays(View):
    def get(self, request, usageaccountid):
        items = models.LineItem.objects
        items = items.select_related('product')
        items = items.filter(UsageAccountId=usageaccountid)
        items = items.order_by('product')

        res = {}
        for product, its in groupby(items, key=lambda x: x.product):
            res[product.ProductName] = {}
            its = list(its)
            sday = min(its, key=lambda x: x.UsageStartDate).UsageStartDate.date()
            eday = max(its, key=lambda x: x.UsageEndDate).UsageEndDate.date()

            for i in range(0, (eday - sday).days+1):
                mday = sday + datetime.timedelta(days=i)
                today_its = filter(lambda x: x.UsageStartDate.date() <= mday <= x.UsageEndDate.date(), its)
                today_its = map(lambda x: x.UsageAmount, today_its)
                res[product.ProductName][mday.strftime(r'%Y/%m/%d')] = f'{sum(today_its):.2f}'

        return JsonResponse(res)

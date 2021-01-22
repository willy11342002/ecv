from django.db.models import Count, Avg, Sum, Min, Max, Q
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from collections import Counter
from itertools import groupby
from . import models
import datetime


class SummaryItem(View):
    def get(self, request, usageaccountid):
        items = models.LineItem.objects
        items = items.select_related('product')
        items = items.filter(UsageAccountId=usageaccountid)
        items = items.values('product__ProductName')
        items = items.annotate(Sum('UnblendedCost'))
        items = {
            item['product__ProductName']: f"{item['UnblendedCost__sum']:.2f}"
            for item in items
        }

        return JsonResponse(items)


class SummaryItemByDays(View):
    def daysUseage(self, item):
        rate = item.UsageAmount / (item.UsageEndDate.timestamp() - item.UsageStartDate.timestamp())
        res = {}
        sdate = item.UsageStartDate
        edate = datetime.datetime.strptime(sdate.strftime(r'%Y%m%d %z'), r'%Y%m%d %z')
        edate = edate + datetime.timedelta(days=1)
        edate = min(edate, item.UsageEndDate)
        while sdate < edate:
            res[sdate.strftime(r'%Y/%m/%d')] = rate * (edate.timestamp() - sdate.timestamp())
            sdate += datetime.timedelta(days=1)
            edate += datetime.timedelta(days=1)
            edate = min(edate, item.UsageEndDate)

        return res

    def get(self, request, usageaccountid):
        items = models.LineItem.objects
        items = items.select_related('product')
        items = items.filter(UsageAccountId=usageaccountid)
        items = items.order_by('product')

        results = {}
        for product, its in groupby(items, key=lambda x: x.product):
            its = [self.daysUseage(it) for it in its]

            res = dict(sum([Counter(it) for it in its], Counter()))
            res = {k: f'{v:.2f}' for k, v in res.items()}

            results[product.ProductName] = res

        return JsonResponse(results)

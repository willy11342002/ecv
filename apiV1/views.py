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
    def dailyUseage(self, item):
        rate = item.UsageAmount / (item.UsageEndDate.timestamp() - item.UsageStartDate.timestamp())
        res = {}
        sdate = item.UsageStartDate
        edate = datetime.datetime.strptime(sdate.strftime(r'%Y%m%d %z'), r'%Y%m%d %z')
        edate = edate + datetime.timedelta(days=1)
        edate = min(edate, item.UsageEndDate)
        while sdate < edate:
            res[sdate.strftime(r'%Y/%m/%d')] = rate * (edate.timestamp() - sdate.timestamp())
            sdate = edate
            edate += datetime.timedelta(days=1)
            edate = min(edate, item.UsageEndDate)

        return res

    def get(self, request, usageaccountid):
        items = models.LineItem.objects
        items = items.select_related('product')
        items = items.filter(UsageAccountId=usageaccountid)

        results = {}
        for item in items:
            product = results.get(item.product.ProductName)
            if not product:
                results[item.product.ProductName] = product = {}

            for dt, value in self.dailyUseage(item).items():
                product[dt] = product.get(dt, 0) + value

        results = {
            pname: {
                dt: f'{product[dt]:.2f}'
                for dt in sorted(product.keys())
            }
            for pname, product in results.items()
        }

        return JsonResponse(results)

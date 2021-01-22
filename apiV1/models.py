from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Bill(models.Model):
    InvoiceId = models.PositiveIntegerField()
    BillingEntity = models.CharField(max_length=16)
    BillType = models.CharField(max_length=16)
    PayerAccountId = models.PositiveIntegerField()
    BillingPeriodStartDate = models.DateField()

    def __str__(self):
        return f'{self.InvoiceId}'

class Product(models.Model):
    ProductName = models.CharField(max_length=128)
    cacheEngine = models.CharField(max_length=16, null=True, blank=True)
    databaseEdition = models.CharField(max_length=16, null=True, blank=True)
    databaseEngine = models.CharField(max_length=32, null=True, blank=True)
    deploymentOption = models.CharField(max_length=32, null=True, blank=True)
    instanceType = models.CharField(max_length=32, null=True, blank=True)
    instanceTypeFamily = models.CharField(max_length=8, null=True, blank=True)
    licenseModel = models.CharField(max_length=32, null=True, blank=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    operatingSystem = models.CharField(max_length=8, null=True, blank=True)
    region = models.CharField(max_length=32, null=True, blank=True)
    tenancy = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.ProductName}'


class LineItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    UsageAccountId = models.PositiveIntegerField(db_index=True)
    LineItemType = models.CharField(max_length=28)
    UsageStartDate = models.DateTimeField()
    UsageEndDate = models.DateTimeField()
    UsageType = models.CharField(max_length=64)
    Operation = models.CharField(max_length=64, null=True, blank=True)
    AvailabilityZone = models.CharField(max_length=16, null=True, blank=True)
    ResourceId = models.CharField(max_length=128, null=True, blank=True)
    UsageAmount = models.FloatField()
    NormalizationFactor = models.FloatField(null=True, blank=True)
    NormalizedUsageAmount = models.FloatField(null=True, blank=True)
    UnblendedRate = models.FloatField(null=True, blank=True)
    UnblendedCost = models.FloatField()
    LineItemDescription = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.bill} ({self.UsageAccountId}) {self.LineItemType}'



# class Pricing(models.Model):
#     LeaseContractLength = models.CharField(max_length=512, null=True, blank=True)
#     OfferingClass = models.CharField(max_length=512, null=True, blank=True)
#     PurchaseOption = models.CharField(max_length=512, null=True, blank=True)
#     publicOnDemandRate = models.CharField(max_length=512, null=True, blank=True)
#     term = models.CharField(max_length=512, null=True, blank=True)


# class Reservation(models.Model):
#     AmortizedUpfrontCostForUsage = models.CharField(max_length=512, null=True, blank=True)
#     AmortizedUpfrontFeeForBillingPeriod = models.CharField(max_length=512, null=True, blank=True)
#     EffectiveCost = models.CharField(max_length=512, null=True, blank=True)
#     EndTime = models.CharField(max_length=512, null=True, blank=True)
#     ModificationStatus = models.CharField(max_length=512, null=True, blank=True)
#     NumberOfReservations = models.CharField(max_length=512, null=True, blank=True)
#     RecurringFeeForUsage = models.CharField(max_length=512, null=True, blank=True)
#     ReservationARN = models.CharField(max_length=512, null=True, blank=True)
#     StartTime = models.CharField(max_length=512, null=True, blank=True)
#     SubscriptionId = models.PositiveIntegerField(null=True, blank=True)
#     TotalReservedUnits = models.CharField(max_length=512, null=True, blank=True)
#     UnusedAmortizedUpfrontFeeForBillingPeriod = models.CharField(max_length=512, null=True, blank=True)
#     UnusedNormalizedUnitQuantity = models.CharField(max_length=512, null=True, blank=True)
#     UnusedQuantity = models.CharField(max_length=512, null=True, blank=True)
#     UnusedRecurringFee = models.CharField(max_length=512, null=True, blank=True)
#     UpfrontValue = models.CharField(max_length=512, null=True, blank=True)


# class SavingsPlan(models.Model):
#     TotalCommitmentToDate = models.CharField(max_length=512, null=True, blank=True)
#     SavingsPlanARN = models.CharField(max_length=512, null=True, blank=True)
#     SavingsPlanRate = models.CharField(max_length=512, null=True, blank=True)
#     UsedCommitment = models.CharField(max_length=512, null=True, blank=True)
#     SavingsPlanEffectiveCost = models.CharField(max_length=512, null=True, blank=True)
#     AmortizedUpfrontCommitmentForBillingPeriod = models.CharField(max_length=512, null=True, blank=True)
#     RecurringCommitmentForBillingPeriod = models.CharField(max_length=512, null=True, blank=True)
#     PurchaseTerm = models.CharField(max_length=512, null=True, blank=True)
#     PaymentOption = models.CharField(max_length=512, null=True, blank=True)
#     OfferingType = models.CharField(max_length=512, null=True, blank=True)
#     Region = models.CharField(max_length=512, null=True, blank=True)
#     StartTime = models.CharField(max_length=512, null=True, blank=True)
#     EndTime = models.CharField(max_length=512, null=True, blank=True)

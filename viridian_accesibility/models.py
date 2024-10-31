from django.db import models
from django.db.models import Q

class Referral(models.Model):
    referral = models.IntegerField()
    datetime = models.DateTimeField()
    user_address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('referral', 'datetime', 'user_address')

class Deposit(models.Model):
    user_address = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    assets = models.DecimalField(max_digits=78, decimal_places=0)
    tx_hash = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        return f"Deposit by {self.user_address} on {self.datetime} for {self.assets} ({self.tx_hash})"

    @property
    def is_tagged(self):
        return Referral.objects.exists(datetime=self.datetime)

class Withdrawal(models.Model):
    user_address = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    assets = models.DecimalField(max_digits=78, decimal_places=0)
    tx_hash = models.CharField(max_length=100, unique=True)

    @property
    def association(self):
        return Tag.objects.filter(Q(start__lt=self.datetime)).order_by("end").first

class Tag(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    referral = models.IntegerField()
    user = models.CharField(max_length=100)

    class Meta:
        unique_together = "start", "end", "referral", "user"

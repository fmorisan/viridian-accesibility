from django.core.management.base import BaseCommand
from viridian_accesibility.models import Deposit, Withdrawal, Referral, Tag
import itertools


class Command(BaseCommand):
    def handle(self, *args, **opts):
        referrals = Referral.objects.all()
        affected_users = referrals.values_list("user_address")

        def group_iter(iterable):
            for i in range(len(iterable) - 1):
                yield iterable[i], iterable[i + 1]

        for user,  in affected_users:
            user_referrals = referrals.filter(user_address=user).order_by("datetime")
            for start, end in group_iter(user_referrals):
                Tag.objects.get_or_create(start=start.datetime, end=end.datetime, referral=start.referral, user=user)

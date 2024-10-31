import os
import csv
import sys
from django.core.management.base import BaseCommand
from dataclasses import dataclass
from viridian_accesibility.models import Deposit, Withdrawal, Referral

class Command(BaseCommand):
    help = "create model objects"
    def add_arguments(self, ap):
        group = ap.add_mutually_exclusive_group(required=True)
        group.add_argument('--deposit', action='store_const', const='deposit', dest='mode')
        group.add_argument('--withdrawal', action='store_const', const='withdrawal', dest='mode')
        group.add_argument('--referral', action='store_const', const='referral', dest='mode')
        ap.add_argument('file')

    def handle(self, *args, **options):
        path = os.path.abspath(options['file'])
        klass = None
        if options['mode'] == "deposit":
            klass = Deposit
        elif options['mode'] == "withdrawal":
            klass = Withdrawal
        elif options['mode'] == "referral":
            klass = Referral

        if not klass:
            print("no valid mode provided")
            sys.exit(1)

        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for line in reader:
                if line['datetime'].endswith(" UTC"):
                    line['datetime'] = line['datetime'][:-4] + "Z"
                try:
                    model = klass.objects.get_or_create(**line)
                except Exception as e:
                    print("skipping line due to", e)

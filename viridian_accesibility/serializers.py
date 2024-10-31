from viridian_accesibility.models import Deposit, Withdrawal, Referral, Tag

from rest_framework.serializers import ModelSerializer

class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        exclude = "id",

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        exclude = "id",

class WithdrawalSerializer(ModelSerializer):
    class Meta:
        model = Withdrawal
        exclude = "id",

class ReferralSerializer(ModelSerializer):
    class Meta:
        model = Referral
        exclude = "id",

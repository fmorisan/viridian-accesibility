from django.http import HttpResponse
from viridian_accesibility.models import Deposit, Referral, Tag
from viridian_accesibility.serializers import DepositSerializer, TagSerializer
from django.db.models import Q
import json

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

class DepositViewSet(ReadOnlyModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

    @action(detail=False)
    def tagged(self, request):
        referrals = Referral.objects.all().values_list("datetime")
        tagged = self.queryset.filter(
            Q(datetime__in=referrals)
        )

        serializer = self.get_serializer(tagged, many=True)
        return Response(serializer.data)

class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = DepositSerializer

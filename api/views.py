from .models import BtcHistory
from rest_framework import viewsets
from .serializers import BtcHistorySerializer


class BtcHistoryView(viewsets.ModelViewSet):
    queryset = BtcHistory.objects.all().order_by('-date')
    serializer_class = BtcHistorySerializer
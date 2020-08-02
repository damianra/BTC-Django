from .models import BtcHistory
from rest_framework import serializers

class BtcHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BtcHistory
        fields = ['date', 'close', 'open', 'max_value', 'min_value', 'vol', 'var']

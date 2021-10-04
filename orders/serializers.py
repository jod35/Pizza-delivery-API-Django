from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    flavour=serializers.CharField(max_length=40)

    class Meta:
        model=Order 
        fields=['order_status', 'size', 'quantity','flavour']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length=25)

    class Meta:
        model=Order
        fields=['order_status']

from rest_framework import serializers
from ..Models.StockIndex import StockIndex


class StockIndexSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    open_val = serializers.DecimalField(max_digits=19, decimal_places=4)
    high_val = serializers.DecimalField(max_digits=19, decimal_places=4)
    low_val = serializers.DecimalField(max_digits=19, decimal_places=4)
    close_val = serializers.DecimalField(max_digits=19, decimal_places=4)
    adjclose_val = serializers.DecimalField(max_digits=19, decimal_places=4)
    volume_val = serializers.IntegerField()
    symbol = serializers.CharField()

    def create(self, validated_data):
        return StockIndex.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.open_val = validated_data.get('open_val', instance.open_val)
        instance.date = validated_data.get('date', instance.date)
        instance.high_val = validated_data.get('high_val',instance.high_val)
        instance.low_val = validated_data.get('low_val',instance.low_val)
        instance.close_val = validated_data.get('close_val',instance.close_val)
        instance.adjclose_val = validated_data.get('adjclose_val',instance.adjclose_val)
        instance.volume_val = validated_data.get('volume_val',instance.volume_val)
        instance.symbol = validated_data.get('symbol',instance.symbol)

        instance.save()
        return instance

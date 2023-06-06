from rest_framework import serializers

from ..Models.Company import Company


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    symbol = serializers.CharField()
    weight = serializers.DecimalField(max_digits=19, decimal_places=4)
    price = serializers.DecimalField(max_digits=19, decimal_places=4)
    chg = serializers.DecimalField(max_digits=19, decimal_places=4)
    percent_chg = serializers.DecimalField(max_digits=19, decimal_places=4)
    founded = serializers.IntegerField()
    sector = serializers.CharField()
    sub_sector = serializers.CharField()

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.chg = validated_data.get('chg', instance.chg)
        instance.percent_chg = validated_data.get('percent_chg', instance.percent_chg)
        instance.founded = validated_data.get('founded', instance.founded)
        instance.sector = validated_data.get('sector', instance.sector)
        instance.sub_sector = validated_data.get('sub_sector', instance.sub_sector)

        instance.save()
        return instance

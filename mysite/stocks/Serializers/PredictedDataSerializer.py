from rest_framework import serializers


class PredictedDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    close_val = serializers.DecimalField(max_digits=19, decimal_places=4)

    def create(self, validated_data):
        return

    def update(self, instance, validated_data):
        return
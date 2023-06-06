from rest_framework.views import APIView

from ..Models.Company import Company
from ..Models.StockIndex import StockIndex
from ..Serializers.StockIndexSerializer import StockIndexSerializer
from rest_framework.response import Response


class StockIndexAPIView(APIView):
    def get(self, request, **kwargs):
        length = request.query_params.get('length', None)
        symbol = kwargs.get("symbol", None)
        if not symbol:
            al = StockIndex.objects.order_by('datetime')
        else:
            id = Company.objects.filter(symbol=symbol)[0].id
            al = StockIndex.objects.filter(symbol=id).order_by('date')

        if length:
            length = int(length)
            all_len = len(al)
            al = al[all_len - length:]

        serializer = StockIndexSerializer(al, many=True)

        return Response(serializer.data)

    def post(self, request):
        serial = StockIndexSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response(serial.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        if not id:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = StockIndex.objects.get(pk=id)
        except:
            return Response({"error": 'Object does not exist'})

        serializer = StockIndexSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response

from ..Models.HistoricalDataIndex import HistoricalDataIndex
from ..Serializers.HistoricalDataIndexSerializer import HistoricalDataIndexSerializer


class HistoricalDataIndexAPIView(APIView):
    def get(self, request, **kwargs):
        length = request.query_params.get('length', None)
        hist_data = HistoricalDataIndex.objects.order_by('date')
        if length:
            length = int(length)
            all_len = len(hist_data)
            hist_data = hist_data[all_len - length:]
        queryset = HistoricalDataIndexSerializer(hist_data, many=True)
        return Response(queryset.data)
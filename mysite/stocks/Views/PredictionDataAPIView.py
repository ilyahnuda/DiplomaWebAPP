import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from ..NeuralNetwork import NeuralNetwork
from ..Serializers.PredictedDataSerializer import PredictedDataSerializer
from ..Models.StockIndex import StockIndex


class PredictionDataAPIView(APIView):
    model = NeuralNetwork()

    def get(self, request):
        days = request.query_params.get('days', None)
        company_id = request.query_params.get('company_id', None)

        if not (days and company_id):
            return Response("You have to fill all inputs")

        days = int(days)
        data = StockIndex.objects.filter(symbol=company_id).values().order_by('date')
        data = data[len(data) - 40:]
        data_str = data[-1]['datetime']
        time_series = [datetime.timedelta(days=x + 1) + data_str for x in range(days)]
        predictions = self.model.predict(data, days)
        print(predictions)
        result = [{'date': time_series[i], 'close_val': predictions[i][4]} for i in range(days)]

        serialized_data = PredictedDataSerializer(result, many=True).data

        return Response(serialized_data)

from rest_framework.views import APIView

from ..Models.Company import Company
from ..Serializers.CompanySerializer import CompanySerializer
from rest_framework.response import Response


class CompanyAPIView(APIView):
    def get(self, request, **kwargs):
        symbol = kwargs.get("symbol", None)
        name = request.query_params.get('name', None)
        if not symbol:
            if not name:
                all = Company.objects.all().order_by('id')
            else:
                all = Company.objects.filter(name__istartswith=name).order_by('id')
            serializer = CompanySerializer(all, many=True)

        else:
            all = Company.objects.filter(symbol=symbol)[0]
            serializer = CompanySerializer(all)

        return Response(serializer.data)

    def post(self, request):
        serial = CompanySerializer(data=request.data)
        serial.is_valid()
        serial.save()
        return Response(serial.data)

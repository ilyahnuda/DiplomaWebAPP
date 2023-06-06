from rest_framework.views import APIView
from rest_framework.response import Response

from ..Models.News import News
from ..Serializers.NewsSerializer import NewsSerializer


class NewsAPIView(APIView):
    def get(self, request, **kwargs):
        title = kwargs.get("title", None)
        query_title = request.query_params.get('title', None)
        if not title:
            if not query_title:
                all = News.objects.all()
            else:
                all = News.objects.filter(title__istartswith=query_title)
            serializer = NewsSerializer(all, many=True)
        else:
            all = News.objects.filter(title__istartswith=title)[0]
            serializer = NewsSerializer(all)
        return Response(serializer.data)

    def post(self, request):
        serial = NewsSerializer(data=request.data)
        serial.is_valid()
        serial.save()
        return Response(serial.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        if not id:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = News.objects.get(pk=id)
        except:
            return Response({"error": 'Object does not exist'})

        serializer = NewsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
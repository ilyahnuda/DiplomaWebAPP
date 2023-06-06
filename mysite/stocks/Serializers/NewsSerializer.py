from rest_framework import serializers

from .AuthorSerializer import AuthorSerializer
from ..Models.News import News


class NewsSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'

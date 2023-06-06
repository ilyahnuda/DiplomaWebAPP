from django.contrib import admin
from django.urls import path, include

from .Views.CompanyAPIView import CompanyAPIView
from .Views.HistoricalDataIndexAPIView import HistoricalDataIndexAPIView
from .Views.NewsAPIView import NewsAPIView
from .Views.PredictionDataAPIView import PredictionDataAPIView
from .Views.StockIndexAPIView import StockIndexAPIView
from .views import *
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'stock', StockIndexViewSet)
urlpatterns = [
    path('stockslist', StockIndexAPIView.as_view()),
    path('stockslist/<str:symbol>/', StockIndexAPIView.as_view()),
    path('news', NewsAPIView.as_view()),
    path('news/<str:title>', NewsAPIView.as_view()),
    path('company', CompanyAPIView.as_view()),
    path('company/<str:symbol>', CompanyAPIView.as_view()),
    path('indexdata', HistoricalDataIndexAPIView.as_view()),
    path('predictedata',PredictionDataAPIView.as_view()),
    # path('v1/', include(router.urls))
]

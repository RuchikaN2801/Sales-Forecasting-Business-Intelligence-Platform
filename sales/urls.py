from django.urls import path
from .views import XGBoostForecastView
from .views import ForecastView
from .views import (
    SalesListCreateView,
    CSVUploadView,
    AnalyticsView,
    RevenueTrendView
)

urlpatterns = [
    path(
        'xgboost-forecast/',
        XGBoostForecastView.as_view(),
        name='xgboost-forecast'
    ),

    path(
        'sales/',
        SalesListCreateView.as_view(),
        name='sales'
    ),

    path(
        'upload-csv/',
        CSVUploadView.as_view(),
        name='upload-csv'
    ),

    path(
        'analytics/',
        AnalyticsView.as_view(),
        name='analytics'
    ),

    path(
        'revenue-trend/',
        RevenueTrendView.as_view(),
        name='revenue-trend'
    ),
    path(
        'forecast/',
        ForecastView.as_view(),
        name='forecast'
    ),
    
]
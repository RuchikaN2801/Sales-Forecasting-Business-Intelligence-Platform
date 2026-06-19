from prophet import Prophet
import pandas as pd
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from xgboost import XGBRegressor
import numpy as np

from .models import SalesData
from .serializers import SalesDataSerializer, CSVUploadSerializer

import pandas as pd


class SalesListCreateView(generics.ListCreateAPIView):

    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer


class CSVUploadView(APIView):
    def get(self, request):
        return Response({
            "message": "Use POST request with CSV file"
        })

    def post(self, request):

        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():

            csv_file = serializer.validated_data['file']

            df = pd.read_csv(csv_file)

            for _, row in df.iterrows():

                SalesData.objects.create(
                    product_name=row['product_name'],
                    quantity=row['quantity'],
                    price=row['price'],
                    sales_date=row['sales_date'],
                    revenue=row['quantity'] * row['price']
                )

            return Response(
                {"message": "CSV uploaded successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class AnalyticsView(APIView):

    def get(self, request):

        sales = SalesData.objects.all()

        total_revenue = 0

        for sale in sales:
            total_revenue += sale.quantity * sale.price

        total_quantity = sales.aggregate(
            total=Sum('quantity')
        )['total'] or 0

        best_product = (
            SalesData.objects
            .values('product_name')
            .annotate(total_qty=Sum('quantity'))
            .order_by('-total_qty')
            .first()
        )

        total_products = (
            SalesData.objects
            .values('product_name')
            .distinct()
            .count()
        )

        return Response({

            "total_revenue": total_revenue,

            "total_quantity": total_quantity,

            "best_selling_product":
                best_product['product_name']
                if best_product else None,

            "total_products": total_products

        })
class RevenueTrendView(APIView):

    def get(self, request):

        sales = SalesData.objects.all().order_by('sales_date')

        dates = []
        revenues = []

        for sale in sales:

            dates.append(str(sale.sales_date))

            revenues.append(
                sale.quantity * sale.price
            )

        return Response({
            "dates": dates,
            "revenues": revenues
        })    
class ForecastView(APIView):

    def get(self, request):

        data = SalesData.objects.all().values(
            'sales_date',
            'revenue'
        )

        df = pd.DataFrame(data)

        if len(df) < 5:
            return Response({
                "error": "Need at least 5 records"
            })

        df.columns = ['ds', 'y']

        model = Prophet()

        model.fit(df)

        future = model.make_future_dataframe(
            periods=30
        )

        forecast = model.predict(future)

        result = forecast[
            ['ds', 'yhat']
        ].tail(30)

        return Response(
            result.to_dict(
                orient='records'
            )
        )
class XGBoostForecastView(APIView):

    def get(self, request):

        data = SalesData.objects.all().values(
            'sales_date',
            'revenue'
        )

        df = pd.DataFrame(data)

        if len(df) < 10:
            return Response({
                "error": "Need at least 10 records"
            })

        df = df.sort_values(
            by='sales_date'
        )

        df['day'] = np.arange(len(df))

        X = df[['day']]
        y = df['revenue']

        model = XGBRegressor(
            n_estimators=100,
            learning_rate=0.1
        )

        model.fit(X, y)

        future_days = np.arange(
            len(df),
            len(df) + 30
        ).reshape(-1, 1)

        predictions = model.predict(
            future_days
        )

        results = []

        for i, pred in enumerate(predictions):

            results.append({
                "future_day": int(i + 1),
                "predicted_revenue": float(pred)
            })

        return Response(results)
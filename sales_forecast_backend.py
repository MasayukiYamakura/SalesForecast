import pandas as pd
import numpy as np
from django.shortcuts import render
from .forms import UploadFileForm
from statsmodels.tsa.arima.model import ARIMA

def forecast_sales(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        data = pd.read_csv(request.FILES['csv_file'])
        sales_data = process_sales_data(data)
        forecast = apply_arima_model(sales_data)
        return render(request, 'forecast_result.html', {'forecast': forecast})
    return render(request, 'upload.html')

def process_sales_data(data):
    data['売上年月日'] = pd.to_datetime(data['売上年月日'], format='%Y/%m')
    monthly_sales = data.groupby('売上年月日')['対象月の売上金額'].sum()
    return monthly_sales

def apply_arima_model(sales_data):
    model = ARIMA(sales_data, order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=12)  # 12ヶ月先の予測
    return forecast

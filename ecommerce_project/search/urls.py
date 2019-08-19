from django.urls import path
from .views import (
    SearchProductsView, )

app_name = 'search'
urlpatterns = [
    path('', SearchProductsView.as_view(), name='query'),
]

from django.urls import path
from .views import (SellerListView, CategoryListView, ProductListView,
                    ProductDetailView, ProductDetailSlugView)

app_name = 'pdt_catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path(
        'product/<slug:slug>-<int:pk>/',
        ProductDetailSlugView.as_view(),
        name='product'),
]

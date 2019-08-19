from django.shortcuts import render
from django.views.generic.list import ListView

from pdt_catalog.models import Product


class SearchProductsView(ListView):
    # queryset = Product.objects.all()
    template_name = 'pdt_catalog/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(f'context esoka {context}')
        query = self.request.GET.get('q')
        context['query'] = query
        # print(f'The {context}')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        # print(f'The gEt parameters {request.GET}')
        query = request.GET.get('q')
        # print(f'The query parameters {query}')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.none()

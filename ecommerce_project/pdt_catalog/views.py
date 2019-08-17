from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, render, redirect

from .models import Product, Seller, Category


class SellerListView(ListView):  # Class based views
    queryset = Seller.objects.all(
    )  # template name guide <app_name>/<modelname>_list.hmrl # NOTE
    template_name = 'pdt_catalog/seller.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SellerListView, self).get_context_data(*args, **kwargs)
        print(f'issa context: {context}')
        return context


def seller_list_view(request):
    queryset = Seller.objects.all()
    context = {'qs': queryset}
    return render(request, 'pdt_catalog/seller.html', context)


class CategoryListView(ListView):
    queryset = Category.objects.all()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'pdt_catalog/product_list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    # NOTE: Clean up
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context


# class ProductListSlugView(ListView):
#     queryset = Product.objects.all()
#     template_name = 'pdt_catalog/product_list.html'


def product_list_view(request):
    queryset = Product.objects.all()
    print(f'the query data: {queryset}')
    context = {'sample': queryset}
    print(f'the context data: {context}')
    return render(request, 'pdt_catalog/product_list.html', context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'pdt_catalog/product_detail.html'

    # NOTE: Clean up
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(
    #         *args, **kwargs)
    #     return context

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        print(f'Get by Id instance: {instance}')
        print(f'Issa absolute url {instance.get_absolute_url()}')
        if instance is None:
            raise Http404("The product doesn't exist")
        return instance


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'pdt_catalog/product_detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        print(f"THis {pk}")
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("The product doesn't exist")
        print(f'URL yeyo {instance.get_absolute_url()}')
        print(f'name: {instance.name}, description: {instance.description}')
        return instance


def product_detail_view(request, pk=None, *args, **kwargs):
    # NOTE: Clean up
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     print(f'Product id: {pk}')
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("Printing The product doesn't exist")
    #     raise Http404("The product doesn't exist")

    # OR
    # qs = Product.objects.filter(id=pk)
    # if qs.exists and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("The product doesn't exist")

    instance = Product.objects.get_by_id(pk)
    print(f'Get by Id instance: {instance}')
    if instance is None:
        raise Http404("The product doesn't exist")

    context = {'object': instance}
    return render(request, 'pdt_catalog/product_detail.html', context)

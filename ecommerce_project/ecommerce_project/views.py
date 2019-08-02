from django.http import HttpResponse
from django.shortcuts import render


def landing(request):
    return render(request, 'ecommerce_project/landing.html', {})

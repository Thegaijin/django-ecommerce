from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('pdt_catalog/', include('pdt_catalog.urls')),
    path('search/', include('search.urls')),
]

urlpatterns += staticfiles_urlpatterns()

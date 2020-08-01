from django.urls import include, path

from . import views

urlpatterns = [
    path('core/', include('core.urls')),
    path('', views.promo, name='index'),

]

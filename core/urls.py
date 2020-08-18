from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.promo, name='promo'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.post_detail, name='post_detail'),
    path('services/lawns', views.lawns,  name='lawns'),



]

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.promo, name='promo'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews')

]

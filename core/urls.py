from django.urls import path

from . import views

urlpatterns = [
    path('', views.promo, name='promo'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
    path('services/lawns/', views.lawns, name='lawns'),
    path('services/garden-design/', views.garden_design, name='garden-design'),
    path('services/auto-watering/', views.auto_watering, name='auto_watering'),
    path('services/trimming/', views.trimming, name='trimming'),
    path('work_system/', views.work_system, name='work_system'),

]

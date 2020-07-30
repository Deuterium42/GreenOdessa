from . import views

urlpatterns = [
    path('core/', include('core.urls')),
    path('', views.index, name='index'),

]

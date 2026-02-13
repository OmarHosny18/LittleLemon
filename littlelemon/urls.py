

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurant import views


router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
    
    
]

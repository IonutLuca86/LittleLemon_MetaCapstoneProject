from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path('restaurant/menu/', views.MenuItemList.as_view(), name='menu'),
    path('restaurant/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-detail'),   
    path('restaurant/booking/', include(router.urls)),
]
from django.urls import path
from .views import HomeView,ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/<pk>/', ProductDetailView.as_view(), name="product_detail"),
]

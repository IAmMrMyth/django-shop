from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Product
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product-detail.html'
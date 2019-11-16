from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Product, Review

class IndexView(ListView):
    model = Product
    template_name = 'index.html'

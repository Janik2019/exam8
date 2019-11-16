from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product, Review

class IndexView(ListView):
    model = Product
    template_name = 'index.html'

class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'desctiption', 'photo')
    success_url = reverse_lazy('webapp:index')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ('name', 'category', 'desctiption', 'photo')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product/delete.html'
    success_url = reverse_lazy('webapp:index')
    model = Product
    context_object_name = 'product'
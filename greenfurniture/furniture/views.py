from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Furniture, Category


class HomeView(ListView):
    template_name = 'furniture/home.html'
    model = Furniture
    context_object_name = 'furniture'
    extra_context = {'home': True}
    paginate_by = 8


class CategoryView(ListView):
    template_name = 'furniture/category.html'
    model = Furniture
    context_object_name = 'furniture'
    extra_context = {'catalog': True}
    paginate_by = 8

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Furniture.objects.filter(type__category=category)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = get_object_or_404(Category, pk=self.kwargs['pk'])
        return context


class FurnitureDetailView(DetailView):
    template_name = 'furniture/furniture_detail.html'
    model = Furniture
    context_object_name = 'furniture'


class CompanyInfoView(TemplateView):
    template_name = 'furniture/company_info.html'
    extra_context = {'company_info': True}


class TableTopInfoView(TemplateView):
    template_name = 'furniture/table_top_info.html'
    extra_context = {'table_top_info': True}

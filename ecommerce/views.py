from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_cars"] = Car.objects.all().order_by('-id') 
        context["project"] = ProjectInfo.objects.latest('id')
        context['all_parts']= CarParts.objects.all()
        context['all_accs']= Accessories.objects.all()
        return context

class AllCarsPageView(TemplateView):
    template_name = 'all_cars.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_cars"] = Car.objects.all().order_by('-id') 
        return context


class OneCarDetail(TemplateView):
    template_name = 'one_car.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["one_car"] = Car.objects.get(id=kwargs['pk'])
        return context


    
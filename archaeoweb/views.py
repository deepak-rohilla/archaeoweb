from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView


# Create your views here.



class HomePageView(TemplateView):
    template_name = 'base.html'
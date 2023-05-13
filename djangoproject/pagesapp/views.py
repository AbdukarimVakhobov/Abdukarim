from django.shortcuts import render
from  django.views.generic import TemplateView

# Create your views here.

class HomapageView(TemplateView):
    template_name = 'home.html'

class AboutpageView(TemplateView):
    template_name = 'about.html'

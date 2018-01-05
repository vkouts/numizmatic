from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from mycoin.models import MyCoin


class MainView(TemplateView):
    template_name = 'main.html'


class MyCoinsView(ListView):
    template_name = "my_coins.html"
    model = MyCoin


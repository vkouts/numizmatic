from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from mycoin.models import MyCoin


class MainView(TemplateView):
    template_name = 'main.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class MyCoinsView(ListView):
    template_name = "my_coins.html"
    model = MyCoin


class MyCoinDetailView(DetailView):
    template_name = "detail.html"
    model = MyCoin


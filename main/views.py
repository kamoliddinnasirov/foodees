from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, View
from main.models import Menu, Home


class Home(TemplateView):
    model = Home
    template_name = 'main/home.html'





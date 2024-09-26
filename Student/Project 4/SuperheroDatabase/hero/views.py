from pathlib import Path
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero
# Create your views here.

class HeroesView(TemplateView):
    template_name = 'heroes.html'

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'superhero': Superhero.objects.get(name=kwargs['name'])
        }
# Create your views here.

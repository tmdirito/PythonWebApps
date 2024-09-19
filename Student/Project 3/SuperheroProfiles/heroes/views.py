from pathlib import Path
from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HeroView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.kwargs.get('name')

        superheroes = {
            'spiderman': {
                'title': "Spider Man",
                'id': 'Peter Parker',
                'image': 'static/images/spiderman.jpg',
                'strength1': 'Web slinging',
                'strength2': 'Super strength',
                'strength3': 'Spidey sense',
                'weakness1': 'Self doubting',
                'weakness2': 'Will not kill'
            },
            'ironman': {
                'title': 'Iron Man',
                'id': 'Tony Stark',
                'image': 'static/images/ironman.jpg',
                'strength1': 'Genius',
                'strength2': 'Rich',
                'strength3': 'Iron man suit',
                'weakness1': 'Arrogant',
                'weakness2': 'No real superpower'
            },
            'thor': {
                'title': 'Thor',
                'id': 'Thor Odinson',
                'image': 'static/images/thor.jpg',
                'strength1': 'God of Thunder',
                'strength2': 'Mjolnir',
                'strength3': 'Super strength',
                'weakness1': 'Arrogant',
                'weakness2': 'Weaker without hammer'
            },
            'blackpanther': {
                'title': 'Black Panther',
                'id': 'T"Challa',
                'image': 'static/images/blackpanther.jpg',
                'strength1': 'Vibranium',
                'strength2': 'Heart shaped black panther herb',
                'strength3': 'Superhuman senses, reflexes, and strength',
                'weakness1': 'Not protected without vibranium',
                'weakness2': 'Human folly'
            },
            'doctorstrange': {
                'title': 'Doctor Strange',
                'id': 'Stephen Strange',
                'image': 'static/images/doctorstrange.jpg',
                'strength1': 'Spells',
                'strength2': 'Astral projection',
                'strength3': 'Sorcerer Supreme',
                'weakness1': 'Human weakness',
                'weakness2': 'Needs hands and tools for spellcasting'
            }
        }

        hero_data = superheroes.get(name)
        if hero_data:
            context['superhero'] = hero_data
            context['title'] = hero_data['title']
            context['id'] = hero_data['id']
            context['strength1'] = hero_data['strength1']
            context['strength2'] = hero_data['strength2']
            context['strength3'] = hero_data['strength3']
            context['weakness1'] = hero_data['weakness1']
            context['weakness2'] = hero_data['weakness2']
            context['image'] = hero_data['image']
        return context



class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        photos = Path('static/images').iterdir()
        photos = [f for f in photos]
        return dict(photos=photos)
        
    
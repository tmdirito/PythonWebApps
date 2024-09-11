from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MainView(TemplateView):
    template_name = 'heroes.html'

class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Spider-Man',
            'id': 'Peter Parker',
            'image': 'static/static/images/spiderman.jpg',
            'strength1': 'Web slinging',
            'strength2': 'Super strength',
            'strength3': 'Spidey sense',
            'weakness1': 'Self doubting',
            'weakness2': 'Will not kill'
        }

class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'image': 'static/static/images/iron_man.jpg',
            'strength1': 'Genius',
            'strength2': 'Rich',
            'strength3': 'Iron man suit',
            'weakness1': 'Arrogant',
            'weakness2': 'No real superpower'
        }
class ThorView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Thor',
            'id': 'Thor Odinson',
            'image': 'static/static/images/thor.jpg',
            'strength1': 'God of Thunder',
            'strength2': 'Mjolnir',
            'strength3': 'Super strength',
            'weakness1': 'Arrogant',
            'weakness2': 'Weaker without hammer'
        }


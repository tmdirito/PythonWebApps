from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Superhero
from csv import reader, writer
from .workshop import tabs_data, card_data, cards_data, accordion_data

def read_table(path):
    with open(path) as f:
        return [row for row in reader(f)]
    
def write_table(path, table):
    with open(path, 'w', newline='') as f:
        writer(f).writerows(table)

def print_table(table):
    for row in table:
        print(row[0], row[1], row[2])

class TableView(TemplateView):
    template_name = 'csv.html'

    def get_context_data(self, **kwargs):
        path = 'numbers.csv'
        return {'table': read_table(path)}
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero

class TabsView(TemplateView):
    template_name = 'hero/tabs.html'

    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)

class AccordionView(TemplateView):
    template_name = 'accordion.html'

    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class HeroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

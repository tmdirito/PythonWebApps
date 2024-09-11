from django.urls import path
from hero.views import MainView, SpiderManView, IronManView, ThorView

urlpatterns = [
    path('',        MainView.as_view()),
    path('spiderman',        SpiderManView.as_view()),
    path('ironman', IronManView.as_view()),
    path('home', MainView.as_view()),
    path('thor', ThorView.as_view())
]
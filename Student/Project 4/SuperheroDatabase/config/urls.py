from django.contrib import admin
from django.urls import path
from hero.views import HeroesView, HeroView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HeroesView.as_view(),  name = 'main-view'),
    path('<str:name>', HeroView.as_view()),
]

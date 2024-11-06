from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, SignUpView, TabsView
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [

    # Hero
    path('',                TabsView.as_view(),    name='hero_list'),
    path('Home',            HeroListView.as_view()),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # Admin views for users
    path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]

from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, SignUpView, TabsView, CarouselView
from django.contrib import admin
from django.views.generic import RedirectView
from . import views

urlpatterns = [

    # Hero
    path('Tab View',                TabsView.as_view(), name='tab-view'   ),
    path('Carousel View', CarouselView.as_view(), name='carousel-view'       ),
    path('Home',            HeroListView.as_view(), name='hero_list'),
    path('',            HeroListView.as_view(), name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    path('messages/', views.message_list, name='message_list'),
    path('messages/create/', views.create_message, name='create_message'),
    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # Admin views for users
    path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]

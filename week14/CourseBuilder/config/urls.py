
from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path


urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # Book
    path('', include('course.urls')),

    # Document
    path('', include('doc.urls')),

]
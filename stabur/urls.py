"""stabur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from services import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('uslugi/', include('services.urls')),
    path('o-kompanii/', views.AboutView.as_view(), name='about'),
    path('proekty/', views.ProjectsView.as_view(), name='projects'),
    path('tehnika/', views.EquipmentView.as_view(), name='equipment'),
    path('kontakty/', views.ContactsView.as_view(), name='contacts'),
    path('politika-konfidencialnosti/', views.PrivacyView.as_view(), name='privacy'),
    path('tinymce/', include('tinymce.urls')),
    path('forms/', include('forms.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

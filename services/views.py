from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from forms import forms
from . import models


# class HomeView(View):
#     def get(self, request):
#         projects = models.Project.objects.all()[:6]
#         equipment = models.Equipment.objects.all()
#         services = models.Service.objects.all()
#         documents = models.Document.objects.all()
#         return render(request, 'services/home.html', {
#             'projects': projects,
#             'equipment': equipment,
#             'services': services,
#             'documents': documents,
#             'title': 'Главная страница'
#         })


class HomeView(ListView):
    model = models.Service
    template_name = 'services/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.all()[:6]
        context['equipment'] = models.Equipment.objects.all()
        context['services'] = models.Service.objects.all()
        context['documents'] = models.Document.objects.all()
        context['title'] = 'Главная страница'
        return context


class ServicesView(ListView):
    model = models.Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Услуги'
        return context


class ServicesDetailView(DetailView):
    model = models.Service


class AboutView(ListView):
    model = models.Document
    template_name = 'services/about.html'
    context_object_name = 'documents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О компании'
        return context


class ProjectsView(ListView):
    model = models.Project
    template_name = 'services/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проекты'
        return context


class EquipmentView(ListView):
    model = models.Equipment
    template_name = 'services/equipment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Техника'
        return context


class ContactsView(View):
    def get(self, request):
        form = forms.ContactForm()
        contacts = models.Contact.objects.first()
        return render(request, 'services/contacts.html', {
            'form': form,
            'contacts': contacts,
            'title': 'Контакты'
        })


class PrivacyView(View):
    def get(self, request):
        contacts = models.Contact.objects.first()
        return render(request, 'services/privacy.html', {
            'title': 'Политика конфиденциальности',
            'contacts': contacts,
        })

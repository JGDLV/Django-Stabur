from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import CreateView
from . import forms


class TestView(View):
    def get(self, request):
        test_form = forms.TestForm()
        return render(request, 'services/test.html', {'test_form': test_form, 'title': 'Тест'})


class TestFormCreate(CreateView):
    form_class = forms.TestForm
    success_url = '/'


class CallbackFormCreate(CreateView):
    form_class = forms.CallbackForm
    success_url = '/'


class ContactFormCreate(CreateView):
    form_class = forms.ContactForm
    success_url = '/'


class ServiceFormCreate(CreateView):
    form_class = forms.ServiceForm
    success_url = '/'


class EquipmentFormCreate(CreateView):
    form_class = forms.EquipmentForm
    success_url = '/'

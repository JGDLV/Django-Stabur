from django import forms
from . import models


class TestForm(forms.ModelForm):
    class Meta:
        model = models.TestFormModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': '+7 (___) ___-__-__'}),
            'comment': forms.Textarea(attrs={'class': 'order-form__textarea', 'placeholder': 'Тут вы можете указать индивидуальные особенность вашего объекта или задать вопросы'}),
        }


class CallbackForm(forms.ModelForm):
    class Meta:
        model = models.CallbackForm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': '+7 (___) ___-__-__'}),
            'comment': forms.Textarea(attrs={'class': 'order-form__textarea', 'placeholder': 'Тут вы можете указать индивидуальные особенность вашего объекта или задать вопросы'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactForm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': '+7 (___) ___-__-__'}),
            'comment': forms.Textarea(attrs={'class': 'order-form__textarea', 'placeholder': 'Напишите любой вопрос и мы вам перезвоним'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.ServiceForm
        fields = '__all__'
        widgets = {
            'service': forms.HiddenInput(),
            'address': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Напишите здесь адрес объекта'}),
            'name': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': '+7 (___) ___-__-__'}),
            'comment': forms.Textarea(attrs={'class': 'order-form__textarea', 'placeholder': 'Тут вы можете указать индивидуальные особенность вашего объекта или задать вопросы'}),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = models.EquipmentForm
        fields = '__all__'
        widgets = {
            'equipment': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': '+7 (___) ___-__-__'}),
            'address': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Напишите здесь адрес объекта'}),
            'date': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Укажите дату'}),
            'time': forms.TextInput(attrs={'class': 'order-form__input', 'placeholder': 'Укажите кол-во часов'}),
            'comment': forms.Textarea(attrs={'class': 'order-form__textarea', 'placeholder': 'Тут вы можете указать индивидуальные особенность вашего объекта или задать вопросы'}),
        }

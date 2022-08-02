from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='test_form'),
    path('test/send/', views.TestFormCreate.as_view(), name='test_form_send'),
    path('callback/send/', views.CallbackFormCreate.as_view(), name='callback_form_send'),
    path('contact/send/', views.ContactFormCreate.as_view(), name='contact_form_send'),
    path('service/send/', views.ServiceFormCreate.as_view(), name='service_form_send'),
    path('equipment/send/', views.EquipmentFormCreate.as_view(), name='equipment_form_send'),
]

from django import template
from .. import forms


register = template.Library()


@register.inclusion_tag('services/include/callback_form.html')
def get_callback_form():
    form = forms.CallbackForm
    return {'form': form}


@register.inclusion_tag('services/include/equipment_form.html')
def get_equipment_form():
    form = forms.EquipmentForm
    return {'form': form}


@register.inclusion_tag('services/include/order.html', takes_context=True)
def get_order(context):
    form = forms.ServiceForm
    return {'form': form, 'request': context['request'], 'services': context['services']}


@register.inclusion_tag('services/include/order.html', takes_context=True)
def get_order_service(context):
    form = forms.ServiceForm(initial={'service': context['service']})
    return {'form': form}

from django import template
from .. import models
import re


register = template.Library()


@register.inclusion_tag('services/include/social.html')
def get_social():
    contacts = models.Contact.objects.first()
    return {'contacts': contacts}


@register.inclusion_tag('services/include/phone.html')
def get_phone():
    data = models.Contact.objects.first()
    phone = data.phone
    phone_clear = re.sub('[^0-9]', '', phone)
    return {
        'phone': phone,
        'phone_clear': phone_clear
    }

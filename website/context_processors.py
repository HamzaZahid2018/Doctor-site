from django.utils.http import urlencode
from .data import CLINIC_INFO

def whatsapp_link(request):
    number = CLINIC_INFO.whatsapp_number
    message = 'Assalam-o-alaikum, I would like to book an appointment with Dr. Muhammad Hassan Tariq.'
    params = urlencode({'text': message})
    link = f'https://wa.me/{number}?{params}'
    return {'whatsapp_link': link, 'clinic_info': CLINIC_INFO}

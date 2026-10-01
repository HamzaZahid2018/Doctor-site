from urllib.parse import quote
from .data import CLINIC_INFO

def whatsapp_link(request):
    number = CLINIC_INFO.whatsapp_number
    message = 'Assalam-o-Alaikum, mujhe Dr. Muhammad Hassan Tariq se appointment chahiye'
    encoded_message = quote(message)
    link = f'https://wa.me/{number}?text={encoded_message}'
    return {'whatsapp_link': link, 'clinic_info': CLINIC_INFO}

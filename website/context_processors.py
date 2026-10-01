from urllib.parse import quote
from .models import ClinicInfo

def whatsapp_link(request):
    try:
        clinic = ClinicInfo.load()
        number = clinic.whatsapp_number
    except:
        number = '923398770001'

    message = 'Assalam-o-Alaikum, mujhe Dr. Muhammad Hassan Tariq se appointment chahiye'
    encoded_message = quote(message)
    link = f'https://wa.me/{number}?text={encoded_message}'
    return {'whatsapp_link': link, 'clinic_info': clinic if 'clinic' in locals() else None}

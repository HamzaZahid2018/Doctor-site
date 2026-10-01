QUALIFICATIONS = [
    {'degree_title': 'MBBS', 'institution': 'FMH, Lahore', 'country': 'Pakistan'},
    {'degree_title': 'Masters in Male Infertility', 'institution': 'UK', 'country': ''},
    {'degree_title': 'Fellow', 'institution': "Academy for Men's Health, Singapore", 'country': ''},
    {'degree_title': 'Certified', 'institution': 'South Asian Society for Sexual Medicine (SASSM)', 'country': ''},
    {'degree_title': 'American Diabetes Association Certified', 'institution': 'USA', 'country': ''},
]

class MockClinicInfo:
    def __init__(self):
        self.phone_number = '0339-8770001'
        self.whatsapp_number = '923398770001'
        self.city = 'Rahim Yar Khan'
        self.timings_weekdays = 'Monday to Sunday: 9:00 AM to 6:00 PM'
        self.timings_sunday = 'Open 7 days a week'
        self.address = 'Rahim Yar Khan, Punjab, Pakistan'

CLINIC_INFO = MockClinicInfo()

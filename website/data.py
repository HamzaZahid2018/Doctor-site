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
        self.timings_weekdays = 'Monday to Sunday: 10:00 AM to 11:00 PM'
        self.timings_sunday = 'Open 7 days a week'
        self.address = 'Rahim Yar Khan, Punjab, Pakistan'

CLINIC_INFO = MockClinicInfo()

class MockService:
    def __init__(self, title, slug, icon_name, short_description, full_description, category, category_display):
        self.title = title
        self.slug = slug
        self.icon_name = icon_name
        self.short_description = short_description
        self.full_description = full_description
        self.category = category
        self._category_display = category_display
        
    def get_category_display(self):
        return self._category_display

from django.utils.text import slugify

_MALE_HEALTH = [
    ('Varicocele', 'Checkup and treatment for varicocele affecting male fertility.', 'I provide proper checkups and medical treatment for varicocele, a condition where enlarged veins in the scrotum can lower sperm production and reduce fertility.'),
    ('Hydrocele', 'Diagnosis and treatment of hydrocele.', 'I offer careful checkups and correct treatment for hydrocele, a collection of fluid around the testicle that may cause discomfort and affect reproductive health.'),
    ('Azoospermia', 'Specialist care for azoospermia (absence of sperm).', 'I evaluate and manage azoospermia, the absence of measurable sperm in the semen, through advanced hormonal and structural tests to find the cause and recommend the right treatment.'),
    ('Low or Absent Sperm Count', 'Checkup and treatment for low or absent sperm count.', 'I provide personal semen tests and fertility checkups to find the cause of low or absent sperm count, and create a treatment plan to improve your chances of becoming a father.'),
    ('Male Hormonal Deficiency', 'Hormone tests and treatment for male hormonal problems.', 'I check your hormone levels in detail and provide proper medical treatment for male hormonal problems that can lower your energy, mood, sexual function, and fertility.'),
    ('Premature Ejaculation', 'Private, respectful care for premature ejaculation.', 'I offer private and respectful treatment for premature ejaculation, helping you regain confidence and improve your life.'),
    ('Delayed Puberty', 'Checkup and treatment of delayed puberty in boys.', 'I check and treat delayed puberty in boys by looking into hormonal and growth factors, and providing the right medical support.'),
    ('Male Weakness', 'Checkup for male weakness related to hormones or fertility.', 'I check male weakness, including fatigue, low sexual desire, and low stamina, that may be linked to hormonal problems or reproductive health.'),
    ('Obesity-related Fertility Issues', 'Fertility support for men affected by weight.', 'I help men understand how weight affects fertility, and I provide personal guidance and treatment to improve reproductive health.'),
]

_PEDS = [
    ('Fever', 'Expert checkup and treatment for children\'s fever.', 'I check and treat fever in children, making sure we find the real cause and give the right medicine.'),
    ('Cold, Flu & Cough', 'Medical care for children with cold, flu, and cough.', 'I provide careful and effective treatment for children with cold, flu, and cough, helping them recover quickly.'),
    ('Allergies', 'Diagnosis and treatment of childhood allergies.', 'I check and treat childhood allergies, helping parents understand the causes and giving the right medicine to reduce symptoms.'),
    ('Asthma', 'Specialist checkup and treatment for childhood asthma.', 'I check and manage childhood asthma, helping your child breathe easier and stay active.'),
    ('Nutritional Deficiency', 'Checkup and guidance for children with poor nutrition.', 'I check for nutritional problems in children and give personal diet advice and supplements to support healthy growth.'),
    ('Delayed Growth & Development', 'Checkup for delayed growth and development in children.', 'I check children with delayed growth or development, looking into hormones, nutrition, and other factors to start treatment early.'),
]

_DIABETES = [
    ('Diabetes Management', 'Proper, ADA-certified diabetes treatment.', 'I offer proper, ADA-certified diabetes care, creating a personal treatment plan to help you control blood sugar, prevent complications, and live a better life.'),
    ('Reduced Sexual Desire due to Diabetes', 'Specialist care for sexual health problems caused by diabetes.', 'I check and treat reduced sexual desire and performance issues caused by diabetes, looking at both hormones and blood flow.'),
    ('ADA-certified Diabetes Care', 'Proper, ADA-certified diabetes care.', 'I follow the latest American Diabetes Association guidelines, making sure you get the best, up-to-date treatment for your specific health needs.'),
    ('Hormonal Imbalance & Endocrine Support', 'Diagnosis and treatment of hormonal problems.', 'I diagnose and treat hormonal problems and endocrine disorders, giving you the right support to restore your hormone balance and improve your health.'),
]

SERVICES = []
for title, short, full in _MALE_HEALTH:
    SERVICES.append(MockService(title, slugify(title), 'fa-mars', short, full, 'male_health', 'Male Reproductive Health'))

for title, short, full in _PEDS:
    SERVICES.append(MockService(title, slugify(title), 'fa-child', short, full, 'pediatrics', 'Pediatric Care'))

for title, short, full in _DIABETES:
    SERVICES.append(MockService(title, slugify(title), 'fa-heartbeat', short, full, 'diabetes', 'Diabetes Care'))


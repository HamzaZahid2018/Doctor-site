from django.core.management.base import BaseCommand
from website.models import Service, Qualification, ClinicInfo
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed the database with initial data for the doctor site'

    def handle(self, *args, **kwargs):
        # Create or update ClinicInfo
        clinic, _ = ClinicInfo.objects.get_or_create(pk=1)
        clinic.phone_number = '0339-8770001'
        clinic.whatsapp_number = '923398770001'
        clinic.city = 'Rahim Yar Khan'
        clinic.timings_weekdays = 'Monday to Sunday: 9:00 AM to 6:00 PM'
        clinic.timings_sunday = 'Open 7 days a week'
        clinic.address = 'Rahim Yar Khan, Punjab, Pakistan'
        clinic.save()
        self.stdout.write(self.style.SUCCESS('Created/Updated ClinicInfo'))

        # Seed Qualifications - institution and country fields are separate; no duplication
        Qualification.objects.all().delete()
        qualifications = [
            {'degree_title': 'MBBS', 'institution': 'FMH, Lahore', 'country': 'Pakistan', 'order': 0},
            {'degree_title': 'Masters in Male Infertility', 'institution': 'UK', 'country': '', 'order': 1},
            {'degree_title': 'Fellow', 'institution': "Academy for Men's Health, Singapore", 'country': '', 'order': 2},
            {'degree_title': 'Certified', 'institution': 'South Asian Society for Sexual Medicine (SASSM)', 'country': '', 'order': 3},
            {'degree_title': 'American Diabetes Association Certified', 'institution': 'USA', 'country': '', 'order': 4},
        ]
        for q in qualifications:
            Qualification.objects.create(
                degree_title=q['degree_title'],
                institution=q['institution'],
                country=q['country'],
                order=q['order']
            )
        self.stdout.write(self.style.SUCCESS('Created Qualifications'))

        # Seed Services
        Service.objects.all().delete()

        male_health_services = [
            {
                'title': 'Varicocele',
                'short': 'Checkup and treatment for varicocele affecting male fertility.',
                'full': 'I provide proper checkups and medical treatment for varicocele, a condition where enlarged veins in the scrotum can lower sperm production and reduce fertility.',
            },
            {
                'title': 'Hydrocele',
                'short': 'Diagnosis and treatment of hydrocele.',
                'full': 'I offer careful checkups and correct treatment for hydrocele, a collection of fluid around the testicle that may cause discomfort and affect reproductive health.',
            },
            {
                'title': 'Azoospermia',
                'short': 'Specialist care for azoospermia (absence of sperm).',
                'full': 'I evaluate and manage azoospermia, the absence of measurable sperm in the semen, through advanced hormonal and structural tests to find the cause and recommend the right treatment.',
            },
            {
                'title': 'Low or Absent Sperm Count',
                'short': 'Checkup and treatment for low or absent sperm count.',
                'full': 'I provide personal semen tests and fertility checkups to find the cause of low or absent sperm count, and create a treatment plan to improve your chances of becoming a father.',
            },
            {
                'title': 'Male Hormonal Deficiency',
                'short': 'Hormone tests and treatment for male hormonal problems.',
                'full': 'I check your hormone levels in detail and provide proper medical treatment for male hormonal problems that can lower your energy, mood, sexual function, and fertility.',
            },
            {
                'title': 'Premature Ejaculation',
                'short': 'Private, respectful care for premature ejaculation.',
                'full': 'I offer private and respectful treatment for premature ejaculation, helping you regain confidence and improve your life.',
            },
            {
                'title': 'Delayed Puberty',
                'short': 'Checkup and treatment of delayed puberty in boys.',
                'full': 'I check and treat delayed puberty in boys by looking into hormonal and growth factors, and providing the right medical support.',
            },
            {
                'title': 'Male Weakness',
                'short': 'Checkup for male weakness related to hormones or fertility.',
                'full': 'I check male weakness, including fatigue, low sexual desire, and low stamina, that may be linked to hormonal problems or reproductive health.',
            },
            {
                'title': 'Obesity-related Fertility Issues',
                'short': 'Fertility support for men affected by weight.',
                'full': 'I help men understand how weight affects fertility, and I provide personal guidance and treatment to improve reproductive health.',
            },
        ]
        for idx, s in enumerate(male_health_services):
            Service.objects.create(
                title=s['title'],
                slug=slugify(s['title']),
                icon_name='fa-mars',
                short_description=s['short'],
                full_description=s['full'],
                category='male_health',
                order=idx
            )

        pediatrics_services = [
            {
                'title': 'Fever',
                'short': 'Expert checkup and treatment for children\'s fever.',
                'full': 'I check and treat fever in children, making sure we find the real cause and give the right medicine.',
            },
            {
                'title': 'Cold, Flu & Cough',
                'short': 'Medical care for children with cold, flu, and cough.',
                'full': 'I provide careful and effective treatment for children with cold, flu, and cough, helping them recover quickly.',
            },
            {
                'title': 'Allergies',
                'short': 'Diagnosis and treatment of childhood allergies.',
                'full': 'I check and treat childhood allergies, helping parents understand the causes and giving the right medicine to reduce symptoms.',
            },
            {
                'title': 'Asthma',
                'short': 'Specialist checkup and treatment for childhood asthma.',
                'full': 'I check and manage childhood asthma, helping your child breathe easier and stay active.',
            },
            {
                'title': 'Nutritional Deficiency',
                'short': 'Checkup and guidance for children with poor nutrition.',
                'full': 'I check for nutritional problems in children and give personal diet advice and supplements to support healthy growth.',
            },
            {
                'title': 'Delayed Growth & Development',
                'short': 'Checkup for delayed growth and development in children.',
                'full': 'I check children with delayed growth or development, looking into hormones, nutrition, and other factors to start treatment early.',
            },
        ]
        for idx, s in enumerate(pediatrics_services):
            Service.objects.create(
                title=s['title'],
                slug=slugify(s['title']),
                icon_name='fa-child',
                short_description=s['short'],
                full_description=s['full'],
                category='pediatrics',
                order=idx
            )

        diabetes_services = [
            {
                'title': 'Diabetes Management',
                'short': 'Proper, ADA-certified diabetes treatment.',
                'full': 'I offer proper, ADA-certified diabetes care, creating a personal treatment plan to help you control blood sugar, prevent complications, and live a better life.',
            },
            {
                'title': 'Reduced Sexual Desire due to Diabetes',
                'short': 'Specialist care for sexual health problems caused by diabetes.',
                'full': 'I check and treat reduced sexual desire and performance issues caused by diabetes, looking at both hormones and blood flow.',
            },
            {
                'title': 'ADA-certified Diabetes Care',
                'short': 'Proper, ADA-certified diabetes care.',
                'full': 'I follow the latest American Diabetes Association guidelines, making sure you get the best, up-to-date treatment for your specific health needs.',
            },
            {
                'title': 'Hormonal Imbalance & Endocrine Support',
                'short': 'Diagnosis and treatment of hormonal problems.',
                'full': 'I diagnose and treat hormonal problems and endocrine disorders, giving you the right support to restore your hormone balance and improve your health.',
            },
        ]
        for idx, s in enumerate(diabetes_services):
            Service.objects.create(
                title=s['title'],
                slug=slugify(s['title']),
                icon_name='fa-heartbeat',
                short_description=s['short'],
                full_description=s['full'],
                category='diabetes',
                order=idx
            )

        self.stdout.write(self.style.SUCCESS('Created Services'))
        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully.'))

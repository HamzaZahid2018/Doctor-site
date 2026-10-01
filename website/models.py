from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = (
        ('male_health', 'Male Reproductive Health'),
        ('pediatrics', 'Pediatrics'),
        ('diabetes', 'Diabetes'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    icon_name = models.CharField(max_length=50)
    short_description = models.TextField()
    full_description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Qualification(models.Model):
    degree_title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'degree_title']

    def __str__(self):
        return f"{self.degree_title} - {self.institution}"

class ClinicInfo(models.Model):
    phone_number = models.CharField(max_length=50, default='0339-8770001')
    whatsapp_number = models.CharField(max_length=50, default='923398770001')
    city = models.CharField(max_length=100, default='Rahim Yar Khan')
    timings_weekdays = models.CharField(max_length=200, default='Mon–Sat 9:00 AM – 6:00 PM')
    timings_sunday = models.CharField(max_length=200, default='Sunday Closed')
    address = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(ClinicInfo, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Clinic Information"

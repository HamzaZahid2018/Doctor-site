from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['website:home', 'website:about']

    def location(self, item):
        return reverse(item)

class ServiceSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Service.objects.all()

    def location(self, item):
        return reverse('website:service_detail', args=[item.slug])

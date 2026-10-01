from django.shortcuts import render
from django.http import Http404
from .data import QUALIFICATIONS, SERVICES

def home(request):
    return render(request, 'website/home.html')

def service_detail(request, slug):
    service = next((s for s in SERVICES if s.slug == slug), None)
    if not service:
        raise Http404("Service not found")
    return render(request, 'website/service_detail.html', {
        'service': service,
    })

def about(request):
    return render(request, 'website/about.html', {
        'qualifications': QUALIFICATIONS,
    })

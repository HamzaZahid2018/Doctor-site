from django.shortcuts import render, get_object_or_404
from .models import Service, Qualification

def home(request):
    return render(request, 'website/home.html')

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'website/service_detail.html', {
        'service': service,
    })

def about(request):
    qualifications = Qualification.objects.all()
    return render(request, 'website/about.html', {
        'qualifications': qualifications,
    })

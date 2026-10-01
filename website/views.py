from django.shortcuts import render
from .data import QUALIFICATIONS

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html', {
        'qualifications': QUALIFICATIONS,
    })

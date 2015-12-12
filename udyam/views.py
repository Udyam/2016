from django.shortcuts import render, render_to_response, HttpResponse
from django.utils import timezone

# Create your views here.


def index(request):
    if request.method == 'POST':
        pass
    return render(request, 'home.html')


def events(request, name):
    pass

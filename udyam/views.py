from django.shortcuts import render, render_to_response, HttpResponse
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, 'home.html')

def register(request, name):
    if request.method == 'POST':
        pass
        # request.POST = request.POST.copy()
        # request.POST['event_name'] = name
        # TODO return success page
        # TODO check for the repeated email entry
    return render(request, 'register.html', {'event':event})

def events(request, name):
    pass

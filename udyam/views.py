from django.shortcuts import render, render_to_response, HttpResponse
import json
from models import RegistrationInfo

# Create your views here.


def index(request):
    if request.method == 'POST':
        form_detail = json.loads(request.body)
        print form_detail
    return render(request, 'home.html')


def events(request, name):
    pass

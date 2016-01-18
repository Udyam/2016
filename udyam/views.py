from django.shortcuts import render, render_to_response, HttpResponse
from models import RegistrationInfo
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        form_detail = request.body
    return render(request, 'home.html')


def static_page(request, page):
    page += '.html'
    return render(request, page)

from django.shortcuts import render
from forms import RegistrationForm
from models import Events
from django.utils import timezone

# Create your views here.


def check_mail(data):
    pass

def index(request):
    pass


def register(request, name):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.isvalid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            # TODO return success page
            # TODO check for the repeated email entry
    form = RegistrationForm()
    event = Events.objects.get(name=name)
    render(request, 'register.html', {'form':form})


def events(request, name):
    pass

from django.shortcuts import render, HttpResponse
from forms import RegistrationForm
from models import Events
from django.utils import timezone

# Create your views here.


def index(request):
    pass


def register(request, name):
    if request.method == 'POST':
        # request.POST = request.POST.copy()
        # request.POST['event_name'] = name
        form = RegistrationForm(request.POST)
        print form
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            # TODO return success page
            # TODO check for the repeated email entry
        else:
            return HttpResponse()
    form = RegistrationForm()
    event = Events.objects.get(name=name)
    return render(request, 'register.html', {'form':form, 'event':event})


def events(request, name):
    pass

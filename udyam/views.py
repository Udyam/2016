from django.shortcuts import render
from models import RegistrationInfo
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    if request.is_ajax():
        try:
            form_detail = json.loads(request.body)
            team = RegistrationInfo()
            team.event_name = form_detail[u'event']
            team.contact = json.dumps(form_detail[u'main_contact'])
            team.team_name = form_detail[u'team_name']
            team.team_details = form_detail[u'team_details']
            team.save()
        except:
            pass
    return render(request, 'home.html')


def static_page(request, page):
    page += '.html'
    return render(request, page)

from django.shortcuts import render, HttpResponse
from models import RegistrationInfo
from django.views.decorators.csrf import csrf_exempt
import json
from send_mail import SendMail

@csrf_exempt
def index(request):
    if request.method == 'POST':
        error = 0
        try:
            form_detail = json.loads(request.body)
            team = RegistrationInfo()
            team.event_name = form_detail[u'event']
            team.contact = json.dumps(form_detail[u'main_contact'])
            team.team_name = form_detail[u'team_name']
            team.team_details = form_detail[u'team_details']
            team.save()
            mail = SendMail(form_detail)
            mail.mail_coordinator()
            mail.mail_representative()
        except:
            error = 1
        return HttpResponse(json.dumps({'error': error}), content_type='application/json')
    return render(request, 'home.html')


def static_page(request, page):
    page += '.html'
    return render(request, page)

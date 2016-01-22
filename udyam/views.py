from django.shortcuts import render, HttpResponse
from models import RegistrationInfo
from django.views.decorators.csrf import csrf_exempt
import json
from send_mail import SendMail
import thread

@csrf_exempt
def index(request):
    msg = False
    error = False
    if request.method == 'POST':
        msg = True
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
            # thread.start_new_thread(mail.mail_coordinator, ())
            # thread.start_new_thread(mail.mail_representative, ())
        except:
            error = True
    return render(request, 'home.html', {'msg': msg, 'error': error})


def static_page(request, page):
    page += '.html'
    return render(request, page)

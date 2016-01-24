import sendgrid
from mail_data import *
import os


class SendMail:
    def __init__(self, json_data):
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        with open(os.path.join(BASE_DIR, 'api.key'), 'r') as files:
            self.APIKEY = files.readline()
        self.data = json_data

    def mail_representative(self):
        sg_client = sendgrid.SendGridClient(self.APIKEY)
        _subject = "Registered successfully for " + events_data[self.data[u'event']][0] + " in UDYAM-2016"
        _body = html_head + participant_mail_body.format(self.data[u'event']) + html_footer
        message = sendgrid.Mail()
        message.add_to(self.data[u'main_contact'][u'email'])
        message.set_subject(_subject)
        message.set_html(_body)
        message.set_from('Team UDYAM<no-reply@udyam.com>')
        sg_client.send(message)


    def mail_coordinator(self):
        sg_client = sendgrid.SendGridClient(self.APIKEY)
        _subject = "A team registered in " + events_data[self.data[u'event']][0] + " event"
        _body = html_head + coordinator_mail_body.format(self.data[u'event'], self.data[u'team_name'])
        for member in self.data[u'team_details']:
            if member:
                _body += "<br>" + member[u'name'] + "   " + member[u'contact'] + "   " + member[u'email']
            else:
                break
        _body += html_footer
        message = sendgrid.Mail()
        message.add_to(events_data[self.data[u'event']][1])
        message.set_subject(_subject)
        message.set_html(_body)
        message.add_cc('udyam@itbhu.ac.in')
        message.set_from('Team UDYAM<no-reply@udyam.com>')
        sg_client.send(message)

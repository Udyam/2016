from django import forms


class RegistrationForm(forms.ModelForm):
    # TODO registration form must have minimum number of entry as per event
    # TODO and to send null for others
    # TODO check the same email is not used in team members
    # TODO a hidden entry in template equals to the event name sent
    pass

from django.contrib import admin

from models import RegistrationInfo

# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    model = RegistrationInfo
    list_filter = ['event_name']

admin.site.register(RegistrationInfo,RegisterAdmin)

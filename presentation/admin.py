from django.contrib import admin
from .models import Mesaj

# Register your models here.
class Mesajadmin(admin.ModelAdmin):
    list_display = ('Fullname', 'EmailAddress', 'PhoneNumber', 'Message')

admin.site.register(Mesaj, Mesajadmin)

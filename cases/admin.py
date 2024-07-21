from django.contrib import admin
from .models import Client, Lawyer, Case
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Client._meta.fields if f.name != 'description']

class LawyerAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Lawyer._meta.fields if f.name != 'description']

class CaseAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Case._meta.fields if f.name != 'description']

admin.site.register(Client, ClientAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Lawyer, LawyerAdmin)
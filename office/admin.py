from django.contrib import admin
from office.models import Protocol


class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('slug', 'contractor')


admin.site.register(Protocol, ProtocolAdmin)
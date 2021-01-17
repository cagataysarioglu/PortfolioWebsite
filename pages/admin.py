from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('namesurname', 'email', 'subject', 'created',)
    list_filter = ('namesurname', 'created',)
    search_fields = ('namesurname', 'subject',)
    list_per_page = 20


admin.site.site_header = 'Tan Ticaret Yönetici Paneli'
admin.site.register(Contact, ContactAdmin)

from django.contrib import admin
from .models import Contact, Carousel

class ContactAdmin(admin.ModelAdmin):
    list_display = ('namesurname', 'email', 'subject', 'created',)
    list_filter = ('namesurname', 'created',)
    search_fields = ('namesurname', 'subject',)
    list_per_page = 20

admin.site.site_header = 'Tan Ticaret Yönetici Paneli'
admin.site.register(Contact, ContactAdmin)

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo',)
    list_display_links = ('name', 'photo',)
    list_filter = ('name', 'photo',)
    search_fields = ('name', 'photo',)
    list_per_page = 7

admin.site.register(Carousel, CarouselAdmin)

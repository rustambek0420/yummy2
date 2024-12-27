from django.contrib import admin
from .models import *



admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Proffesionalchef)
admin.site.register(Staywithus)
admin.site.register(Ourgallery)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Reservation)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  
    list_filter = ('created_at',)  
    search_fields = ('name', 'email', 'subject')



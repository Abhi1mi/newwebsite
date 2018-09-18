from django.contrib import admin
from .models import Subscriber, Profile

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic','created')
    search_fields = ('user','profile_pic')
    ordering = ('created',)
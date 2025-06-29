from django.contrib import admin
#registring the models in admin files
from.models import Room, Message

# Register your models here.

#below will shown in django admin 
admin.site.register(Room)
admin.site.register(Message)

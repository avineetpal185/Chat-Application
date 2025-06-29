from django.db import models
from datetime import datetime # to add the date and time

# Create 2 models one for Room and second for Message
#Djan go id automaticcaly created one object create

class Room(models.Model):
    name = models.CharField(max_length=1000)


#below is model going to store the data in the database
#value come from  views.py->send function ->store in admin 
class Message(models.Model):
    #value is the message we sent it hi,hlo etc
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    #user >avi1 or avi2 
    user = models.CharField(max_length=1000000)
    #room tells in which room want to send the message
    room = models.CharField(max_length=1000000)

    #reister this model in admin file

    #migrations->migrate->super user
from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    #it goes for home.html
    return render(request, 'home.html')
# collecitng the room(string) coming from url.py

def room(request, room):
    username = request.GET.get('username') #getting usernmae coming in url(get metod)
    #below from(Room) model gettign the particar model which have name of this room
    room_details = Room.objects.get(name=room) #storing the partic;ar room(url)
    #passing the username and then room(function pass) and room_details in html 
   
    return render(request, 'room.html',{
        'username' : username,
        'room' : room,
        'room_details' : room_details
        #after this pass to room.html->by help of this data in values,input type
    }) 

#import the model from Chat
def checkview(request):
    #the room name when user fill or send it will come in the room and checking that it is exists or not 
    
    room = request.POST['room_name'] #roomname in Html 
    username = request.POST['username']
    #checking room in models (user enter dtore in (room) compare with name(in model))
    if Room.objects.filter(name=room).exists():
        #it exists redirect it(moving 1 location to other)
        #movine user to that user (with room (matched) and passing the username also)
        return redirect('/'+room+'/?username='+username)
    
    else:
        #if it is not exists we create it 
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
#data come from room.html(Ajax passing url->urls.py->now here !)
def send(request):
      #now getting the data passing from Ajax
    message = request.POST['message'] #message is variable create in Ajax
    username = request.POST['username']
    room_id = request.POST['room_id']
#now storing the above weel we fetched into the Message model in models.py 
    new_message = Message.objects.create(value = message, user = username, room=room_id)
    new_message.save()
    #returning back this message in to the front end and in the javascript
    return HttpResponse('Message sent succesfully')

#we use here JSON respone so import it
def getMessages(request, room):

   # now to get all the messages of different rooms
    room_details = Room.objects.get(name=room) #getting room name 
    messages = Message.objects.filter(room = room_details.id)

    #reutnring JSON response
    return JsonResponse({"messages": list(messages.values())})
    #message have the room_detail.id and the values (store the message hi,hlo etc)
    #->room.html



#Ajax display the messages on scree without reloading the url (goof fetaure)



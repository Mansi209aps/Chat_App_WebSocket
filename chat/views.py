from django.shortcuts import render, redirect
from .models import Room, Message
# Create your views here.

def HomeView(request):
    if request.method == "POST":
        username = request.POST["username"]
        room = request.POST["room"]

        # Create a new room object with the given username and room name if the room with given room name doesn't exist
        try:
            existing_room = Room.objects.get(room_name__icontains=room) # __icontains : to treat upper case and lower case same in the room name
        except Room.DoesNotExist:
            r = Room.objects.create(room_name=room)
        return redirect("room", room_name=room,username=username) # Once the room has been created redirect to room page and pass room name and username in the url
    return render(request, "home.html")

def RoomView(request, room_name, username):
    existing_room = Room.objects.get(room_name__icontains=room_name)
    get_messages = Message.objects.filter(room=existing_room)
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": existing_room.room_name
    }
    return render(request, "room.html", context)
from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, "home.html")

def RoomView(request, room_name, username):
    return render(request, "room.html")
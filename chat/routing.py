from django.urls import path
from .consumers import ChatConsumer

wsPattern = [path("wss/messages/<str:room_name>/", ChatConsumer.as_asgi())] # WebSocket pattern

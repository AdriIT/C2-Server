#routing.py

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/devices/(?P<device_id>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
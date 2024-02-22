#consumers.py
import json
import subprocess

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    
                
    async def connect(self):
        # Esegui le operazioni necessarie quando una connessione WebSocket viene stabilita
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.room_group_name = f"chat_{self.device_id}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Join room group

        await self.accept()
        
        #print(subprocess.getoutput('ps'))

        #await heartbeat() #funzione utile a controllare se il server è presente nella chatroom

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        
        sender = text_data_json.get('sender', '')
        message = sender + ' ' + text_data_json['message']
        print(message)
        
         # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "sender": sender}
        )
        
        # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        
        
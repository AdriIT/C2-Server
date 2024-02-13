#consumers.py
import json
import subprocess

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    
                
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        # Esegui le operazioni necessarie quando una connessione WebSocket viene stabilita
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': f'You are now connected to device {self.device_id}'
        }))
        #print(subprocess.getoutput('ps'))

        #await heartbeat() #funzione utile a controllare se il server è presente nella chatroom

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        #if message == "ciao":
        #    await self.send(text_data=json.dumps({
        #    'message': f'{self.device_id} ciao'
        #    }))
        #    print("prova")
        #



        await self.send(text_data=json.dumps({
            'message': f'{self.device_id}: {message}'
            }))




        
        
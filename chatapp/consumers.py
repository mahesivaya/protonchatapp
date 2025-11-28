import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("User in connect():", self.scope["user"])
        print("Authenticated:", self.scope["user"].is_authenticated)
        await self.accept()
        print(f'WebSocket connected: {self.channel_name}')

    async def disconnect(self, close_code):
        print(f'WebSocket disconnected: {self.channel_name}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Echo message back to client
        username = self.scope['user'].username
        await self.send(text_data=json.dumps({
            'message': f"{username}: {message}",
            'sender': username
        }))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(f'WebSocket connected: {self.channel_name}')

    async def disconnect(self, close_code):
        print(f'WebSocket disconnected: {self.channel_name}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Echo message back to client
        await self.send(text_data=json.dumps({
            'message': f'Echo: {message}',
            'sender': 'system'
        }))

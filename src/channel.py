import requests
import response
import os
import build
import json

class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id: str,) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.server().channel().list(id=channel_id, part='snippet, statistics').execute()
        self.api_key = os.getenv('API_KEY')
        self.youtube = build('youtube', 'v3', developer=self.api_key)
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'http://www.youtube.com/channel/'+self.channel['items'][0]['id']
        self.subscribers_count = self.channel['items'][0]['statistics']['subscribersCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count= self.channel['items'][0]['statistics']['viewCount']


    def print_info(self) -> str:
        """Выводит в консоль информацию о канале."""
        print(f'{self.channel_id}, {self.channel}, {self.title}, {self.url}, {self.video_count}')

    def server(self):
        pass

    def get_service(self, request):
            self.request = response.request

    def to_json(value: str):

        return getattr(value, Channel)


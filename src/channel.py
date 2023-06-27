import build
from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # self.service = build('youtube', 'v3', developerKey='API_KEY')
        # self.channel = self.service().channels().list(id=channel_id, part='snippet, statistics').execute()
        self.channel_id = channel_id
        # self.api_key = os.getenv('API_KEY')
        # self.title = self.channel["items"][0]['snippet']['title']
        # self.description = self.channel['items'][0]['snippet']['description']
        # self.url = 'http://www.youtube.com/channel/' + self.channel['items'][0]['id']
        # self.subscribers_count = self.channel['items'][0]['statistics']['subscribersCount']
        # self.video_count = self.channel['items'][0]['statistics']['videoCount']
        # self.view_count = self.channel['items'][0]['statistics']['viewCount']

        # def print_info(self):
        """Выводит в консоль информацию о канале."""
        # print(f'{self.channel_id}, {self.channel}, {self.title}, {self.url}, {self.video_count}')

    def server(self):
        pass

    def get_service(self):
        service = build('youtube', 'v3', developerKey='API_KEY')
        return service

    def print_info(self, channel_id):

        r = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()

        print(r['items'][0]['snippet']['title'])
        print(r['items'][0]['snippet']['publishedAt'])
        print(r['items'][0]['statistics']['viewCount'])


    # def to_json(value: str):
    # return getattr(value, Channel)

    # def channel(self) -> None:
    # pass

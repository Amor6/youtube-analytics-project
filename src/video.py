from helper.youtube_api_manual import video_id, video_response, youtube, playlist_videos
import build
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_response, video_title, view_count, like_count):
        self.video_response = youtube().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                      id=video_id
                                                      ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']


class PLVideo(Video):
    def __init__(self, video_ids):
        super().__init__(video_response)
        self.video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

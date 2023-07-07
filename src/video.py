class Video:
    def __init__(self, video_id):
        self.video = self.service().video.list(id=video_id, part='snippet, statistics').execute()
        self.video_id = video_id
        self.title_video = self.video["items"][0]['snippet']['title']
        self.url_video = 'youtube.com/watch?v=' + self.video['items'][0]['id']
        self.vive_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']


class PLVideo:
    def __init__(self, video_id, title_video, url_video, vive_count, like_count, id_play_list):
        super().__init__(video_id, title_video, url_video, vive_count, like_count)
        self.id_play_list = id_play_list

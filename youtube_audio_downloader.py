from moviepy.editor import *
from pytube import *
import requests
import os

class YoutubeDownloader:
    def __init__(self, link: str, current_path: str = None):
        if not current_path:
            self.current_path = os.getcwd()
        else:
            self.current_path = current_path
            
        self.current_playlist_music = -1
        self.playlist_lenght = 0
        self.mp4_current_path = self.current_path + "\\mp4music"
        self.mp3_current_path = self.current_path + "\\mp3music"

        self.__donwload_youtube_mp4_audio(link)

    def __donwload_youtube_mp4_audio(self, link: str):
        print("Starting process...")

        youtube_playlist_link = []

        if link.startswith("https://www.youtube.com/playlist?list="):
            youtube_playlist_link = Playlist(link).parse_links()
        else:
            youtube_playlist_link += link

        self.playlist_lenght = len(youtube_playlist_link)

        self.__check_directories_existence()

        for youtube_link in youtube_playlist_link:
            print("Downloading music...")

            self.current_playlist_music += 1

            youtube = YouTube(youtube_link)

            streams = youtube.streams.filter(only_audio=True)

            streams.first().download('mp4music')

            self.__convert_mp4_to_mp3()
            print(f"Music {youtube.title} has been downloaded!")
        
        os.rmdir(self.mp4_current_path)

    def __check_directories_existence(self):
        if not os.path.exists(self.mp3_current_path):
            print("Creating mp3music folder...")
            os.makedirs(self.mp3_current_path)

        if not os.path.exists(self.mp4_current_path):
            print("Creating mp4music folder...")
            os.makedirs(self.mp4_current_path)

    def __convert_mp4_to_mp3(self):
        files = os.listdir(self.mp4_current_path)

        for file in files:
            mp4music = self.mp4_current_path + f"\\{file}"

            mp3music = mp4music.replace("mp4music", "mp3music").replace(".mp4", ".mp3")

            if not os.path.exists(mp3music):
                audioclip = AudioFileClip(mp4music)
                audioclip.write_audiofile(mp3music)
                audioclip.close()

                os.remove(mp4music)

                break

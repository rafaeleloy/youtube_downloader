from youtube_audio_downloader import YoutubeDownloader
import sys
import click

@click.command()
@click.argument('link', type=str, required=True)
@click.option('--p', help='The directorie to save the songs.', type=str)
def youtube_downloader(link, p):
    """Simple program to download youtube songs."""
    YoutubeDownloader(link, p)

if __name__ == '__main__':
    youtube_downloader()
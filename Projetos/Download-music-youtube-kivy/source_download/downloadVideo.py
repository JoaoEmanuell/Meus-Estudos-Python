# Global imports

from pytube import YouTube
from pytube.cli import on_progress
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Local imports

from .downloadEssential import DownloadEssential
from .interfaces import DownloadInterface
from .message import Message

class DownloadVideo(DownloadInterface):
    def __init__(self, link : str, mp3 : bool) -> None:
        self.video = YouTube(link, on_progress_callback=on_progress)
        self.convert = mp3
        Message.set_progressbar(100, 0)
        self.__templates_strings = {
            'start' : 'Iniciando o download %s \n%s\nAguarde um pouco!',
            'download' : 'Download %s\n%s\nIniciado',
            'convert' : 'Música \n%s\nbaixada e convertida para MP3',
            'end' : 'Vídeo %s baixado',
            'exists' : '%s "%s" já foi baixado!'
        }
        self.download()

    def download(self):
        if self.convert:
            Message.set_output(self.__templates_strings['start'] % ('da música', self.video.title))
            self.stream = self.video.streams.get_audio_only()
        else:
            Message.set_output(self.__templates_strings['start'] % ('do vídeo', self.video.title))
            self.stream = self.video.streams.get_highest_resolution()
        self.path = DownloadEssential()._get_download_path()
        if DownloadEssential().VerifyIfFileNotExists(self.convert, self.stream, self.path):
            if self.convert:
                Message.set_output(self.__templates_strings['download'] % ('da música', self.video.title))
            else:
                Message.set_output(self.__templates_strings['download'] % ('do vídeo', self.video.title))
            self.stream.download(output_path=f'{self.path}/Música/')
            if self.convert:
                DownloadEssential().ConvertToMp3(self.stream, self.video, self.path)
                Message.set_output(self.__templates_strings['convert'] % (self.video.title))
            else:
                Message.set_output(self.__templates_strings['end'] % (self.video.title))
            Message.set_progressbar(100, 100)
        else :
            if self.convert:
                Message.set_output(self.__templates_strings['exists'] % ('Música', self.video.title))
            else:
                Message.set_output(self.__templates_strings['exists'] % ('Vídeo', self.video.title))
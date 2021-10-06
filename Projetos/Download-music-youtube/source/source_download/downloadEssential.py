from os.path import exists
import sys, os

class DownloadEssential():
    def VerifyIfFileNotExists(self, directoryName):
        source = sys.path[0]
        filename = self.video.title.replace("|", '').replace(".", '').replace("#", '')
        return not(exists(f"{source}/{directoryName}/{filename}.mp3"))

    def ConvertToMp3(self):
        source = sys.path[0]
        filename = self.stream.default_filename.replace('.mp4', '')
        os.rename(f"{source}/Musicas/{filename}.mp4", f"{source}/Musicas/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")
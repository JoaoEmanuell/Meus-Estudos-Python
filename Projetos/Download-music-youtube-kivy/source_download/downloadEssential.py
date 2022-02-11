from os.path import exists
import os

class DownloadEssential():
    def VerifyIfFileNotExists(self):
        if self.convert:
            filename = self.stream.default_filename.replace('.mp4', '')
            return not(exists(f"{self.path}/Musicas/{filename}.mp3"))
        else:
            filename = self.stream.default_filename
            return not(exists(f"{self.path}/Musicas/{filename}"))

    def ConvertToMp3(self):
        filename = self.stream.default_filename.replace('.mp4', '')
        os.rename(f"{self.path}/Musicas/{filename}.mp4", f"{self.path}/Musicas/{filename}.mp3")
        print(f"'{self.video.title}' convertido para mp3")
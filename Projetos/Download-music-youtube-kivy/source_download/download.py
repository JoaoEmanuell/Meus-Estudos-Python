from .interfaces import DownloadInterface
from io import BytesIO
from urllib.request import Request, urlopen
from .message import Message

class Download(DownloadInterface) :
    def download(self, url : str) -> bytes :
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        with urlopen(request) as response : 
            file : bytes = b''
            length = response.getheader('content-Length')
            block_size = 1000000 # 1MB Default

            if length :
                length = int(length)
                block_size = max(4096, length // 20)
            
            print(f'Len : {length} blocksize : {block_size}')

            buffer_all = BytesIO()
            size = 0

            while True :
                buffer_now = response.read(block_size)
                file += buffer_now

                if not buffer_now :
                    break

                buffer_all.write(buffer_now)
                size += len(buffer_now)

                if length :
                    # percent = int((size / length) * 100)
                    # print(f'{percent}%')
                    # print(f'Actual : {size} total : {length}')
                    # progress_bar(int(size), int(length))
                    Message.set_progressbar(int(length), int(size))
            
            # print(f"Buffer all size : {len(buffer_all.getvalue())}")

            return file

    def save_file(self, name : str = '', dir : str = '.', content : bytes = b'') -> None :
        with open(f'{dir}/{name}', 'wb') as f :
            f.write(content)
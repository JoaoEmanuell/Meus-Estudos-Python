class RemoteControll:
    def __init__(self, television : str, room : str) -> None:
        self.television = television
        self.room = room

    def forward_channel(self) -> None:
        print(f"{self.television} in {self.room} is forwarding channel")
    
    def back_channel(self) -> None:
        print(f"{self.television} in {self.room} is back channel")

    def choose_channel(self, channel : int) -> None:
        print(f"{self.television} in {self.room} is chose channel {channel}")

if __name__ == '__main__':
    controll = RemoteControll("Samsung", "Living Room")
    controll.forward_channel()
    controll.back_channel()
    controll.choose_channel(10)
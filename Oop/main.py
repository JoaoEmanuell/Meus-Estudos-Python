class Alarm:
    def __init__(self, state : bool = False) -> None:
        self.__state = state

    def get_state(self) -> bool:
        return self.__state

    def set_state(self, state : bool) -> None:
        self.__state = state

if __name__ == '__main__':
    alarm_one = Alarm()
    print(alarm_one.get_state())
    alarm_one.set_state(True)
    print(alarm_one.get_state())
from typing import Type
class LightSwitch:
    def __init__(self, room : str) -> None:
        self.__room = room

    def light_up(self) -> None:
        print(f"The light in the {self.__room} is on")

    def turn_off(self) -> None:
        print(f"The light in the {self.__room} is off")

class Person:
    def turn_on_light(self, light_switch : Type[LightSwitch]) -> None:
        light_switch.light_up()

    def turn_off_light(self, light_switch : Type[LightSwitch]) -> None:
        light_switch.turn_off()

    def sleep(self) -> None:
        print("I'm sleeping")
        
if __name__ == '__main__':
    Jhon = Person()
    light_switch_room = LightSwitch("room")
    Jhon.turn_on_light(light_switch_room)
    Jhon.turn_off_light(light_switch_room)
    Jhon.sleep()
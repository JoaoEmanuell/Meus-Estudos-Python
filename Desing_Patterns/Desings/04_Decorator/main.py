from typing import Callable

def decorator(function : Callable) -> None:
    def wrapper(*args, **kwargs):
        print("Hello World")
        function(*args, **kwargs)
    return wrapper

class MyClass:
    @decorator
    def method(self, number : int) -> None:
        print(f"My method {number}")

cl = MyClass()
cl.method(6)
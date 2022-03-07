from source import AbstractClass

class Daughter(AbstractClass) :
    def present_method(self) -> None:
        print(self.atribute)

    def abstract_method(self) -> None:
        print("Implementing abstract method")

if __name__ == '__main__':
    daughter = Daughter()
    daughter.present_method()
    daughter.method('Hello World 2')
    daughter.abstract_method()

    '''abstract_class = AbstractClass()
    abstract_class.method('Hello World 3')'''
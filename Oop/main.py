class Calculator:
    def calculate(self, operation : str, num_1 : float, num_2 : float) -> None:
        if operation == '+':
            print(self.__add(num_1, num_2))
        elif operation == '-':
            print(self.__sub(num_1, num_2))
        else :
            print('Invalid operation')

    def __add(self, num_1 : float, num_2 : float) -> float:
        return (num_1 + num_2)

    def __sub(self,  num_1 : float, num_2 : float) -> float:
        return (num_1 - num_2)

if __name__ == '__main__':
    calculator = Calculator()
    calculator.calculate('+', 5, 7)
    calculator.calculate('-', 5, 7)
    calculator.calculate('+-', 5, 7)
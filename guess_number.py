from math import sqrt
from typing import Optional


def add_numbers(firstNumber: int, secondNumber: int) -> int:
    return firstNumber + secondNumber


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None

    root = calculate_square_root(your_number)
    return f"Мы вычислили квадратный корень из введённого вами числа.Это будет: {root}"


firstNumber = 10
secondNumber = 5

print("Сумма чисел: ", add_numbers(firstNumber, secondNumber))

print(calc(25.5))

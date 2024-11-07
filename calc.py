# __init__.py: Imports the classes from the package.

# calculator/__init__.py
from .basic_operations import BasicOperations
from .advanced_operations import AdvancedOperations
from .statistics import Statistics


# basic_operations.py: Contains the class for basic calculation operations.

# calculator/basic_operations.py
class BasicOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")


# advanced_operations.py: Contains the class for more advanced mathematical operations.

# calculator/advanced_operations.py
import math

class AdvancedOperations:
    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number >= 0:
            return math.sqrt(number)
        else:
            raise ValueError("Cannot calculate the square root of a negative number.")

    def logarithm(self, number, base=math.e):
        if number > 0:
            return math.log(number, base)
        else:
            raise ValueError("The number must be greater than zero to calculate the logarithm.")


# statistics.py: Contains the class for statistical operations.

# calculator/statistics.py
class Statistics:
    def mean(self, numbers):
        if len(numbers) > 0:
            return sum(numbers) / len(numbers)
        else:
            raise ValueError("The list of numbers cannot be empty.")

    def median(self, numbers):
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n == 0:
            raise ValueError("The list of numbers cannot be empty.")
        elif n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            middle = n // 2
            return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    def mode(self, numbers):
        from collections import Counter
        if len(numbers) == 0:
            raise ValueError("The list of numbers cannot be empty.")
        count = Counter(numbers)
        max_occurrences = max(count.values())
        modes = [num for num, cnt in count.items() if cnt == max_occurrences]
        return modes


# Below is an example of how to use the "calculator" package:

# main.py
from calculator import BasicOperations, AdvancedOperations, Statistics

if __name__ == "__main__":
    # Creating instances of the classes
    basic = BasicOperations()
    advanced = AdvancedOperations()
    statistics = Statistics()

    # Using BasicOperations
    print("Addition: ", basic.add(5, 3))
    print("Division: ", basic.divide(10, 2))

    # Using AdvancedOperations
    print("Power: ", advanced.power(2, 3))
    print("Square Root: ", advanced.square_root(16))

    # Using Statistics
    number_list = [1, 2, 2, 3, 4]
    print("Mean: ", statistics.mean(number_list))
    print("Median: ", statistics.median(number_list))
    print("Mode: ", statistics.mode(number_list))

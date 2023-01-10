"""
Contains the Calculator class.

...

Classes
-------
Calculator
    A class that can be used to perform basic arithmetic operations.
"""


class Calculator():
    """
    Class used to perform basic arithmetic operations.

    ...

    Attributes
    ----------
    __value : float
        The value displayed on the calculator.
    """

    def __init__(self):
        self.__value = 0

    def get_value(self) -> float:
        """
        Returns the value displayed on the calculator.

        ...

        Returns
        -------
        float
            The value displayed on the calculator.
        """
        return self.__value

    def set_value(self, num: float = 0):
        """
        Sets the value displayed on the calculator.
        By default, the value is set to 0.

        ...

        Parameters
        ----------
        num : float
            The value to be displayed on the calculator. By default, it is set to 0.
        """
        self.__value = num

    def add(self, num: float):
        """
        Adds a number to the value displayed on the calculator.

        ...

        Parameters
        ----------
        num : float
            The number to be added to the value displayed on the calculator.
        """
        self.__value += num

    def subtract(self, num: float):
        """
        Subtracts a number from the value displayed on the calculator.

        ...

        Parameters
        ----------
        num : float
            The number to be subtracted from the value displayed on the calculator.
        """
        self.__value -= num

    def multiply(self, num: float):
        """
        Multiplies the value displayed on the calculator by a number.

        ...

        Parameters
        ----------
        num : float
            The number to be multiplied by the value displayed on the calculator.
        """
        self.__value *= num

    def divide(self, num: float):
        """
        Divides the value displayed on the calculator by a number.
        If the number is 0, it will raise ZeroDivisionError.

        ...

        Parameters
        ----------
        num : float
            The number to be divided by the value displayed on the calculator.

        Raises
        ------
        ZeroDivisionError
            If the number is 0.
        """
        if num == 0:
            raise ZeroDivisionError
        self.__value /= num

    def power(self, num: float):
        """
        Elevates the value displayed on the calculator to a power.

        ...

        Parameters
        ----------
        num : float
            The power to which the value displayed on the calculator will be elevated.
        """
        self.__value **= num

    def root(self, num: float = 2):
        """
        Calculates the root of the value displayed on the calculator.
        By default, the root is the square root.

        ...

        Parameters
        ----------
        num : float
            The root of the value displayed on the calculator.
            It must be an integer. By default, it is set to 2.

        Raises
        ------
        ValueError
            If the number is less or equal to 0.
        """
        if num <= 0 or num % 1 != 0:
            raise ValueError
        self.__value **= 1 / num

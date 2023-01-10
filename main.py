"""
Main file.

PS: Chris, if you are reading this, know that we are doing this homework in our lunch break.
"""
from src.calculator import Calculator

calc = Calculator()
num1 = float(input("Enter the first number: "))
calc.set_value(num1)
num2 = float(input("Enter the second number: "))
print(
    "\nOptions:\n" +
    "1. Add\n" +
    "2. Subtract\n" +
    "3. Multiply\n" +
    "4. Divide\n" +
    "5. Power\n" +
    "6. Root\n"
)
choice = input("Enter your choice: ")
try:
    choice = int(choice)
except ValueError:
    print("Not a number!")
    exit(1)
if choice == 1:
    calc.add(num2)
elif choice == 2:
    calc.subtract(num2)
elif choice == 3:
    calc.multiply(num2)
elif choice == 4:
    calc.divide(num2)
elif choice == 5:
    calc.power(num2)
elif choice == 6:
    calc.root(num2)
else:
    print("Invalid choice!")
    exit(1)
print("\nResult: " + str(calc.get_value()))
input("\nPress ENTER to exit...")

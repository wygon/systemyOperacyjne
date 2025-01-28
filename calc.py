#Author: Szymon Wygonski
#Contact: swygonski@student.wsb-nlu.edu.pl
#Version: 1.1

print("Welcome in simple calculator\nWrite two numbers which you want + - / *")

number1 = float(input("First number"))
number2 = float(input("Second number"))

add = number1 + number2
subtract = number1 - number2
division = number1 / number2
multiplication = number1 * number2

print(f"Your numbers: {number1} and {number2}\n{add} - add result\n{subtract} - subtract result\n{division} - division result\n{multiplication} - multiplication result")

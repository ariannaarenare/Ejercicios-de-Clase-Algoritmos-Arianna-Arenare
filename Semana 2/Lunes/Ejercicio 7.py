number = input("Please enter a number")
if number.isnumeric():
    number = int(number)
else:
    print("Error")

if number%2 == 0:
    print(f"The number {number} is even")

if number%2 != 0:
    print(f"The number {number} is odd")
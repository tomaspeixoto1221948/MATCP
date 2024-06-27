# function input() always returns string
a = input("Write a number:")
b = input("Write a number:")
print(f"The sum of number {a} and {b} is: {a + b}")

a = int(input("Write an int:"))
b = float(input("Write a float:"))
print(f"The sum of number {a} and {b:.3f} is: {a + b:.3f}")
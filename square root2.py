x = int(input("Enter a number from 1-10: "))
y = int(input("Enter a number from 1-10: "))

if (1 <= x <= 10) and (1 <= y <= 10):
    print(f"x={x}, y={y} x*y={x*y}")
else:
    print("Invalid input")

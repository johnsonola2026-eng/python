x = int(input("Enter a number from 1-100:"))
y = int(input("Enter a number from 1-100   "))

if (1 <= x <= 100) and (1 <= y <= 100):
    print(f"x={x}, y={y} x*y={x*y}")
else:
    print("Invalid input")
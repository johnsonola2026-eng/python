from builtins import ValueError, input, print

rowsize = int(input("please enter the number of rows: "))

if rowsize < 1:
    raise ValueError("The number of rows must be positive")

top_rows = (rowsize + 1) // 2
bottom_rows = rowsize // 2

for i in range(1, top_rows + 1):
    print(" " * (top_rows - i), end="")
    print(" ".join(str(num) for num in range(1, 2 * i)))

for i in range(bottom_rows, 0, -1):
    print(" " * (top_rows - i), end="")
    print(" ".join(str(num) for num in range(1, 2 * i)))
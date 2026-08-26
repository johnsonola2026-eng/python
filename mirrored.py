rows = int(input("Enter the height of the triangle: "))
for i in range(1, rows + 1):
   for j in range(1, rows + 1):
       if j <= rows - i:
           print(' ', end=' ')
       else:
           print('*', end=' ')
   print()
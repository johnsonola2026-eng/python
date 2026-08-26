import builtins

rows = int(builtins.input("please enter the total number of rows: "))
number=1
builtins.print("floyd's triangle")
for i in range(1,rows+1):
    for j in range(1,i+1):
        builtins.print(number, end='')
        number=number+1
    builtins.print()
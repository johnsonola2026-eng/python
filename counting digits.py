import builtins

number = int(builtins.input("Enter a number: "))
digit_count = builtins.len(str(builtins.abs(number)))

builtins.print(f"The number has {digit_count} digit(s).")

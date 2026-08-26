from builtins import ValueError, abs, input, print

try:
	x = int(input("Type a decimal: "))
	y = int(input("Type a base: "))

	if not 2 <= y <= 36:
		raise ValueError("The base must be between 2 and 36.")

	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if x == 0:
		result = "0"
	else:
		sign = "-" if x < 0 else ""
		value = abs(x)
		result = ""
		while value:
			result = digits[value % y] + result
			value //= y
		result = sign + result

	print(result)
except ValueError as error:
	print(f"Error: {error}")
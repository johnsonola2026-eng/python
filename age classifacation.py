age = int(input("type age: "))
if 1 <= age <= 9 or 21 <= age <= 100:
    print("not allowed")
else:
    if 10 <= age <= 20:
        print("allowed")
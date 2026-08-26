import sys

num = int(sys.stdin.readline().strip())
total = 0
temp=num
while temp>0:
    digit=temp%10
    total += digit**3
    temp//=10
if num == total:
 sys.stdout.write(f"{num} is an armstrong number\n")
else:
 sys.stdout.write(f"{num} is not an armstrong number\n")
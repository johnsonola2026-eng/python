string=input("please enter your own words:")
char=input("please enter your own character:")
i=0
count=0
while(i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1
print("total amount of times",char,"has Ocurred=",count)
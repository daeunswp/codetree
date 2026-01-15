a, b = map(int, input().split())

while(True):
    print(a, end=" ")
    if(a%2==1):
        a = 2*a
    elif(a%2==0):
        a = a+3
    if(a>b):
        break
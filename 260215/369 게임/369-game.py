n = int(input())

temp = 1

while temp<=n:
    if temp//10==0:
        if temp%3==0:
            print(0, end=" ")
        else:
            print(temp, end=" ")
    else:
        if (temp//10)%3!=0 and temp%10==0:
            print(temp, end=" ")
        elif (temp//10)%3==0 or (temp-(temp//10)*10)%3==0 or temp%3==0:
            print(0, end=" ")
        else:
            print(temp, end=" ")
    temp+=1
n=int(input())
temp=2
while(True):
    if temp==n:
        print('N')
        break
    if n%temp==0:
        print('C')
        break
    temp+=1
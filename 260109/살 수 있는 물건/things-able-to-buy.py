n= int(input())
book = 3000
mask = 1000

if(n<=0):
    print('no')
elif(n<=mask):
    print('mask')
elif(n<=book):
    print('book')
else:
    print('no')

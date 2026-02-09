mid, final = map(int, input().split())

if(mid>=90):
    if(95<=final<=100):
        print(100000)
    elif(final>=90):
        print(50000)
    else:
        print(0)
else:
    print(0)
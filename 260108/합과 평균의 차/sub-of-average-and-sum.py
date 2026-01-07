a,b,c = map(int, input().split())

sum = a + b + c

if(sum%3 != 0):
    print("세 수의 합이 3의 배수가 아닙니다")

else:
    print(sum)
    print(int(sum/3))
    print(int(sum - sum/3))
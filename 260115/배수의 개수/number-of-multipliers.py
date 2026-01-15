multiples_three = 0
multiples_five = 0

for i in range(10):
    n = int(input())
    if(n%3==0):
        multiples_three+=1
    if(n%5==0):
        multiples_five+=1

print(multiples_three, multiples_five)
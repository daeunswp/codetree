height, weight = map(int, input().split())

bmi = (10000*weight)//(height*height)

print(bmi)

if(bmi>=25):
    print("Obesity")
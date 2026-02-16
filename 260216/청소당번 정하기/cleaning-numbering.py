n = int(input())

class_cnt = 0
hallway_cnt = 0
toilet_cnt = 0

for i in range(1, n+1):
    if i%12==0:
        toilet_cnt+=1
    elif i%6==0 or i%3==0:
        hallway_cnt+=1
    elif i%2==0:
        class_cnt+=1

print(class_cnt, hallway_cnt, toilet_cnt)
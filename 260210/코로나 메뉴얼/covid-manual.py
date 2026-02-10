a_symp, a_temp = input().split()
b_symp, b_temp = input().split()
c_symp, c_temp = input().split()

cnt = 0

if a_symp=='Y' and int(a_temp)>=37:
    cnt+=1
if b_symp=='Y' and int(b_temp)>=37:
    cnt+=1
if c_symp=='Y' and int(c_temp)>=37:
    cnt+=1

if(cnt>=2):
    print('E')
else:
    print('N')
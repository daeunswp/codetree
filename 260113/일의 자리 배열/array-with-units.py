nlist = list(map(int, input().split()))

for i in range(8):
    append_num = (nlist[i]+nlist[i+1]) % 10
    nlist.append(append_num)

for i in range(10):
    print(nlist[i], end=" ")
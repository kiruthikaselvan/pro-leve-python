n,li=int(input()),[]
for i in range(n):
    temp=list(map(int,input().split()))
    li=li+temp
li.sort()
print(*li)

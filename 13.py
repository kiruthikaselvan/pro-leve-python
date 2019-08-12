num,tc=map(int,input().split())
inp=list(map(int,input().split()))
for i in range(tc):
    s,e=map(int,input().split())
    temp=inp[s-1:e]
    print(min(temp))

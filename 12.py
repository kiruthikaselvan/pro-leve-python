n,k=map(int,input().split())
inp=list(map(int,input().split()))
for i in range(k):
    s,e=map(int,input().split())
    sum,temp=0,inp[s-1:e]
    for i in temp:
        sum=sum+i
    print(sum)
    

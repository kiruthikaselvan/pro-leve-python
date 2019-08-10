def check(s1,s2):
    res=""
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            res=res+s1[i]
        else:
            break
    return res
n,l=int(input()),[]
for i in range(n):
    m=input()
    l.append(m)
fr=check(l[0],l[1])
for i in range(2,len(l)-1):
    fr=check(fr,l[i])
print(fr)

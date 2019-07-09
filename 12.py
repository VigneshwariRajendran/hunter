sd,ad=map(int,input().split())
jk=list(map(int,input().split()[:ad]))
jk.sort()
jk=jk[::-1]
print(jk[ad-1])

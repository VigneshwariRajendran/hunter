dvi=input().split()
thu=[]
for i in dvi:
   thu.append(i[::-1])
print(' '.join(map(str,thu)))

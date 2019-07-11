kl=int(input())
kl=list(map(int,input().split()))
kl.sort()
kl.reverse()
if(kl[0]==0):
   print("0")
else:
   for i in kl:
      print(i,end="")

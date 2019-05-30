ch=int(input())
if(ch>0):
  for i in range(2,ch//2):
    if(ch%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")

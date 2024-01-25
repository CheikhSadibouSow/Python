
def premier(n):
    cpt = 0
    for i in range(1,n+1):
        if n%i==0 :
         cpt+=1
    if cpt==2 :
       return True
    else :
      return False
  
n=-1
while n<=0:
  n=int(input("Entrer un nombre positif : "))
if premier(n)==True :
   print(n ,"est un nombre premier.")    
else :
   print(n ,"n'est pas un nombre premier.")   
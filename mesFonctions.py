T=[]
def creationTableau(T) :
    print("=======Creation du tableau=======")
    rep = "O"
    while rep == "O" :
        n = int(input("Entrer une valeur : "))
        T.append(n)
        print("Voulez-vous entrer une nouvelle valeur ?(O/N) : ")
        rep = input("")

def afficheTableau(T) :
    for i in range(len(T)) :
      print(T[i],end="\t\n")  
      
      
def decalageGauche(T):
    n = len(T)
    tmp = T[0]  
    i = 1
    while i < n  :  
      T[i-1] = T[i]
      i+=1
    T[n-1] = tmp          

def menu () :
     
  choix = 1 
  while choix != 4 :
    print("\n\t===============MENU===============")
    print("\n\t*****1.Creation du tableau")
    print("\n\t*****2.Affichage du tableau")
    print("\n\t*****3.Decalage Gauche du tableau")
    print("\n\t*****4.Quitter")
    print("\n\t*****Faites votre choix : ")
    choix = int(input(""))
    if choix == 1 :
        creationTableau(T)
    if choix == 2 :
        afficheTableau(T)
    if choix == 3 :
        decalageGauche(T)
        afficheTableau(T)      
    if choix == 4 :
        print("\tMerci d'avoir utiliser notre Appli !!!")  
    if choix < 1 or choix > 4 :
       print("\n\tVotre choix n'existe pas .")             
        

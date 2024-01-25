Tab = []
def createTabEmploy(Tab):
    rep = "Oui"
    while rep=="Oui":
      print("Donnez le matricule : ")  
      mat = input("")
      nom =  input("Donnez le nom : ")
      prenom =  input("Donnez le prenom : ")
      adresse =   input("Donnez l'adresse : ")
      sal = int(input('Donnez le salaire : '))
      info = mat+"\t"+nom+"\t"+prenom+"\t"+adresse+"\t"+str(sal)
      Tab.append(info)
      rep = input("Voulez-vous ajouter un autre employes(O/N) ? ")

def affTabEt(Tab) :
    print("=====Les employes du tableaux sont : ======\n")
    for i in range(len(Tab)):
     print(Tab[i],end="\n")
def decalageDroite(Tab):
    n = len(Tab)
    i = n-1
    tmp = Tab[n-1]
    while i > 0 :
      Tab[i]=Tab[i-1]
      i-=1
      Tab[0]=tmp

def menu():
    choix = 1
    while choix != 4 :
        print("\t\n==========Menu===========\n")
        print("***1-Creation tableau employe\n")     
        print("***2-Affichage tableau employe\n")
        print("***3-decalage a droite tableau employe\n")
        print("***4-Quitter Application\n") 
        
        print("Faites votre choix : ",end="\t")
        choix = int(input(""))
        if choix == 1 :
            createTabEmploy(Tab)              
        if choix == 2 :
            affTabEt(Tab)
        if choix == 3 :
            decalageDroite(Tab)
        if choix == 4 :
            print("Au revoir et a la prochaine !!!")    
        if choix < 1 or choix > 4 :
            print("Le choix n'existe pas .")        

menu()    
      
    
        



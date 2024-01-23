import os
def createFile() :
    fe=open("listeEtudiant.txt",'w')   
    rep = "O"
    while rep == "O" :
        mat = input("Donner le matricule de l'etudiant : ")
        prenom = input("Donner le prenom de l'etudiant : ")
        nom = input("Donner le nom de l'etudiant : ")
        classe = input("Donner la classe de l'etudiant : ")
        moy = -1
        while moy < 0 :
         moy = float(input("Donner sa moyenne : "))
        info = mat+ "\t" +prenom+ "\t" +nom+ "\t" +classe+ "\t" +str(moy)+"\n"
        fe.write(info)
        rep = input("Voulez-vous ajouter un autre etudiant (O/N) : ")
    fe.close()

def readFile() :
    if os.path.isfile("listeEtudiant.txt") :
       fe=open("listeEtudiant.txt",'r')
       contenu = fe.read()
       print("==>Le Contenu du fichier est : ")
       print(contenu,end="\n")
       fe.close()
    else :
        print("==>Le fichier n'existe pas.")

def addFile():
    fe=open("listeEtudiant.txt",'a')
    rep = "O"
    while rep == "O" :
        mat = input("Donner le matricule de l'etudiant : ")
        prenom = input("Donner le prenom de l'etudiant : ")
        nom = input("Donner le nom de l'etudiant : ")
        classe = input("Donner la classe de l'etudiant : ")
        moy = -1
        while moy < 0 :
         moy = float(input("Donner sa moyenne : "))
        info = mat+ "\t" +prenom+ "\t" +nom+ "\t" +classe+ "\t" +str(moy)
        fe.write(info)
        rep = input("Voulez-vous ajouter un autre etudiant (O/N) : ")
    fe.close()

def menu () :
     
  choix = 1 
  while choix != 4 :
    print("\n\t===============MENU===============")
    print("\n\t*****1.Creation du fichier etudiant")
    print("\n\t*****2.Affichage du contenu du fichier")
    print("\n\t*****3.Ajout d'un nouveau etudiant")
    print("\n\t*****4.Quitter")
    print("\n\t*****Faites votre choix : ")
    choix = int(input(""))
    if choix == 1 :
       createFile()
    if choix == 2 :
        readFile()
    if choix == 3 :
        addFile()      
    if choix == 4 :
        print("\tMerci d'avoir utiliser notre Appli !!!")  
    if choix < 1 or choix > 4 :
       print("\n\tVotre choix n'existe pas .") 
       
menu()                   
        
                        
import json


class Tache:
    titre:str
    description:str
    statut:str

    def marquer_terminer (self):
        self.statut=self.vers_dict(2)

    def vers_dict(self,n):
        self.DICTIONNAIRE = {
            1:'a faire',
            2:'terminee'
        }
        if n==1 :
             return self.DICTIONNAIRE[1]
        elif n==2 :
             return self.DICTIONNAIRE[2]

class GestionnaireTaches:
    taches:list[Tache]

    def __init__(self):
         self.taches=[]
         self.charger()
    
    def ajouter (self,titre,description):
        objet=Tache()
        objet.titre=titre
        objet.description=description
        objet.statut=objet.vers_dict(1)
        self.taches.append(objet)
        self.sauvegarder()

    def afficher (self,status=None):
        for i in self.taches :
            if i.statut==status :
                print ("-> titre : "+ i.titre )
                print("description :" + i.description )
                print("statut: " + i.statut)
            if status==None :
                print ("-> titre : "+ i.titre )
                print ("description : " + i.description )
                print("statut: " + i.statut)
    

    def modifier (self,index,titre,description,status):
        self.taches[index].titre= titre
        self.taches[index].description=description
        if status ==self.taches[index].vers_dict(2):
            self.taches[index].marquer_terminer()
        else :
             self.taches[index].statut=self.taches[index].vers_dict(1)
        self.sauvegarder()

    def supprimer (self,index):
        self.taches.pop(index)
        self.sauvegarder()

    def sauvegarder (self):
        data = {"taches": []}
        for i in self.taches:
            tache_dict = {
                "titre": i.titre,
                "description": i.description,
                "statut": i.statut
            }
            data["taches"].append(tache_dict)
            
        with open('taches.json', 'w', encoding='utf-8') as t:
            json.dump(data, t, ensure_ascii=False, indent=4)
        print('sauvegarde effectuée')

    def charger (self):
        try:
            with open("taches.json", "r", encoding="utf-8") as t:
                data = json.load(t)
                self.taches = []
                for item in data.get("taches", []):
                    tache = Tache()
                    tache.titre = item["titre"]
                    tache.description = item["description"]
                    tache.statut = item["statut"]
                    self.taches.append(tache)
        except FileNotFoundError:
            pass

finboucle = False
objetGT=GestionnaireTaches()

while finboucle == False :
    print ("menu interactif :")
    print ("1- Ajouter")
    print ('2- Afficher')
    print ('3- Modifier')
    print ('4- Supprimer')
    print ('5- Filtrer')
    print ('0- Quitter')

    choix=input()

    if choix=='1' :
        print ('donner le nom de la tache a ajouter')
        nomAjout=input()
        print ('donner la description de cette tache')
        descriptioonAjout=input()
        objetGT.ajouter(nomAjout,descriptioonAjout)

    if choix=='2' :
            objetGT.afficher()

    if choix=='3' :
        c=5
        while c==5:
             try :
                  print ("entrer l'index de l'element a modifier")
                  indexM=int(input())
                  c=6
             except ValueError :
                  print('erreur veuiller entrer un nombre entier')



        print ("entrer le titre modifiee")
        titreM=input()
        print ("entrer la description modifiee")
        descriptionM=input()
        while c==6:
            print ("entrer le status modifiee (a faire/terminee)")
            statusM=input()
            if statusM=='a faire' or statusM=='terminee':
                c=7
            else :
                 print("statut incorrecte veuiller entrer: 'a faire' ou bien 'terminer'")
                  
        objetGT.modifier(indexM,titreM,descriptionM,statusM)

    if choix=='4' :
        print ("entrer l'index de l'element a supprimer")
        indexS=int(input())
        objetGT.supprimer(indexS)

    if choix=='5' :
         c=7
         while c==7:
            print ("vous voulez afficher les taches 'a faire' ou 'terminee'?")
            choixAffichage=input()
            if choixAffichage == 'a faire':
                c=8
                objetGT.afficher('a faire')
            elif choixAffichage == 'terminee':
                c=8
                objetGT.afficher('terminee')
            else :
                print('option non disponible')
        
    if choix=='0' :
        finboucle=True
        exit()
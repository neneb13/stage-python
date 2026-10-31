import random
import json

with open("scores.json","r",encoding="utf-8") as scores:
     score= json.load(scores)
    
def demander_nombre():
    print ("deviner le nombre :")
    return int(input())
def verifier(n):
    try :
         if n == nombre_aleatoire:
              print("Gagne !")
              return True
         elif n < nombre_aleatoire:
              print ("nombre trop petit")
              return False
         else:
              print("nombre trop grand")
              return False
    except NameError:
         print("entrer un niveau disponible")
         
    
def jouer():
    global nbr_essai,correcte
    while correcte == False:
       guess=demander_nombre()
       proposition.append(guess)
       nbr_essai += 1
       correcte=verifier(guess)
global sortie
sortie= False
NIVEAUX = {
    "facile": (1, 50),
    "moyen": (1, 100),
    "difficile": (1, 500),
}

while sortie == False :
    print("Menu :")
    print(" 1 - jouer ")
    print(" 2 - voir le score ")
    print(" 3 - quitter ")
    choixMenu=input()
    if choixMenu=='1':
            print ("choisir un niveau de difficulte : facile/moyen/difficile ")
            
            niveau=input ()
            if niveau == 'facile':
                nombre_aleatoire= random.randint(NIVEAUX["facile"][0],NIVEAUX['facile'][1])
                score["niveau"]='facile'
            elif niveau == 'moyen':
                nombre_aleatoire= random.randint(NIVEAUX["moyen"][0],NIVEAUX["moyen"][1])
                score["niveau"]='moyen'
            elif niveau =='difficile':
                nombre_aleatoire= random.randint(NIVEAUX["difficile"][0],NIVEAUX["difficile"][1])
                score["niveau"]='difficile'
            
            correcte= False
            nbr_essai =0
            proposition=[]
            score['essaies']=[]
            jouer()
            if correcte == True:
                 score['nombre essaies']=nbr_essai
                 for i in proposition:
                      score['essaies'].append(i)    
                 with open("scores.json", "w", encoding="utf-8") as scores:
                      json.dump(score, scores,indent=4)
                 print (f"nombre d'essaie : {nbr_essai}")
                 print("recapitulatif de toutes les proposition : ")
                 for i in range(nbr_essai):
                     print(str(proposition[i]))          
    elif choixMenu=='2':
            print(score)
            print(f"nom :{score['nom']}")
            print(f"niveau :{score['niveau']}")
            print(f"nombre d'essaies :{score['nombre essaies']} ")
            for i in score['essaies']:
                 print (i)
    elif choixMenu=='3':
            sortie= True
            exit()






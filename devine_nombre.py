import random
    
def demander_nombre():
    print ("deviner le nombre de 1 a 100")
    return int(input())
def verifier(n):
    if n == nombre_aleatoire:
        print("Gagne !")
        return True
    elif n < nombre_aleatoire:
        print ("nombre trop petit")
        return False
    else:
        print("nombre trop grand")
        return False
def jouer():
    global nbr_essai,correcte
    while correcte == False:
       guess=demander_nombre()
       proposition.append(guess)
       nbr_essai += 1
       correcte=verifier(guess)

print ('vous voulez jouez? : oui/non')
choix_jeu= input()
if choix_jeu=='oui':
    nombre_aleatoire= random.randint(1,100)
    correcte= False
    nbr_essai =0
    proposition=[]
    jouer()
else:
    exit()
if correcte == True :
    print (f"nombre d'essaie : {nbr_essai}")
    print("recapitulatif de toutes les proposition : ")
    for i in range(nbr_essai):
       print(str(proposition[i])+' ')





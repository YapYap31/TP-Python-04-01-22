import re

nom = input("Quel est votre nom ? \n")
prenom = input("Quel est votre prénom ? \n")
annee = int(input("Quelle est votre année de naissance ? \n"))

if annee > 2022 - 6:
    print("#####################")
    print("Vous n'êtes pas admis")
    print("#####################")
elif annee > 2022 - 12:
    print("#####################")
    print("Vous êtes poussin")
    print("#####################")
elif annee > 2022 - 18:
    print("#####################")
    print("Vous êtes cadet")
    print("#####################")
elif annee > 2022 - 24:
    print("#####################")
    print("Vous êtes junior")
    print("#####################")
elif annee > 2022 - 30:
    print("#####################")
    print("Vous êtes semi-pro")
    print("#####################")
elif annee >= 2022 - 40:
    print("#####################")
    print("Vous êtes pro")
    print("#####################")
else:
    print("#####################")
    print("Vous n'êtes pas admis")
    print("#####################")

def verif_mail(adresse):
    rex = re.compile("[A-Z]{1}.[a-z]{6}@baton-rouge.fr")
    if rex.fullmatch(adresse):
        return True
    else:
        return False

mail = input("Quelle est votre adresse mail ? \n")

if verif_mail(mail):
    print("OK")
    print(f"Nom : {(nom)} ; Prénom : {(prenom)} ; Mail : {(mail)} ")
else:
    print("Ecrivez correctement votre adresse mail ! modèle : H.potter@baton-rouge.fr")
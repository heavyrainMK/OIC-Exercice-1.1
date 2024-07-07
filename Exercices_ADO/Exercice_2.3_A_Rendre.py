# *******************************************************
# Nom ......... : Exercice_2.3_A_Rendre.py
# Rôle ........ : Convertir un nombre décimal en chiffres romains
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 19/11/2023
# Licence ..... : Réalisé dans le cadre du cours de l'Architecture des Ordinateurs
# Usage : Pour exécuter : python Exercice_2.3_A_Rendre.py 
#********************************************************

# Fonction pour convertir un nombre décimal en chiffres romains
def conv_nombre_en_chiffre_romain(nombre):
    if not (0 < nombre < 4000):
        raise ValueError("Le nombre doit être compris entre 1 et 3999 inclus.")

    valeurs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    chiffres_romains = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    resultat = ''
    for valeur, chiffre_romain in zip(valeurs, chiffres_romains):
        while nombre >= valeur:
            resultat += chiffre_romain
            nombre -= valeur

    return resultat

# Saisie du nombre par l'utilisateur avec gestion des erreurs
try:
    saisie_utilisateur = int(input("Entrez un nombre : "))
except ValueError:
    print("Erreur : Veuillez entrer un nombre entier.")
    exit()

# Conversion et affichage en chiffres romains
romain_resultat = conv_nombre_en_chiffre_romain(saisie_utilisateur)
print(f"Le nombre {saisie_utilisateur} en chiffres romains est : {romain_resultat}")






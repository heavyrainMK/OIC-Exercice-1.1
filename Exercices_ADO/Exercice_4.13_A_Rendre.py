# *******************************************************
# Nom ......... : Exercice_4.13_A_Rendre.py
# Rôle ........ : Multiplier deux nombres en virgule flottante et normaliser le résultat
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 03/07/2024
# Licence ..... : Réalisé dans le cadre du cours de l'Architecture des Ordinateurs
# Usage : Pour exécuter : "python Exercice_4.13_A_Rendre.py" 
# *******************************************************

# Fonction pour multiplier deux nombres en virgule flottante
def multiplier_nombres_flotants(a, b):
    try:
        resultat = a * b
    except Exception as e:
        print(f"Erreur lors de la multiplication : {e}")
        return None
    return resultat

# Fonction pour normaliser un résultat en virgule flottante
def normaliser_resultat(resultat):
    try:
        # Si le résultat est 0, il est déjà normalisé.
        if resultat == 0:
            return 0, 0
        exposant = 0
        # Diviser le résultat par 10 jusqu'à ce qu'il soit inférieur à 10.
        while abs(resultat) >= 10:
            resultat /= 10
            exposant += 1
        # Multiplier le résultat par 10 jusqu'à ce qu'il soit supérieur ou égal à 1.    
        while abs(resultat) < 1:
            resultat *= 10
            exposant -= 1
    except Exception as e:
        print(f"Erreur lors de la normalisation : {e}")
        return None, None
    return resultat, exposant

# Fonction pour obtenir un nombre en virgule flottante de l'utilisateur
def obtenir_nombre(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre en virgule flottante.")

# Exemple d'utilisation
nombre_1 = obtenir_nombre("Entrez le premier nombre en virgule flottante : ")
nombre_2 = obtenir_nombre("Entrez le deuxième nombre en virgule flottante : ")

# Si la multiplication est réussie, normaliser le résultat
resultat = multiplier_nombres_flotants(nombre_1, nombre_2)
if resultat is not None:
    resultat_normalise, exposant = normaliser_resultat(resultat)
    # Si la normalisation est réussie, afficher le résultat
    if resultat_normalise is not None:
        print(f"Le résultat normalisé de la multiplication est : {resultat_normalise}e{exposant}")
    else:
        print("Erreur lors de la normalisation du résultat.")
else:
    print("Erreur lors de la multiplication des nombres.")

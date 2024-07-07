# *******************************************************
# Nom ......... : Exercice_2.2_Bonus.py
# Rôle ........ : Additionner deux nombres écrits en chiffres romains
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 19/11/2023
# Licence ..... : Réalisé dans le cadre du cours de l'Architecture des Ordinateurs
# Usage : Pour exécuter : python Exercice_2.2_Bonus.py 
#********************************************************

# Fonction pour convertir un nombre en chiffres romains
def chiffre_romain_en_nombre_decimal(chiffre_romain):
    # Dictionnaire des correspondances entre les chiffres romains et les valeurs décimales
    chiffres_romains = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    decimal = 0

    i = 0
    # Parcourt la chaîne de caractères représentant le nombre en chiffres romains
    while i < len(chiffre_romain):
        # Vérifie si le caractère actuel a une valeur inférieure au caractère suivant
        if (i < len(chiffre_romain) - 1) and (chiffres_romains[chiffre_romain[i]] < chiffres_romains[chiffre_romain[i + 1]]):
            # Si c'est le cas, soustrait la valeur actuelle de la valeur suivante
            decimal += chiffres_romains[chiffre_romain[i + 1]] - chiffres_romains[chiffre_romain[i]]
            i += 2
        else:
            # Sinon, ajoute simplement la valeur actuelle au nombre décimal
            decimal += chiffres_romains[chiffre_romain[i]]
            i += 1

    return decimal

# Fonction pour convertir un nombre décimal en chiffres romains
def nombre_decimal_en_chiffre_romain(nombre_decimal):
    if not (0 < nombre_decimal < 4000):
        raise ValueError("Le nombre decimal doit être compris entre 1 et 3999 inclus.")
    
    valeurs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    chiffres_romains = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    resultat = ''
    for valeur, chiffre_romain in zip(valeurs, chiffres_romains):
        while nombre_decimal >= valeur:
            resultat += chiffre_romain
            nombre_decimal -= valeur

    return resultat

# Fonction pour additionner deux nombres en chiffres romains
def additioner_chiffres_romains(chiffre1, chiffre2):
    # Convertit les chiffres romains en nombres décimaux, les additionne, puis reconvertit le résultat en chiffres romains
    resultat_decimal = chiffre_romain_en_nombre_decimal(chiffre1) + chiffre_romain_en_nombre_decimal(chiffre2)
    resultat_chiffres_romains = nombre_decimal_en_chiffre_romain(resultat_decimal)

    return resultat_chiffres_romains

# Fonction pour saisir les nombres en chiffres romains de l'utilisateur
def saisie_utilisateur():
    # Saisie de l'utilisateur
    saisie_utilisateur1 = input("Entrez le premier nombre en chiffres romains : ").strip().upper()
    saisie_utilisateur2 = input("Entrez le deuxième nombre en chiffres romains : ").strip().upper()

    # Validation des saisies
    chiffres_valides = {'M', 'D', 'C', 'L', 'X', 'V', 'I'}
    if not all(char in chiffres_valides for char in saisie_utilisateur1):
        print("Erreur : Veuillez entrer un nombre valide en chiffres romains.")
        exit()
    if not all(char in chiffres_valides for char in saisie_utilisateur2):
        print("Erreur : Veuillez entrer un nombre valide en chiffres romains.")
        exit()

    return saisie_utilisateur1, saisie_utilisateur2

# Le résultat de la saisie de l'utilisateur
resultat_chiffres_romains_1, resultat_chiffres_romains_2 = saisie_utilisateur()

# Effectue l'addition des nombres en chiffres romains saisis par l'utilisateur.
resultat_final = additioner_chiffres_romains(resultat_chiffres_romains_1, resultat_chiffres_romains_2)

# Affichage du résultat final
print(f"Le résultat de l'addition est : {resultat_final}")




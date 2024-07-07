# *******************************************************
# Nom ......... : Exercice_4.17_Bonus.py
# Rôle ........ : Calculer l'exponentielle d'un nombre en utilisant la série de Taylor
# Auteur ...... : Maxim Khomenko
# Version ..... : V1.0.0 du 03/07/2024
# Licence ..... : Réalisé dans le cadre du cours de l'Architecture des Ordinateurs
# Usage : Pour exécuter : "python Exercice_4.17_Bonus.py"
# *******************************************************

# Importer le module math pour utiliser la fonction de factorielle
import math

# Fonction pour calculer l'exponentielle d'un nombre en utilisant la série de Taylor
def exponentielle_taylor(x, n):
    result = 0
    for i in range(n):
        result += (x**i) / math.factorial(i)
    return result

# Fonction pour obtenir une entrée utilisateur de type spécifié
def obtenir_entree_utilisateur(prompt, type_attendu): 
    while True:
        try:
            return type_attendu(input(prompt)) 
        except ValueError:
            print(f"Erreur : veuillez entrer une valeur valide pour {type_attendu.__name__}.") 

# Demander à l'utilisateur d'entrer une valeur pour x
x = obtenir_entree_utilisateur("Entrez la valeur de x : ", float)

# Demander à l'utilisateur d'entrer le nombre de termes de la série de Taylor
n = obtenir_entree_utilisateur("Entrez le nombre de termes dans la série de Taylor : ", int)

if n <= 0:
    print("Erreur : Le nombre de termes doit être un entier positif.")
else:
    # Fonction exponentielle de Python pour obtenir la valeur réelle
    valeur_reelle = math.exp(x)

    # Calcul de l'approximation
    resultat_approximatif = exponentielle_taylor(x, n)

    # Calcul de l'erreur d'approximation
    erreur_approximation_absolue = abs(valeur_reelle - resultat_approximatif)

    # Affichage des résultats
    print(f"La valeur réelle de e^{x} est : {valeur_reelle}")
    print(f"L'approximation de l'exponentielle avec {n} termes de la série de Taylor est : {resultat_approximatif}")
    print(f"L'erreur d'approximation absolue est : {erreur_approximation_absolue}")
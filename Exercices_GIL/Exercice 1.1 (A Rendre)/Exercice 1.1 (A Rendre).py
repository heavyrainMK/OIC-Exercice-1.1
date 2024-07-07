# Importe la bibliothèque WordCloud depuis le module wordcloud
from wordcloud import WordCloud

# Importe la bibliothèque matplotlib.pyplot depuis le module matplotlib
import matplotlib.pyplot as plt

# Importe la bibliothèque random pour générer des nombres aléatoires
import random

# Importe la bibliothèque os pour manipuler les chemins de fichiers
import os

# Texte personnalisé contenant les mots à inclure dans le nuage de mots
text_personnalisé = (
    "Quantique, Qubit, Superposition, Intrication, Algorithme, Numérique,"
    "Donnée, Discrimination, Sécurité, Cryptographie, "
    "Apprentissage Automatique, Intelligence Artificielle, "
    "Médecine, Climat, Énergie, Finance, Environnement, "
    "Optimisation, Simulation, Pasqal, IBM, Google, Thales, "
    "ANSSI, France, Limité, Chine, Évolutivité, Progrès, "
    "Ordinateur, Menaces, Sécurité, Révolution, "
    "Potentiel, Investissement, Collaboration, Innovation, Avenir," 
    "Technologie, Recherche, Développement," 
    "Défi, Opportunité, Calcul, Performance, Informatique"
)

# Chemin du répertoire contenant le script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Chemins des fichiers de police relatifs au répertoire du script
font_dir = "Bebas_Neue,Butterfly_Kids,Oswald,Rubik_Scribble,Workbench"

# Chemins des fichiers de police relatifs au répertoire du script
font_paths = [
    os.path.join(script_dir, 'BioRhyme/BioRhyme-VariableFont_wdth,wght.ttf'),
    os.path.join(script_dir, font_dir, 'Bebas_Neue/BebasNeue-Regular.ttf'),
    os.path.join(script_dir, font_dir, 'Butterfly_Kids/ButterflyKids-Regular.ttf'),
    os.path.join(script_dir, font_dir, 'Oswald/Oswald-VariableFont_wght.ttf')
]

# Définit une fonction de couleur personnalisée pour le nuage de mots
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    # Retourne une couleur aléatoire au format HSL
    return "hsl({}, 100%, 50%)".format(random.randint(0, 360))

# Choisis aléatoirement un chemin de police parmi ceux spécifiés
font_path = random.choice(font_paths)

# Crée un nuage de mots à partir du texte personnalisé avec les paramètres spécifiés
wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=color_func, font_path=font_path).generate_from_text(text_personnalisé)

# Affiche le nuage de mots avec les paramètres spécifiés
plt.figure(figsize=(10, 5))  # Définit la taille de la figure
plt.imshow(wordcloud, interpolation='bilinear')  # Affiche le nuage de mots
plt.axis('off')  # Désactive les axes
plt.show()  # Affiche la figure
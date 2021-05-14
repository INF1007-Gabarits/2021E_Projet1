import random

# PARTIE 1 =======================================================
dictionnaire = [
    {
        "mot": "luzerne",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "jury",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "comete",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "competition",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "respirer",
        "type": "verbe",
        "temps": "infinitif"
    },
    {
        "mot": "cuisinier",
        "type": "verbe",
        "temps": "infinitif"
    },
    {
        "mot": "pneus",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "hippopotame",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "pression",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "collision",
        "type": "nom",
        "genre": "féminin"
    }
]

# TODO: À partir du dictionnaire, créez une liste de noms féminins

# PARTIE 2 =======================================================

# Initialiser vos variables

# Sélectionner un mot aléatoire à faire deviner dans la liste des noms féminins

# Tant que le mot n'est pas deviné et qu'il reste des vies:

    # Afficher les lettres devinées à date
    # Demander à l'utilisateur de deviner une lettre

    # SI la lettre a déjà été essayée
        # Dire à l'utilisateur de recommencer

    # SINON S'il s'agit d'un bon essai
        # ajouter la lettre aux lettre essayées
        # Calculer le mot qu'il a deviné jusqu'à présent
        #  Dire bravo à l'utilisateur et lui montrer le mot

    # SINON (c'est un mauvais essai)
        # ajouter la lettre aux lettre essayées
        # enlever une vie
        # dire à l'utilisateur il lui reste combien de vies


# En sortant de la boucle principale, SI l'utilisateur n'a plus de vies, c'est quil a perdu
# SINON il a gagné :)
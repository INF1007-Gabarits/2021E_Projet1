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

# TODO: Initialiser vos variables

# TODO: Sélectionner un mot aléatoire à faire deviner dans la liste des noms féminins

# TODO: Tant que le mot n'est pas deviné et qu'il reste des vies:

    # TODO: Afficher les lettres devinées à date
    # TODO: Demander à l'utilisateur de deviner une lettre

    # TODO: SI la lettre a déjà été essayée
        # TODO: Dire à l'utilisateur de recommencer

    # TODO: SINON S'il s'agit d'un bon essai
        # TODO: ajouter la lettre aux lettre essayées
        # TODO: Calculer le mot qu'il a deviné jusqu'à présent
        # TODO: Dire bravo à l'utilisateur et lui montrer le mot

    # TODO: SINON (c'est un mauvais essai)
        # TODO: ajouter la lettre aux lettre essayées
        # TODO: enlever une vie
        # TODO: dire à l'utilisateur il lui reste combien de vies


# TODO: En sortant de la boucle principale, SI l'utilisateur n'a plus de vies, c'est quil a perdu
# TODO: SINON il a gagné :)
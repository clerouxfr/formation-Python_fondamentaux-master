"""
Cecli est un module de fonctions utiles pour l'usage du terminal.
"""

def display_shows(shows:dict):
    """
    Affiche dans le terminal les informations d'une série. La série doit avoir
    un attribut `name` et un attribut `episodes` contenant des objets ayant
    eux-même un attribut `title`.

    :param shows: Dictionnaire dont les valeurs sont des objets série.
    """
    for show in shows.values():
        print("\n-----")
        print(show.name)
        for episode in show.episodes:
            print(f" - {episode.title}")

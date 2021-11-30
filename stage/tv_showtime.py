"""
Second exercice
Pour cet exercice, l’idéal est de créer un nouveau module.
Il me reste 7 épisodes de Big Bang Theory à regarder.
On va considérer que chaque épisode a une durée de 23 minutes.


Je souhaite savoir quelle sera la durée de ma soirée. Vous allez bien entendu écrire le
code pour calculer cela, mais pour afficher le résultat, vous allez utiliser des chaines de
caractères qui ont été préparées dans le module pylib.templating .
Importez ce module. Utilisez la constante TIME_REMAINING pour afficher cette durée.

Le module datasource contient une fonction get_start_time() qui retourne l’heure de
début de ma soirée. Utilisez cette valeur pour calculer l’heure de fin que vous afficherez
grâce à la constante END_HOUR du module templating .
Note : ces valeurs n’entraineront pas de changement de jour.
"""

import pylib.templating as pt
import pylib.datasource as pd
#  import stage.time_util as tu

SEASON_DURATION = 7 * 23  # 7 episodes de 23 min


def time_reformat(template, duration):
    return template.format(duration // 60, duration % 60)


print(time_reformat(pt.TIME_REMAINING, SEASON_DURATION))
print("Début du show TV : ", pd.get_start_time())

tuple_start_time = pd.get_start_time().split("h")
end_time_minutes = (int(tuple_start_time[0]) * 60 + int(tuple_start_time[1])) + SEASON_DURATION

print(time_reformat(pt.END_HOUR, end_time_minutes))














"""
movies_media = pd.get_movies()
for movies_media in movies_media:
    print(movies_media[0])
"""

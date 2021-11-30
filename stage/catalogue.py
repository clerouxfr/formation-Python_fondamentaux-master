import pylib.datasource as ds
from pprint import pprint

ds.bbt_s12 = ds.get_season()  # liste de chaines de caractères
#  pprint(ds.bbt_s12)
EPISODE_DURATION = 23
season_duration = int(len(ds.bbt_s12) * EPISODE_DURATION)
print("durée totale de a saison:", season_duration)

SHOW_TIME_MAX = 120
n_episode = int(SHOW_TIME_MAX // 23)
print("nombre d'épisode à visonner:", n_episode)
playlist = ds.bbt_s12.copy()  # .clear() permet de vider la liste
pprint(playlist)

print("episode visionné:", playlist.pop(0))
print("durée de la playlist:", len(playlist) * EPISODE_DURATION, len(ds.bbt_s12) * EPISODE_DURATION)

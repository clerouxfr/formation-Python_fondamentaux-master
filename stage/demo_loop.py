import pylib.datasource as ds
from pprint import pprint

"""vue pas vue spécifique au user"""

movies = ds.get_season("Christophe")

#  print(movies)
for index, (title, viewed, duration) in enumerate(movies):
    if not viewed:
        print(title)
        playlist = movies[index:]
        break
else:
    playlist = []

pprint(playlist)

print("**************")

time_left = 120

while playlist and time_left > playlist[0][2]:
    next_episode = playlist.pop(0)
    print(next_episode[0])
    next_episode[1] = True
    time_left -= next_episode[2]

pprint(time_left)
pprint(movies)


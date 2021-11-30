"""correction de l'exercice"""

import pylib.templating as tp
import pylib.datasource as ds
import stage.time_util as tu

EPISODE_DURATION = 23
episodes = 7

total_duration = episodes * EPISODE_DURATION
#  Prend deux nombres (non complexes)
#  et donne leur quotient et reste de leur division entière sous forme d’une paire de nombres.
#  duration_hours,  duration_minutes = divmod(total_duration, 60)

#  * permet de déballer le tuple _ packing / unpacking
print(tp.TIME_REMAINING.format(*divmod(total_duration, 60)))

#  start_hours, start_minutes = ds.get_start_time().split("h")
begin_hour = tu.to_minutes_(*ds.get_start_time().split("h"))  # idem, l'étoile permet de déballer la liste

print(tp.END_HOUR.format((begin_hour + total_duration) // 60, (begin_hour + total_duration) % 60))

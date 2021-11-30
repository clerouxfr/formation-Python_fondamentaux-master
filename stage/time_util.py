"""
Créez cette fonction qui prend un paramètre hours et affiche la durée en minutes.
Exécutez cette fonction avec différents paramètres (vous pouvez faire cet appel dans le
module).
Avez-vous essayé d’exécuter cette fonction avec le paramètre "20" ? Que se passe-t-il ?
Si le comportement est incohérent, corrigez la fonction.
"""


def convert_minutes(hours):
    pass  # mot clé pour eviter de planter pycharm lors de la phase de dev de la fonction


def to_minutes(hours, minutes=0):
    return int(hours) * 60 + int(minutes)


def to_minutes_2(hours, minutes=0):
    if hours >= 0 and minutes >= 0:
        value = int(hours) * 60 + int(minutes)
    else:
        value = "unexpected"
    return value


# version ternaire
def to_minutes_3(hours, minutes=0):
    value = int(hours) * 60 + int(minutes) if hours >= 0 and minutes >= 0 else " 😱 unexpected"
    return value

"""
print(to_minutes(1, minutes=30))
print(to_minutes(2))
print(to_minutes("2"))
print(to_minutes("2", minutes="45"))

print(to_minutes_2(-230))
print(to_minutes_3(-230))
"""
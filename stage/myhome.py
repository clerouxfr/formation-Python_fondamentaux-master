"""
Module de contrôle du confort à la maison… Ou plutôt, qui va le simuler.

Premier exercice
Nous allons écrire une fonction dans le but d’afficher le confort en fonction de la
température. Bien entendu, cette fonction n’affiche pas en elle même, elle retourne la
chaîne de caractères à afficher. Cette fonction prend donc en paramètre une température.
Si la température est supérieure à la température max ( T_MAX ), informez qu’il fait trop
chaud.
Si la température est inférieur à la température minimum, informez qu’il fait trop froid.
Sinon, informez que tout va bien.
Vérifiez que tout fonctionne avec différentes valeurs de température


Second exercice
Écrivez une fonction, similaire à la précédente, qui retourne il fait bon si la température
est comprise entre T_MIN et T_MAX ou il ne fait pas bon pour tous les autres cas.
Retour à notre fonction
Nous allons rendre notre fonction to_minutes plus intelligente. Elle ne devra faire les
calculs que pour les durées positives ou nulles. Modifiez la fonction pour lui attribuer ce
comportement.

"""

T_MAX = 26
T_MIN = 18


def confort(temp):
    if temp > T_MAX:
        value = "il fait trop chaud"
    elif temp < T_MIN:
        value = "il fait bon"
    else:
        value = "il fait froid"
    return value


def other_confort(temperature):
    if T_MIN <= int(temperature) <= T_MAX:
        status = "il fait bon"
    else:
        status = "il ne fait pas bon"
    return status


# version ternaire de la fonction ci-dessus
def other_confort_ter1(temperature):
    return "il fait bon" if T_MIN <= int(temperature) <= T_MAX else "il ne fait pas bon"


# version ternaire bis de la fonction ci-dessus
def other_confort_ter2(temperature):
    value = "il fait bon" if T_MIN <= int(temperature) <= T_MAX else "il ne fait pas bon"
    return value


# quand on ecrit is_it ... généralement on recupére vrai / faux
def is_it_ok(temperature):
    return T_MIN <= int(temperature) <= T_MAX


print(confort(10))
print(confort(19))
print(confort(29), "\n\n")
print(other_confort(10))
print(other_confort(19))
print(other_confort(31), "\n\n")

print(is_it_ok(10))
print(is_it_ok(19), "\n\n")

print(other_confort_ter1(25))
print(other_confort_ter2(5))
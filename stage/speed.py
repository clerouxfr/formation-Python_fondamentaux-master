"""
Premier exercice
Un petit calcul de vitesse. J’ai parcouru 19, 7 mètres en 6,892 secondes. Affichez la
vitesse avec son unité en imposant deux chiffres après le point décimal.
"""
speed = 19.7 / 6.892
print(f"speed is  {speed:.2f} m/s")

DISTANCE = 19.7
DURATION = 6.892

print("vitesse: {:.2f} m/S".format(DISTANCE / DURATION))

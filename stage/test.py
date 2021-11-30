camelot = ["Arthur", "Merlin", "Robin", "Karadoc", "Perceval"]
wizards = ["Mrlin", "Tim"]

print(camelot[:])
print(camelot[::-1])  # methode la plus efficace pour inverser une chaine de caractères
print(camelot)
print(camelot.append("Arthur"))
print(camelot.pop())
print(camelot)
print(camelot.insert(0, "Arthur"))
print(camelot)
print(camelot.extend(("toto", "titi", "riri")))
print(camelot)

i = 10


def ma_func(i):
    i += 1
    print(i)


ma_func(12)
print(i)

print("____________")


"""boucle for__else"""
for knight in camelot:
    if knight in wizards:
        break
else:
    print("you need a wizard")

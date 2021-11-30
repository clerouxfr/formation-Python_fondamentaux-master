"""
exo 1
"""

formation_days = 5
formation_hours = 7

print(formation_days)
print(formation_hours)


def training_duration(days, hours):
    return days * hours


print(training_duration(formation_days, formation_hours))

break_duration = 72
print (break_duration//60,"h",break_duration%60,"mn")
#built-in
print(divmod(break_duration, 60)) #built-in
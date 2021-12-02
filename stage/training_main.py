import stage.time_util as tu

training_duration = -12

try:
    print(f"La formation a une durée de {tu.to_minutes_4(training_duration)} minutes")
except ValueError as inst:
    # print(type(inst))    # the exception instance
    # print(inst.args)     # arguments stored in .args
    print(inst)

try:
    print(f"La formation a une durée de {tu.to_minutes_4(training_duration)} minutes")
except ValueError as err:
    # print(type(inst))    # the exception instance
    # print(inst.args)     # arguments stored in .args
    print(err)

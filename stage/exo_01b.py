import pylib.datasource as ds


def conversion_minutes():
    return int(ds.time_loader()) * 60


print(conversion_minutes())



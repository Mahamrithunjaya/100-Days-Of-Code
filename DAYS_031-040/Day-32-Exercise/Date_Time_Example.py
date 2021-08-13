import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1785, month=12, day=19, hour=8)
print(date_of_birth)

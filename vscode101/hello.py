def say_hello(name):
    print("Hello," + name)

say_hello("Alice")

def say_day_of_week(date):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date.weekday()
    print("Today is " + days_of_week[day_index])

import datetime
today = datetime.date.today()
say_day_of_week(today)
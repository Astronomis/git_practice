from datetime import datetime

birthday = datetime(1991, 2, 4, 4)
print(birthday)

print("Year:  " + str(birthday.year))
print("Month: " + str(birthday.month))
print("Day:   " + str(birthday.day))
print("Hour:  " + str(birthday.hour))

print(datetime.now() - birthday)

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date.month)

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
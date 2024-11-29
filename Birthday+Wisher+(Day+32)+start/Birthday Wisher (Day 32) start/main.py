import smtplib
import datetime as dt
import random

# now = dt.datetime.today()
# year = now.year
# if year == 2024:
#     print(year)
# day_of_week = now.weekday()
# print(day_of_week)
# # print(type(now))
# # print(type(year))
#
# date_of_birth = dt.datetime(year=1996, month=12, day=8)
# print(date_of_birth)

# obtain current day of the week
now = dt.datetime.today()
day_of_week = now.weekday()

if day_of_week == 0:
    # open the file and obtain list of quotes
    with open("quotes.txt") as file:
        data = file.read().splitlines()
        random_quote = random.choice(data)

    # Email to yourself
    my_email = "vedantpant.python@gmail.com"
    my_password = ("wgrkaapqmipwtkgu")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject:hey good morning\n\n" + random_quote
                            )
else:
    print("not working")


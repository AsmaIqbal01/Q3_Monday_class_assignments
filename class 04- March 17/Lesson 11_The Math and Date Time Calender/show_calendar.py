import calendar
from datetime import datetime

# 1. Show calendar for the current month
now = datetime.now()
year = now.year
month = now.month

print("📅 Calendar for current month: \n ")
print(calendar.month(year,month))

#2. show calendar for specific month/year
custom_year= 1999
custom_month = 7
print(f"📆 Calendar for {calendar.month_name[custom_month]} {custom_year}:\n")
print(calendar.month(custom_year,custom_month))

#3. show the full calendar for a given year
print("📖 Full Calendar - 2025:\n")
print(calendar.calendar(2025))
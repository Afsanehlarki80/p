import calendar

# Get year and month from user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Create a calendar object
cal = calendar.monthcalendar(year, month)

# Print the calendar
print("\n", calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day == 0:
            print("  ", end="")
        else:
            print(str(day).rjust(2), end=" ")
    print()
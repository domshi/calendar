# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a year: "))

# Get the year, then the month, then the day
# housekeeping()

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False
if int(month) == 4 or int(month) == 6 and int(day) > 30:
    validDate = False
if int(month) == 9 or int(month) == 11 and int(day) > 30:
    validDate = False
if int(month) == 2 and int(day) > 29:
    validDate = False
# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(str(month) + "/" + str(day) + "/" + str(year) + " is a valid date.")
else:
    print(str(month) + "/" + str(day) + "/" + str(year) + " is an invalid date")
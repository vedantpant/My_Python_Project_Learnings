#key,value pair
#three digit month name to full month name

MonthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(MonthConversion["Mar"])
#get -> specify default value
#if a key is not mappable to a certain value
print(MonthConversion.get("Luv", "Not a valid key"))
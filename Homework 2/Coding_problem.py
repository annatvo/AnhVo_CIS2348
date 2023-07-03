# Anh Vo
# 2037824
# Coding problem

import re

def is_date(date_str):
    # Check if the date string matches the required format
    check_month = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$"
    return re.match(check_month, date_str) is not None

def parse_date(date_str):
    month_dict = {"January": 1, "February": 2, "March": 3, "April": 4,
                  "May": 5, "June": 6, "July": 7, "August": 8, "September": 9,
                  "October": 10, "November": 11, "December": 12}

    # Extract the month, day, and year from the date string using find() method
    year = date_str[date_str.find(',') + 2:]
    month, day = date_str[: date_str.find(',')].split(" ")
    month = month_dict[month.title()]

    return '{}/{}/{}'.format(month, day, year)

def main():
    # Part B: Read dates from "inputDates.txt" file
    with open("inputDates.txt", 'r') as file:
        dates = [parse_date(date) for date in file if is_date(date)]

    # Part C: Write correct dates to "parsedDates.txt" file
    with open("parsedDates.txt", 'w') as file:
        file.write(''.join(dates))

if __name__ == "__main__":
    main()

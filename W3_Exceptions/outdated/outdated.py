# user inputs date in month-day-year order, either as 1/1/2025 or January 1, 2025
# I'll need to use .split() to assign month, day, year
# hint suggests I'll need to use list.index(x[, start[, end]])
# output user's date in format YYYY-MM-DD
# ignore invalid inputs
# invalid if day is >31


def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        user_date = input("Date: ").strip()
        valid = False  # I can use this further down to flag if the first version is correct or not

        # First checks if the input is in format "Month Day, Year" then splits
        for month_name in months:
            if user_date.startswith(month_name):
                try:
                    # Must require 1 comma after the day
                    if user_date.count(",") != 1:
                        continue

                    parts = user_date.replace(
                        ",", ""
                    ).split()  # replaces commas with nothing so September, 1 = September 1 (Then splits to become "September", "1")
                    if len(parts) != 3:  # this checks split created exactly 3 parts
                        continue

                    month_part, day_part, year_part = parts
                    month = (
                        months.index(month_part) + 1
                    )  # finds the index value of the month list item and adds 1 (since list starts at 0)
                    day = int(day_part)
                    year = int(year_part)

                    # Validate day
                    if not (1 <= day <= 31):
                        continue

                    valid = True
                    break

                except (ValueError, IndexError, AttributeError):
                    continue

            # If input wasn't in text format, try "MM/DD/YYYY" (e.g., "9/8/1636")
            if not valid:
                try:
                    # Must have exactly two slashes
                    if (
                        user_date.count("/") != 2
                    ):  # since it must have two slashes to be valid
                        continue

                    month, day, year = map(
                        int, user_date.split("/")
                    )  # map simply applies int to each month, day, year part

                    # Validate month and day
                    if not (1 <= month <= 12 and 1 <= day <= 31):
                        continue

                    valid = True

                except (ValueError, IndexError):
                    continue

        # If valid, print and exit
        if valid:
            print(f"{year}-{month:02}-{day:02}")
            break

        # Otherwise, silently reprompt


main()

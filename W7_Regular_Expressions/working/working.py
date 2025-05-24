"""
TASK: Convert 12h times to 24h times. Expect numbers in format either 9:00 AM or 9 AM and output as 09:00
9:00 AM to 5:00 PM > 09:00 to 17:00
9 AM to 5 PM > 09:00 to 17:00
"""
import re

def main():
    print(convert(input("Hours: ")))


def convert(str):
    # Strict regex (hours 1-12, minutes 00-59, AM/PM, also accepting inputs with no minutes "5 PM")
    pattern = r"^((1[0-2]|[1-9])(:([0-5][0-9]))?\s(AM|PM))\s+to\s+((1[0-2]|[1-9])(:([0-5][0-9]))?\s(AM|PM))$"
    match = re.match(pattern, str)

    if not match:
        raise ValueError

    # Extract components (group 2=hr1, group 3=min1, group 4=period1, group 6=hr2, group 7=min2, group 8=period2)
    h1 = match.group(2)
    m1 = match.group(4) or "00"
    period1 = match.group(5)

    h2 = match.group(7)
    m2 = match.group(9) or "00"
    period2 = match.group(10)

    # use to_24h function to convert regex components
    time1_24h = to_24h(h1, m1, period1)
    time2_24h = to_24h(h2, m2, period2)

    return f"{time1_24h} to {time2_24h}"

# Extra function to convert a single time to 24h, used within convert
def to_24h(hour_str, minute_str, period):
    hour = int(hour_str)
    if period == 'PM' and hour != 12: # because 12PM needs to be treated differently from other PMs
        hour += 12
    elif period == 'AM' and hour == 12: # deal with 12PM=0h edge case
        hour = 0
    return f"{hour:02d}:{minute_str}"


if __name__ == "__main__":
    main()

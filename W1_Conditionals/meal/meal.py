def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time) #refers to the below def where its converted to float value

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    # Converts to int and assigns to hours and mins at same time
    # map applies int to each item
    if minutes >= 60:
        raise ValueError("Invalid minutes.. max 59)")
    # Outputs error if user inputs invalid time
    return hours + minutes / 60
    # Converts to float (e.g., 7:30 is 7.5)

if __name__ == "__main__":
    main()

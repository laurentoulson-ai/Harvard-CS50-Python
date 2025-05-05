# Keep prompting user for items and print ongoing total after each input
# Input is title cased
# Add dollar sign to output
# Only exits when user uses ctrl D
# Ignore inputs that aren't on list

def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    ordered = 0

    while True:
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                new_total = ordered + menu[item]
                ordered = new_total # This means original 'ordered' value gets updated each time
                print(f"${ordered:.2f}") #.2f makes to 2 decimal places
        except ValueError:
            pass  # Ignore inputs not in list

        except EOFError: # Catch when user inputs ctrl D
            print("\n") # If I don't do this then it exits programme on same line as Item:
            break
main()

# prompt names until user ctrl D
# then return "Adieu, adieu, to" + (names)
# if >1 name, append 'and ' to the last name
# if 3 or more names, separate names by commas

import inflect


def main():

    p = inflect.engine()  # initiating inflect

    names = []  # create empty list to store names

    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)  # adds new name to the list

        except EOFError:  # Catch when user inputs ctrl D
            print()  # If I don't do this then it exits programme on same line
            break

    if names:  # Only joins if there are names
        inflected = p.join(names)
        print(f"Adieu, adieu, to {inflected}")


main()

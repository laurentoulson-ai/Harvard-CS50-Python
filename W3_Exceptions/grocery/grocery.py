# Prompt user for grocery items until ctrl D
    # Append in a list
    # Catch cases where its sometimes capitalised / has spaces with .strip().lower()
# After ctrl D, print all items in uppercase
    # Items should be printed alphabetically
    # It should print how many times that item is in the list

def main():
    shopping_list = []
    counted_list = {}

    while True:
        try:
            item = input().strip().upper() # ensures it'll print out in uppercase
            shopping_list.append(item) # adds item to my list
            counted_list[item] = shopping_list.count(item) # counts items and stores as values in my dict

        except EOFError: # Catch when user inputs ctrl D
                print("\n") # If I don't do this then it exits programme on same line
                break

    alphabetical_list = sorted(counted_list.keys()) # sorts keys into alphabetical order

    for item in alphabetical_list: # iterates over my keys and values then prints each out
        print(f"{counted_list[item]} {item}")

main()

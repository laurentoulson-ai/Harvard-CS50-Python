def main():
    calories = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pineapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80",
    }
    user_input = input("Item: ").strip().title() # Converts to title case to match dictionary keys

    if user_input in calories:
        print(f"Calories: {calories[user_input]}") # Makes sure to match input to dictionary key

# Could add an else to print if fruit not found, but test just wanted no return in this instance
main()



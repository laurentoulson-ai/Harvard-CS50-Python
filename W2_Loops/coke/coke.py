def main():
    coke_price = 50
    amount_paid = 0

    while amount_paid < coke_price:
        # Always show current amount due first and returns amount due even if input is not in list
        print(f"Amount Due: {coke_price - amount_paid}")

        coin_input = input("Insert coin: ") # asks for coins every time, loops if < coke_price

        try:
            coin = int(coin_input) # converts to int
            if coin in [25, 10, 5]: # specifies in list which are valid
                amount_paid += coin  # Only deduct valid coins
            # Invalid coins fall through to show Amount Due again
        except ValueError:
            pass  # Ignore non-integer inputs

        # Loop will automatically show Amount Due again

    print(f"Change Owed: {amount_paid - coke_price}")

if __name__ == "__main__":
    main()

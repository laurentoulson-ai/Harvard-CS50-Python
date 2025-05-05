# TASK
# User inputs number of bitcoins via command line argument (bitcoin.py 2)
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message
    # "python bitcoin.py" = 'Missing command-line argument'
    # "python bitcoin.py cat" = 'Command-line argument not a number'
# Queries the API for the CoinCap Bitcoin Price Index
# returns a JSON object, among whose nested keys is the current price of Bitcoin as a float
# Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator ($38,761.0833)

import requests
import sys


def main():
    API_KEY = # OMMITTED FOR SECURITY
    url = "https://rest.coincap.io/v3/assets/bitcoin"

    try:
        # Fetch Bitcoin price - Pass API key as URL parameter
        response = requests.get(f"{url}?apiKey={API_KEY}")

        # Raise error if request fails
        response.raise_for_status()

        # assigning json data from api to value
        data = response.json()

        # Extract price
        bitcoin_price = float(data["data"]["priceUsd"])

        # Purchase calculation
        purchase_amount = get_input()
        total_cost = purchase_amount * bitcoin_price
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        ...


def get_input():

    # exits if user didn't input an argument
    if len(sys.argv) <= 1:
        print("Missing command-line argument")
        sys.exit(1)

    user_input = sys.argv[1]

    try:
        # Try converting to float, otherwise except ValueError if not number
        user_float = float(user_input)

        # Validate positive number
        if user_float <= 0:
            print("Amount must be greater than 0")
            sys.exit(1)

        # if all is good
        return user_float

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


if __name__ == "__main__":
    main()

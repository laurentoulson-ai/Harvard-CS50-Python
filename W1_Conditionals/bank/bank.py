# Prompt the user to input greeting

greeting = input("What's your greeting? ").lower().strip(" ,.!?")

# If the user inputs any greeting that starts with hello, return $0

if greeting.startswith("hello"):
    print("$0")

# If the inputs any greeting that starts with h, but not hello, return $20

elif greeting.startswith("h"): # elif here specifically means it only runs if it wasn't hello, otherwise hello also starts with h and would return $20
    print("$20")

# Otherwise, return $100

else:
    print("$100")

# other notes
# Ignore any leading whitespace in the user’s greeting
# Treat the user’s greeting case-insensitively
# Test: Hello (0), Hello Newman (0), How you doing? (20), What's happening? (100)

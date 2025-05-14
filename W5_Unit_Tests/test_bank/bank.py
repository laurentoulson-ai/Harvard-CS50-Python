# TASK
# Reimplement W1 bank.py programme
# Restructure code within new def structure
# Use test_bank.py to test bank.py

def main():
    greeting = input("What's your greeting? ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0 # This CS50 exercise expects int values not strings, so 0 here instead of previous programme "$0"
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

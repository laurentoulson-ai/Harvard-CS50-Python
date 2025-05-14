# TASK
# Reimplement W2 twttr.py programme
# Restructure code within new def shorten(word)
    # Does the same - shorten expects a string input and returns string without vowels
# Use test_twttr.py to implement one or more functions that collectively test your implementation of shorten thoroughly
# Take care to return, not print, a str in shorten. Only main should call print

def main():
    word = shorten(input("Input: "))
    print(word.strip())

def shorten(word):
    vowels = [
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"] # stores vowels in list

    for vowel in vowels:
        word = word.replace(vowel, "")  # removes the vowels
    return word

if __name__ == "__main__":
    main()

import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    # get fonts outside of if statements so it can be accessed by all the blocks
    available_fonts = figlet.getFonts()

    # If user wants to specify font they'll be using 3 arguments, such as figlet.py -f slant
    if len(sys.argv) == 3:

        # Assign arguments to argv inputs
        option = sys.argv[1]
        font_name = sys.argv[2]

        # Validate argv[1] is valid input
        if option not in ["-f", "--font"]:
            print("First argument must be -f or --font")
            sys.exit(1)

        # reject if argv[2] font not valid
        if font_name not in available_fonts:
            print(f"Font '{font_name}' not available. Choose from:")

            #print out font options if error
            print(", ".join(available_fonts))
            sys.exit(1)

        # If input correct, set font and process input
        figlet.setFont(font=font_name)
        request_word = input("Input: ")

        print("Output: " + figlet.renderText(request_word))

    # If user doesn't specify font, return input in random font
    elif len(sys.argv) == 1:

        user_word = input("Input: ")

        random_font = random.choice(available_fonts)  # Pick a random font
        figlet.setFont(font=random_font)

        print("Output: " + figlet.renderText(user_word))

    else:
        print("Invalid number of arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()

# TASK
# Summary: Resize and overlay shirt.png onto a posed image to virtually try on CS50 shirt
# sys.argv[1] = the name (or path) of a JPEG or PNG to read (i.e., open) as input
# sys.argv[2] = the name (or path) of a JPEG or PNG to write (i.e., save) as output
# resize and crop shirt.png to match the size of the posed image
# overlay resized image onto new output

from PIL import Image, ImageOps
import sys

def main():
    input_file, output_file = validate_arguments()
    resize_and_overlay(input_file, output_file)

def validate_arguments(): # Validates command line arguments and return filenames

    # assign name to user input
    input_file, output_file = sys.argv[1], sys.argv[2]

    # exit if user does not specify exactly two command-line arguments
    # note: could be done shorter as '!= 3' but CS50 wants two different print statements
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # split and check extensions
    input_ext = input_file.split(".")[1]
    output_ext = output_file.split(".")[1]
    valid_extensions = {'jpg', 'jpeg', 'png'}
    # exit if input’s and output’s names do not end in .jpg, .jpeg, or .png
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid file type. Use .jpg, .jpeg, or .png")
    # exit if the input’s name does not have the same extension as the output’s name
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    return input_file, output_file

def resize_and_overlay(input_file, output_file):
    try:
        # Open images
        with Image.open(input_file) as input_img, Image.open("shirt.png") as shirt:
            # Resize input to match shirt size
            resized_input = ImageOps.fit(input_img, shirt.size)

            # Paste shirt onto resized input
            resized_input.paste(shirt, (0, 0), shirt)  # using shirt as mask

            # Save result
            resized_input.save(output_file)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

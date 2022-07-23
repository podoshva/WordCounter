def get_filename():  # Define the function;
    """This function requests the file name."""

    print("\nEnter 'q' to end the program.")
    file_name = input('Enter the text file name: ')
    if file_name == 'q':  # If the user entered 'q', then terminate the program;
        quit()
    else:
        return file_name
        checking_file()


def get_word():  # Define the function;
    """This function requests the word."""

    word = input('Enter the word: ')
    if word == 'q':  # # If the user entered 'q', then terminate the program;
        quit()
    else:
        return word
        count_words()


def checking_file():  # Define the function;
    """This function checks if there is a file in the directory."""

    file_name = get_filename()
    try:
        file_name = file_name + '.txt'  # Add the '.txt' extension to the end of the file name;
        with open(file_name) as f:  # Open the file;
            f.read()
    except FileNotFoundError:  # If the file is not in the directory, an error message is displayed;
        print(f"File named '{file_name}' is not found.")
    else:
        return file_name


def count_words():  # Define the function;
    """This function counts how many times the word appears in the text."""

    file_name = checking_file()
    if file_name:  # Checking if the value matches
        word = get_word()
        with open(file_name) as f:  # Open the file;
            content = f.read()  # Read the file and place it in a variable;
        word_count = content.lower().count(word)  # Word counting
        print(f"\tThe word '{word}' appears {word_count} times in the text.")
    else:
        count_words()


while True:  # Starting the cycle
    count_words()

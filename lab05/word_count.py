def word_count1():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Can't open {file_name}")
        return  # Exit the function gracefully

    # Split by whitespace to count words
    words = content.split()
    word_count = len(words)

    # Count all characters (including punctuation and whitespace)
    char_count = len(content)

    # Remove all non-alphanumeric characters by replacing them
    alphanumeric_content = content.replace(" ", "")  # Remove spaces
    # Add more replacements for common punctuation and symbols
    for symbol in [
        ".",
        ",",
        "!",
        "?",
        "-",
        "_",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        '"',
        "'",
        ":",
        ";",
        "/",
        "\\",
        "\n",
        "\t",
    ]:
        alphanumeric_content = alphanumeric_content.replace(symbol, "")

    # The length of the cleaned content will give the number of letters and numbers
    alphanumeric_count = len(alphanumeric_content)

    # Print the results
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    print(f"Letters & numbers: {alphanumeric_count}")


word_count1()

# regex version
import re


def word_count2():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as file:
            content = file.read()  # Read the entire file content
    except FileNotFoundError:
        print(f"Can't open {file_name}")
        return  # Exit the function if the file can't be found

    # Count words by splitting the content by whitespace
    words = content.split()
    word_count = len(words)

    # Count all characters (including punctuation and spaces)
    char_count = len(content)

    # Use regex to find all alphanumeric characters
    alphanumeric_chars = re.findall(r"\w", content)  # Matches letters and numbers
    alphanumeric_count = len(
        alphanumeric_chars
    )  # Count the length of the found characters

    # Print results
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
    print(f"Letters & numbers: {alphanumeric_count}")


word_count2()

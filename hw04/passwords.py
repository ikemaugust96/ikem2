import random


# Function to create a username
def cusername(first_name, last_name):
    # Get the first letter of the first name
    first_initial = first_name[0].lower()

    # Pad the last name with * if it's less than 7 characters, then take the first 7 characters
    padded_last_name = (last_name + "*******")[:7].lower()

    # Append a random number between 0 and 99
    random_number = random.randint(0, 99)

    # Combine all parts into the username
    username = f"{first_initial}{padded_last_name}*{random_number}"

    return username


# Function to create Password 1: First name, last name with replacements
def cpassword1(first_name, last_name):
    # Concatenate first and last names in lowercase
    password1 = f"{first_name.lower()}{last_name.lower()}"

    # Insert a random number between 0 and 99 in the middle
    random_number = random.randint(0, 99)
    password1 = f"{first_name.lower()}{random_number}{last_name.lower()}"

    # Replace specific letters with similar-looking symbols
    replacements = {"a": "@", "o": "0", "l": "1", "s": "$"}

    # Replace the characters in the string
    for key, value in replacements.items():
        password1 = password1.replace(key, value)

    return password1


# Function to create Password 2: Acronym-style password
def cpassword2(first_name, last_name, favorite_word):
    # First and last character of first name (lower, upper)
    part1 = first_name[0].lower() + first_name[-1].upper()

    # First and last character of last name (lower, upper)
    part2 = last_name[0].lower() + last_name[-1].upper()

    # First and last character of favorite word (lower, upper)
    part3 = favorite_word[0].lower() + favorite_word[-1].upper()

    # Combine all parts together
    password2 = part1 + part2 + part3

    return password2


# Function to create Password 3: Random segments of first name, last name, and favorite word
def cpassword3(first_name, last_name, favorite_word):
    # Generate random lengths for each part (at least 1 character from each)
    len_first = random.randint(1, len(first_name))
    len_last = random.randint(1, len(last_name))
    len_fav = random.randint(1, len(favorite_word))

    # Take the random portions from each string
    part1 = first_name[:len_first]
    part2 = last_name[:len_last]
    part3 = favorite_word[:len_fav]

    # Shuffle the order of the parts randomly
    parts = [part1, part2, part3]
    random.shuffle(parts)

    # Combine the shuffled parts into a password
    password3 = "".join(parts)

    return password3


def main():
    print("Welcome to the username and password generator!")

    # Collect user inputs: first name, last name, and favorite word
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    favorite_word = input("Please enter your favorite word: ")

    # Username creation:
    # The username consists of the first letter of the first name,
    # first 7 letters of the last name (padded with * if needed), and a random number.
    username = cusername(first_name, last_name)
    print(f"\nThanks {first_name}, your user name is {username}")

    # Generate the three passwords
    print("\nHere are three suggested passwords for you to consider:")

    # Password 1: Replace letters with symbols and numbers
    password1 = cpassword1(first_name, last_name)
    print(f"Password 1: {password1}")

    # Password 2: Acronym-based password
    password2 = cpassword2(first_name, last_name, favorite_word)
    print(f"Password 2: {password2}")

    # Password 3: Random portion from each input (first name, last name, favorite word)
    password3 = cpassword3(first_name, last_name, favorite_word)
    print(f"Password 3: {password3}")


if __name__ == "__main__":
    main()

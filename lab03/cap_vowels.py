def cap_vowels():
    # Get user input
    user_input = input("Enter a phrase: ")

    # Initialize an empty result string
    result = ""

    # Define vowels
    vowels = "aeiouAEIOU"

    # Iterate through each character in the input
    for char in user_input:
        if char in vowels:
            result += char.upper()  # Uppercase for vowels
        else:
            result += char.lower()  # Lowercase for consonants

    # Print the result
    print(result)


# Run the function
cap_vowels()

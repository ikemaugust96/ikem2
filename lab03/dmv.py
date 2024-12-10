import random


def generate_license():
    # Welcome words
    print("Welcome to the DMV (estimated wait time is 3 hours)")

    #  the user's name
    full_name = input("Please enter your first, middle, and last name:\n")
    first_name, middle_name, last_name = full_name.split()

    #  the user's date of birth
    dob = input("Enter date of birth (MM/DD/YY):\n")

    # Split the date of birth to extract month, day, and year
    month, day, year = dob.split("/")

    # Generate a random 7-digit driver's license number
    dl_number = random.randint(0, 9999999)
    dl_number_output = f"{dl_number:07}"

    # using the same month and day, but year remains 2021
    exp_year = "21"
    expiration_date = f"{month}/{day}/{exp_year}"

    # Display
    print("Washington Driver License")
    print(f"DL {dl_number_output}")
    print(f"LN {last_name}")
    print(f"FN {first_name} {middle_name}")
    print(f"DOB {dob}")
    print(f"EXP {expiration_date}")


# Run the program
generate_license()

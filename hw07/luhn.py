def luhn_check(account_number):
    # Reverse the account number string and convert to a list of integers
    digits = [int(d) for d in str(account_number)][::-1]

    # Apply Luhn's algorithm
    total_sum = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            # Double every second digit from the right (i.e., every odd index in reversed list)
            doubled_digit = digit * 2
            # If the result is two digits, subtract 9 instead of adding the digits
            if doubled_digit > 9:
                doubled_digit_ones = doubled_digit - 10
                doubled_digit_tens = 1
                new_doubled_digit = doubled_digit_ones + doubled_digit_tens
                total_sum += new_doubled_digit
            else:
                total_sum += doubled_digit
        else:
            # Add the digit as it is for every other digit
            total_sum += digit

    # If the total sum is divisible by 10, the account number is valid
    return total_sum % 10 == 0


def main():
    # Prompt the user for an account number
    account_number = input("Enter the account number: ")

    # Validate the account number
    if luhn_check(account_number):
        print("The account number is valid.")
    else:
        print("The account number is not valid.")


if __name__ == "__main__":
    main()

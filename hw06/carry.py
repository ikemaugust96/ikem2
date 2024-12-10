def validate_input(num1, num2):
    while True:
        try:
            valid_int1 = int(num1)
            if valid_int1 > 0:
                break

            else:
                print("Please provide a positive integer for the first number.")
            return None, None
        except ValueError:
            print("Please provide a positive integer for the first number.")
            return None, None

    while True:
        try:
            valid_int2 = int(num2)
            if valid_int2 > 0:
                break
            else:
                print("Please provide a positive integer for the first number.")
            return None, None
        except ValueError:
            print("Please provide a positive integer for the second number.")
            return None, None

    return valid_int1, valid_int2


def add_up(int1, int2):
    final_sum = int1 + int2
    return final_sum


def add_with_carries(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    max_length = max(len(num1), len(num2))
    carry = 0
    carry_count = 0

    for i in range(max_length):
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i]) if i < len(num2) else 0
        column_sum = digit1 + digit2 + carry
        if column_sum >= 10:
            carry = column_sum // 10
            carry_count += 1
        else:
            carry = 0

    return carry_count


def main():
    num1 = input("Please enter your first number: ")
    num2 = input("Please enter your second number: ")
    valid_int1, valid_int2 = validate_input(num1, num2)

    if valid_int1 is None:
        num1 = input("Please enter a valid first number: ")
    if valid_int2 is None:
        num2 = input("Please enter a valid second number: ")

    final_sum = add_up(valid_int1, valid_int2)
    carry_count = add_with_carries(num1, num2)
    print(f"{num1} + {num2} = {final_sum}")
    print(f"Number of carries: {carry_count}")


main()

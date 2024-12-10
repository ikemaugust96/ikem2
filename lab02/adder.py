def main():
    # the program will calculate the sum first
    first_value = float(input("Please input first number: "))
    second_value = float(input("Please input second number: "))
    sum = first_value + second_value
    print(sum)
    string1 = str("The sum of ")
    string2 = str(first_value)
    string3 = str("+")
    string4 = str(second_value)
    string5 = str("=")
    string6 = str(sum)
    print(string1 + string2 + string3 + string4 + string5 + string6)


main()

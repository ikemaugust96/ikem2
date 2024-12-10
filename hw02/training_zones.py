def main():
    # get the name and resting heart rate from the user
    age = input("Please enter your age:")
    resting_heart_rate = input("please enter your resting_heart_rate:")
    # calculate the heart rate reserve
    reserve = 208 - 0.7 * float(age) - float(resting_heart_rate)
    # calculate the starting number of each zone and the last number of zone5
    value_1 = round(float(resting_heart_rate) + 0.5 * float(reserve), 2)
    value_2 = round(float(resting_heart_rate) + 0.6 * float(reserve), 2)
    value_3 = round(float(resting_heart_rate) + 0.7 * float(reserve), 2)
    value_4 = round(float(resting_heart_rate) + 0.8 * float(reserve), 2)
    value_5 = round(float(resting_heart_rate) + 0.93 * float(reserve), 2)
    value_6 = round(float(resting_heart_rate) + float(reserve), 2)
    # print out reserve
    print(f"\nYour heart rate reserve is:{round(reserve, 2)} bpm")
    # print out zones
    print("Here is a breakdown of your training zones:")
    print(f"Zone1:{value_1} to {round(value_2 - 0.01, 2)} bpm")
    print(f"Zone2:{value_2} to {round(value_3 - 0.01, 2)} bpm")
    print(f"Zone3:{value_3} to {round(value_4 - 0.01, 2)} bpm")
    print(f"Zone4:{value_4} to {round(value_5 - 0.01, 2)} bpm")
    print(f"Zone5:{value_5} to {value_6} bpm")


main()

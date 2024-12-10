def swap1():
    x1 = input("first word:")
    x2 = input("second word:")
    x1, x2 = x2, x1
    print(f"""
 "The first word is {x1}. "
 "The second word is {x2}."
 """)


swap1()


def swap2():
    x1 = "love"
    x2 = "hate"
    x1, x2 = x2, x1
    print(f"""
 "The first word is {x1}. "
 "The second word is {x2}."
 """)


swap2()
# Function to ask Yes/No questions
def ask_question(question):
    response = input(question + " (Yes/No): ").lower()
    return response == "yes"


# Specific diagnostic
def more_possibilities():
    if ask_question("Do you have aching bones or aching joints?"):
        print("Possibilities include viral infection.")
    elif ask_question("Do you have a rash?"):
        print("Insufficient information to list possibilities.")
    elif ask_question("Do you have a sore throat?"):
        print("Possibilities include a throat infection.")
    elif ask_question("Are you vomiting or had diarrhea?"):
        print("Possibilities include digestive tract infection.")
    elif ask_question(
        "Do you have back pain just above the waist with chills and fever?"
    ):
        print("Possibilities include kidney infection.")
    elif ask_question("Do you have pain urinating or are urinating more often?"):
        print("Possibilities include a urinary tract infection.")
    elif ask_question("Have you spent the day in the sun or in hot conditions?"):
        print("Possibilities include sunstroke or heat exhaustion.")
    else:
        print("Insufficient information to list possibilities.")


# Meningitis-specific diagnostic
def check_for_meningitis():
    if ask_question(
        "Are you experiencing any of the following: pain when bending your head forward, nausea or vomiting, bright light hurting your eyes, drowsiness or confusion?"
    ):
        print("Possibilities include meningitis.")
    else:
        more_possibilities()


# Main fever diagnostic function
def diagnose_fever():
    if ask_question("Are you coughing?"):
        if ask_question("Are you short of breath or wheezing or coughing up phlegm?"):
            print("Possibilities include pneumonia or infection of airways.")
        elif ask_question("Do you have a headache?"):
            print("Possibilities include viral infection.")

    elif ask_question("Do you have a headache?"):
        check_for_meningitis()
    else:
        more_possibilities()


# Run the expert system
diagnose_fever()

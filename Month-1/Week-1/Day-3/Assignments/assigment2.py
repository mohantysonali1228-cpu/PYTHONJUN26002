def check_vote_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

age = int(input("Enter your age: "))
print(check_vote_eligibility(age))

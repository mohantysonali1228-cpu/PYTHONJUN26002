
def check_vote_eligibility(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

# Example
check_vote_eligibility(20)
check_vote_eligibility(16)
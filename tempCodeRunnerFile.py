def check_voting_eligibility(age):
    if age >= 18:
        print("eligible to vote")
    else:
        print("not eligible to vote")

for i in range(3):  # Checks eligibility for 3 people
    age = int(input("Enter age: "))
    check_voting_eligibility(age)

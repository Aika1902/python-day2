age = int(input("Enter your age: "))
if age >= 18:
    print("You are ready to vote")
elif age < 18 and age >= 16:
    print("You are ready to get drivers license")
else:
    print("You are not ready to vote or get drivers license")
    
# Password Strength Checker
# Checks the strength of a password based on 5 criteria

is_lower = False
is_Upper = False
is_digit = False
is_specialChar = False
score = 0

print("Welcome to Password Strength Checker")
password = input("Enter Your password please: ")

# Check each character in the password
for letter in password:
    if letter.islower():
        is_lower = True
    elif letter.isupper():
        is_Upper = True
    elif letter.isdigit():
        is_digit = True
    elif not letter.isalpha() and not letter.isdigit():
        is_specialChar = True

# Add 1 to score for each criteria met
if is_lower:
    score += 1
if is_Upper:
    score += 1
if is_digit:
    score += 1
if is_specialChar:
    score += 1
if len(password) >= 8:
    score += 1

# Display strength based on final score
if score == 5:
    print("Your Password is Very Strong")
elif score == 4:
    print("Your Password is Strong")
elif score == 3:
    print("Your Password is Moderate")
elif score == 2:
    print("Your Password is Weak")
elif score == 1:
    print("Your Password is Very Weak")
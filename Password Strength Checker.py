import re

def check_password_strength(password):
    strength = 0
    
    # Length of the password
    if len(password) >= 8:
        strength += 1
    
    # Presence of lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Presence of uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Presence of digits
    if re.search(r'[0-9]', password):
        strength += 1
    
    # Presence of special characters
    if re.search(r'[\W_]', password):
        strength += 1
    
    # Strength evaluation
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Input from user
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"The strength of the password is: {strength}")

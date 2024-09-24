import re

def check_password_strength(password):
    min_length = 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    length_ok = len(password) >= min_length
    
    strength = 'Weak'
    if length_ok and has_uppercase and has_lowercase and has_number and has_special:
        strength = 'Very Strong'
    elif length_ok and has_uppercase and has_lowercase and (has_number or has_special):
        strength = 'Strong'
    elif length_ok and (has_uppercase or has_lowercase) and (has_number or has_special):
        strength = 'Moderate'
    elif length_ok:
        strength = 'Weak'
    
    return strength, length_ok, has_uppercase, has_lowercase, has_number, has_special

def suggest_improvements(password):
    """Suggest improvements for weak passwords."""
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Add at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        suggestions.append("Add at least one lowercase letter.")
    if not re.search(r'\d', password):
        suggestions.append("Include at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character (e.g., @, #, $, etc.).")
    if len(suggestions) == 0:
        suggestions.append("Your password is strong!")
    return suggestions

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")

    strength, length_ok, has_uppercase, has_lowercase, has_number, has_special = check_password_strength(password)
    
    print("\nPassword Assessment:")
    print(f"Password Length Valid: {'Yes' if length_ok else 'No'}")
    print(f"Contains Uppercase Letters: {'Yes' if has_uppercase else 'No'}")
    print(f"Contains Lowercase Letters: {'Yes' if has_lowercase else 'No'}")
    print(f"Contains Numbers: {'Yes' if has_number else 'No'}")
    print(f"Contains Special Characters: {'Yes' if has_special else 'No'}")
    print(f"Overall Strength: {strength}")
    
    if strength == 'Weak' or strength == 'Moderate':
        print("\nSuggestions to Improve Password Strength:")
        for suggestion in suggest_improvements(password):
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()

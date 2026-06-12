from collections import Counter

total_passwords = 15

strong_count = 0
medium_count = 0
weak_count = 0

for i in range(total_passwords):
    print(f"\nEnter Password {i+1}: ")
    password = input()

    upper = 0
    lower = 0
    digits = 0
    special = 0
    vowels = 0
    consonants = 0

    for ch in password:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        elif not ch.isalnum() and ch != " ":
            special += 1

        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    length_ok = len(password) >= 8
    has_space = " " in password

    # Password Strength
    if length_ok and upper > 0 and lower > 0 and digits > 0 and special > 0:
        strength = "Strong"
        strong_count += 1
    elif length_ok and ((upper > 0 or lower > 0) and digits > 0):
        strength = "Medium"
        medium_count += 1
    else:
        strength = "Weak"
        weak_count += 1

    # Repeated Characters
    repeated = []
    freq = Counter(password)

    for char, count in freq.items():
        if count > 1:
            repeated.append(char)

    # Most Frequent Character
    most_char = max(freq, key=freq.get)

    print("\n----- Password Analysis -----")
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)
    print("Digits:", digits)
    print("Special Characters:", special)
    print("Minimum Length (8):", length_ok)
    print("Contains Spaces:", has_space)
    print("Password Strength:", strength)
    print("Repeated Characters:", repeated if repeated else "None")
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Most Frequent Character:", most_char)

print("\n========== SECURITY REPORT ==========")
print("Total Passwords Analyzed:", total_passwords)
print("Strong Passwords:", strong_count)
print("Medium Passwords:", medium_count)
print("Weak Passwords:", weak_count)
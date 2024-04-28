import random
import string

def generate_password(lengths):
    passwords = []
    for length in lengths:
        password = ''.join(random.choices(string.ascii_lowercase, k=length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    return passwords

def replace_with_number(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randint(len(password) // 2, len(password) - 1)
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def get_password_lengths(num_passwords):
    print("Minimum length of password should be 3")
    lengths = []
    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        lengths.append(max(length, 3))
    return lengths

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    password_lengths = get_password_lengths(num_passwords)
    passwords = generate_password(password_lengths)
    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i} = {password}")

if __name__ == "__main__":
    main()

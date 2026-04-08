import random
import string


def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    categories = {
        "uc": string.ascii_uppercase,
        "lc": string.ascii_lowercase,
        "num": string.digits,
        "spc": "!@#$%^&*()-_=+"
    }

    password_chars = [
        random.choice(categories["uc"]),
        random.choice(categories["lc"]),
        random.choice(categories["num"]),
        random.choice(categories["spc"])
    ]

    for _ in range(length - len(password_chars)):
        char_type = random.choice(list(categories.keys()))
        password_chars.append(random.choice(categories[char_type]))

    random.shuffle(password_chars)
    return "".join(password_chars)

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8, or 0 to exit): "))
            print()

            if length == 0:
                return 0
            elif length >= 8:
                return length

            print("Password must be at least 8 characters long.")
            print()
            # print("=" * 100)
            # print()

        except ValueError:
            print("Please enter a whole number.")
            print()
            # print("=" * 100)
            # print()


if __name__ == "__main__":
    while True:
        length = get_password_length()
        if length == 0:
            print("Exiting program.")
            break

        password = generate_password(length)
        print(f"Generated password: {password}")
        print()
        print("=" * 100)
        print()

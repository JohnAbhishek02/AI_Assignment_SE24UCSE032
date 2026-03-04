
import random
import string

def generate_captcha(length=5):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def captcha_test():
    captcha = generate_captcha()
    print("CAPTCHA:", captcha)

    user_input = input("Enter the CAPTCHA: ")

    if user_input == captcha:
        print("Verification successful. Access granted.")
    else:
        print("Verification failed. Try again.")

if __name__ == "__main__":
    captcha_test()

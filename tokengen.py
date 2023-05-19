#A simple ascending ordered token genetator
# queue = []
#
# def generate_token():
#     if not queue:
#         # If the queue is empty, assign the first token as 1
#         return 1
#     else:
#         # Otherwise, assign the next token as the last token in the queue plus 1
#         last_token = queue[-1]
#         return last_token + 1
#
# #
# def print_next_token():
#     if not queue:
#         # If the queue is empty, print a message saying so
#         print("There are no more tokens in the queue.")
#     else:
#         # Otherwise, print the next token in the queue
#         print(f"Next token: {queue[0]}")
#
# # Define a function to add a new token to the queue
# def add_token():
#     token = generate_token()
#     queue.append(token)
#     print(f"Token {token} added to the queue.")
#
# # Define a function to remove the next token from the queue
# def remove_token():
#     if not queue:
#         # If the queue is empty, print a message saying so
#         print("There are no more tokens in the queue.")
#     else:
#         # Otherwise, remove the next token from the queue and print a message saying so
#         token = queue.pop(0)
#         print(f"Token {token} removed from the queue.")
#
# # Define a function to display the current queue
# def display_queue():
#     if not queue:
#         # If the queue is empty, print a message saying so
#         print("The queue is currently empty.")
#     else:
#         # Otherwise, print the current queue
#         print("Current queue:")
#         for token in queue:
#             print(token)
#
# if __name__ == "__main__":
#     while True:
#         print("1. Print next token")
#         print("2. Add new token")
#         print("3. Remove next token")
#         print("4. Display current queue")
#         print("5. Exit")
#
#         choice = input("\nEnter your choice: ")
#
#         if choice == "1":
#             print_next_token()
#         elif choice == "2":
#             add_token()
#         elif choice == "3":
#             remove_token()
#         elif choice == "4":
#             display_queue()
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#simple otp generator and verification
##import random as r
#import math
#import pyotp
import time


def generate_otp():

    digits = "0123456789"
    otp = ""
    #interval = 60
    # secret = pyotp.random_base32()
    # otp = pyotp.TOTP(secret)
    # otp.now()
    #otp = pyotp.TOTP(secret, interval=3600)


    for i in range(3):
        otp += digits[math.floor(r.random() * 10)]

    return otp

    user = int(input('Enter the OTP: '))
    if otp==user:
        print('Access granted')
    else:
        print('Access Denied!')


if __name__ == '__main__':
    print("Your three digit OTP is : ", generate_otp())


# token generator with OTP
import random

# Define a queue to store tokens
queue = []

# Define a dictionary to store OTPs for each token
otps = {}

# Define a function to generate a new token
def generate_token():
    if not queue:
        # If the queue is empty, assign the first token as 1
        return 1
    else:
        # Otherwise, assign the next token as the last token in the queue plus 1
        last_token = queue[-1]
        return last_token + 1

# Define a function to generate an OTP for a given token
def generate_otp(token):
    otp = random.randint(100000, 999999)
    otps[token] = otp
    print(otp)
    return otp

# Define a function to print the next token
def print_next_token():
    if not queue:
        # If the queue is empty, print a message saying so
        print("There are no more tokens in the queue.")
    else:
        # Otherwise, print the next token in the queue and its OTP
        token = queue[0]
        otp = generate_otp(token)
        print(f"Next token: {token}")
        print(f"OTP: {otp}")

# Define a function to add a new token to the queue
def add_token():
    token = generate_token()
    queue.append(token)
    print(f"Token {token} added to the queue.")

# Define a function to remove the next token from the queue
def remove_token():
    if not queue:
        # If the queue is empty, print a message saying so
        print("There are no more tokens in the queue.")
    else:
        # Otherwise, remove the next token from the queue and its OTP from the dictionary
        token = queue.pop(0)
        del otps[token]
        print(f"Token {token} removed from the queue.")

# Define a function to verify an OTP for a given token
def verify_otp(token, otp):
    if token in otps and otps[token] == otp:
        # If the token is in the dictionary and its OTP matches the given OTP, return True
        return True
    else:
        # Otherwise, return False
        return False

if __name__ == "__main__":
    while True:
        print("1. Print next token")
        print("2. Add new token")
        print("3. Remove next token")
        print("4. Verify token with OTP")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print_next_token()
        elif choice == "2":
            add_token()
        elif choice == "3":
            remove_token()
        elif choice == "4":
            token = int(input("Enter token number: "))
            otp = int(input("Enter OTP: "))
            if verify_otp(token, otp):
                print("OTP verified. Token is valid.")
            else:
                print("Invalid token or OTP.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")



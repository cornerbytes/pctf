#!/usr/bin/python3 
from hashlib import md5

def get_flag():
    with open('flag.txt', 'r') as f:
        print(f.read())

def calculate_hash(hash_1: bytes, hash_2: bytes):
    hash_1 = md5(hash_1).hexdigest()
    hash_2 = md5(hash_2).hexdigest()
    return hash_1 == hash_2

def list_menu():
    print(f"1. Play the game")
    print(f"2. Exit")
    print(f"3. Ask dealer what secret")

if __name__ == "__main__":
    print("="*35)
    print("""
                   _           
  _________ ______(_)___  ____ 
 / ___/ __ `/ ___/ / __ \/ __ \\
/ /__/ /_/ (__  ) / / / / /_/ /
\___/\__,_/____/_/_/ /_/\____/
          """)
    print(f"Welcome to the casino!")
    print(f"Hope you get two your lucky number!")
    print(f"enjoy")
    print("="*35)

    while True:
        list_menu()
        user_choice = input('Enter menu (1-3): ')

        if user_choice == '1':
            first_number = input("Enter the first lucky number in hexadecimal : ")
            second_number = input("Enter the second lucky number in hexadecimal : ")
            try: 
                first_lucky_number = bytes.fromhex(first_number)
                second_lucky_number = bytes.fromhex(second_number)
                result = calculate_hash(first_lucky_number, second_lucky_number)
            except: 
                print("In hexa decimal please. Example: da64f2")
                exit()

            if result and (first_number != second_number):
                print(f"Congratulations! your are the lucky person. Here your reward :{get_flag()}")
                exit()
            else:
                print("You are not lucky enough!")
                print("Try again")

        elif user_choice == '2':
            exit()
        elif user_choice == '3':
            print('What ?')
        else:
            print(f"Sir! are you stupid ?")

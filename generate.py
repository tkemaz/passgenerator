import os
import random
import time

def clear():
    os.system('clear')

def main():

    lower = "abcdefghijklmnoprstuvwxyz" # All lower letters
    upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ" # All upper letters
    numbers = "0123456789" # All numbers
    symbols = "!@#$%^&*_=?" # Symbols

    RESET = "\033[0m" # Colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    all_chars = lower + upper + numbers + symbols
    clear()
    time.sleep(1)
    print(f"""
          {CYAN}
       ___                 ___                          _             
      / _ \\__ _ ___ ___   / _ \\___ _ __   ___ _ __ __ _| |_ ___  _ __ 
     / /_)/ _` / __/ __| / /_\\/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|
    / ___/ (_| \\__ \\__ \\/ /_\\\\  __/ | | |  __/ | | (_| | || (_) | |   
    \\/    \\__,_|___/___/\\____/\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   
    {RESET}
    """) # Logo
    while True:
        print(" ")
        user_input = input(f"{RESET}Enter password length or type {BLUE}'exit'{RESET} to quit: ").strip()
        
        if user_input.lower() == 'exit': # Program exitting
            print(f"{RED}Exiting the program.{RESET}")
            time.sleep(1)
            break
        
        if not user_input.isdigit():
            print(f"{RED}Invalid input. Please enter a valid number or 'exit' to quit.{RESET}")
            time.sleep(1)
            continue
        
        length = int(user_input)
        
        password = ''.join(random.sample(all_chars, length))
        time.sleep(1)
        print(f"{RESET}Generated password:{GREEN} ", password) # Generator

if __name__ == '__main__':
    main()
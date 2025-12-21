from fake_data import *
from colorama import Fore, Style, init
import random
import textwrap

# Initialize colorama
init(autoreset=True)

def generate_fake_news():
    subject = Fore.YELLOW + random.choice(subjects) + Style.RESET_ALL
    action = Fore.CYAN + random.choice(actions) + Style.RESET_ALL
    object_ = Fore.MAGENTA + random.choice(objects) + Style.RESET_ALL
    place = Fore.GREEN + random.choice(places) + Style.RESET_ALL
    modifier = Fore.RED + random.choice(modifiers) + Style.RESET_ALL
    
    return f"{subject} {action} {object_} {place} {modifier}"

if __name__ == "__main__":
    user_input = input("Enter the number of fake news you want to generate: ")
    
    # Validate input
    try:
        count = int(user_input)
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive number.")
        exit()

    # Generate and print fake news
    for i in range(count):
        fake_news = generate_fake_news()
        fake_news_text = textwrap.fill(fake_news, width=60)
        print(f"{i+1}. {fake_news_text}\n")

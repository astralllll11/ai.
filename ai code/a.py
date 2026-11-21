import random
import time

CYAN, YELLOW, GREEN, BOLD, RESET = "\033[96m", "\033[93m", "\033[92m", "\033[1m", "\033[0m"

print(f"{CYAN}{BOLD}Genius AI Bot at your service.{RESET}")
print(f"{CYAN}{'=' * 20}{RESET}")
print("Ask me anything")
print("Type 'exit' to quit the program")

while True:
    user_input = input(f"{YELLOW}You: {RESET}")
    q = user_input.lower().strip()

    if q == "exit":
        print(f"{CYAN}Goodbye!{RESET}")
        break
    elif q == "hello":
        print(f"{GREEN}Bot: Hello, I am a AI. How may I help you today?{RESET}")

    elif q == "2+2":
        print(f"{GREEN}Bot: 4 {RESET}")

    elif q == "1+1":
        print(f"{GREEN}Bot: 2 {RESET}")
    else:
        print(f"{GREEN}Bot: im kinda like dumb and idk how to do that sorry{RESET}")

    
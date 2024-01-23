def print_options():
    print("Bot will respond to the following questions:")
    print("1. 'hi'")
    print("2. 'how are you?'")
    print("3. 'how old are you?'")
    print("Type 'bye' to exit.")

def ChatBot():
    print("Welcome to my little chat bot!")
    print_options()

    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("ChatBot: Goodbye!")
            break
        elif 'hi' in user_input:
            print("ChatBot: Hi, I hope you are doing well?")
        elif 'how are you' in user_input:
            print("ChatBot: I am good, thank you for asking!")
        elif 'how old are you' in user_input:
            print("ChatBot: I have just been born, funny enough!")
        else:
            print("ChatBot: Invalid input.")
            print_options()

if __name__ == "__main__":
    ChatBot()






























































































































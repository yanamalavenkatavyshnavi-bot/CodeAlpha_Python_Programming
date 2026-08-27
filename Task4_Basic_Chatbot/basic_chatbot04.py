print("WELCOME TO SIMPLE CHATBOT")
print("Type: hello, how are you, bye or exit")

while True:
    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "bye":
        print("Bot: Goodbye!")

    elif user == "exit":
        print("Bot: Chat ended.")
        break

    else:
        print("Bot: Sorry, I don't understand.")

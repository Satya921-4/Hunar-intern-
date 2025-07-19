def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Rule-based responses
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I help you?")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Bye! Take care.")
        elif "weather" in user_input:
            print("Chatbot: The weather today is sunny with a chance of clouds.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatSimple, your rule-based assistant!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm running perfectly! 😄")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you ask something else?")

# Run the chatbot
chatbot()

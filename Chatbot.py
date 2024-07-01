def jarvis_chatbot(user_input):
    user_input = user_input.lower()
    
    if user_input == "hello" or user_input == "hi":
        return "Hi there! How can I assist you today?"
    elif user_input == "how are you?" or user_input == "how are you":
        return "I'm just a bot, but thanks for asking!"
    elif "your name" in user_input:
        return "I'm just a simple chatbot named Jarvis."
    elif "bye" in user_input or "see you" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"
    elif "weather" in user_input:
        return "I'm just a bot, but you can check the weather online!"
    elif "help" in user_input or "support" in user_input:
        return "Sure, I can help. What do you need assistance with?"
    else:
        return "Sorry, I didn't understand that. Can you please ask something else?"

print("Welcome to Jarvis, your personal chatbot assistant!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Jarvis: Goodbye!")
        break
    response = jarvis_chatbot(user_input)
    print("Jarvis:", response)

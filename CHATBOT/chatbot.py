import datetime
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I help you?"
    elif "your name" in user_input:
        return "I am CodSoft AI Chatbot 🤖"
    elif "time" in user_input:
        return f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "date" in user_input:
        return f"Today's date is {datetime.date.today()}"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"
    elif "help" in user_input:
        return "You can ask me about time, date, or general greetings."
    else:
        return "Sorry, I don't understand that yet 😅"
print("🤖 Chatbot is running (type 'bye' to exit)\n")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Bot:", response)
    if "bye" in user.lower():
        break
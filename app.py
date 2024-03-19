from transformers import pipeline

# Conversational pipeline
chatbot = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")

chat_history = []

while True:
    user_message = input("You: ")
    chat_history.append({"role": "user", "message": user_message})

    if user_message.lower() == "exit":
        break

    conversation_bot_result = chatbot(user_message)
    bot_response = conversation_bot_result[0]["generated_text"]
    chat_history.append({"role": "bot", "message": bot_response})

    print("Bot:", bot_response)

# Print the chat history
print("\nChat History:")
for chat in chat_history:
    print(f"{chat['role']}: {chat['message']}")

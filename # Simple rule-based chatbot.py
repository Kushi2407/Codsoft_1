# Simple rule-based chatbot
def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined responses and associated keywords
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm just a computer program, but I'm here to help!",
        "goodbye": "Goodbye! Have a great day!",
    }

    # Check if the user input matches any predefined keywords
    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # If no match is found, provide a default response
    return "I'm not sure how to respond to that. Can you please rephrase your question?"

# Main loop for interacting with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

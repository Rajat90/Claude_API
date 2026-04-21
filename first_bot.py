import modules

# Initial list of messages
messages = []

while True:
    user_input = input(">: ")

    if user_input.lower() == "exit":
        break

    print(user_input)

    # Add user message
    messages = modules.add_user_message(messages, user_input)

    # Get assistant response
    response = modules.chat(messages)
    print(response)

    # Add assistant response to history
    messages = modules.add_assistant_message(messages, response)

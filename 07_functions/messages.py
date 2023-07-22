def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Message sent: {current_message}")
        sent_messages.append(current_message)


messages = ['hey, how are you?', 'I hope you\'re doing ok!', 'I\'m sightseeing.']
messages_completed = []
send_messages(messages[:], messages_completed)

print(messages)
print(messages_completed)
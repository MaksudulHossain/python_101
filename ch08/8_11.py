def send_messages(messages):
        sent_messages = []
        while messages:
             sent_messages.append(messages.pop())
        return sent_messages

messages = [
    "Happy Birthday!",
    "May Allah bless you always.",
    "Keep up the great work!",
    "Wishing you success and happiness.",
    "Thank you for being a great mentor!"
]
sent_messages = send_messages(messages[:])
print(sent_messages) 
print(messages) 
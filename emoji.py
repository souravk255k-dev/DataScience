emoji = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "love": "❤️",
    "surprised": "😲"
}

message = input("Enter your message: ")

words = message.split()
new_message = ""

for word in words:
    if word in emoji:
        new_message += emoji[word] + " "
    else:
        new_message += word + " "

print("Converted message:")
print(new_message)

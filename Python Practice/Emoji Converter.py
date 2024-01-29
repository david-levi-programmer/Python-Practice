text = input(">")


def emoji_convert(message):
    sentence = message.split(" ")
    emoji = {
        ":)": "😀",
        ":(": "☹️",
        ":<": "🫤"
    }
    output = ""
    for word in sentence:
        output += emoji.get(word, word) + " "
    return output


print(emoji_convert(text))

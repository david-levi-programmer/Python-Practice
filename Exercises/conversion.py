def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


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

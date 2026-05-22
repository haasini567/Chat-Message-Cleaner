import re

def clean_message(msg):
    try:
        if not isinstance(msg, str):
            raise ValueError("Invalid message")

        cleaned = re.sub(r'[^A-Za-z0-9 ]', '', msg)
        cleaned = cleaned.strip().lower()

        return cleaned

    except ValueError:
        return None


def filter_empty(messages):
    return [msg for msg in messages if msg and msg.strip()]


def process_messages(*msgs):
    cleaned_list = []

    for msg in msgs:
        cleaned = clean_message(msg)

        if cleaned:
            cleaned_list.append(cleaned)

    return cleaned_list


messages = [
    "Hello!!!",
    "Buy now $$$",
    "Good morning :)",
    "",
    "   Extra spaces   ",
    "Wow!!! Amazing!!!",
    "123456",
    "@@@###",
    "Python is fun!!",
    None
]

valid_messages = filter_empty(messages)

result = process_messages(*valid_messages)

print(result)

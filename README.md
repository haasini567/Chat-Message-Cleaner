# Chat-Message-Cleaner

Python project to clean and process chat messages

📩 Chat Message Cleaner

📄 Description
A command-line based Python application that cleans and processes chat messages efficiently.
The program removes unwanted special characters, eliminates empty or invalid messages, normalizes text formatting, and generates a clean list of readable messages. It uses functions, string operations, regular expressions, and exception hand.


🎯 Objective

1)To remove unwanted special characters from chat messages.

2)To normalize and format text properly.

3)To filter empty or invalid messages from the list.

4)To handle errors using exception handling.

5)To generate a cleaned and readable messages listling to improve the quality.


✨ Features

1)Removes special characters like @, #, !, $, etc.

2)Eliminates extra spaces from messages.

3)Converts messages into a normalized format.

4)Filters empty strings and invalid inputs.

5)Handles exceptions for non-string values like None.

6)Uses regular expressions for text cleaning.

7)Processes multiple messages efficiently.

8)Displays a clean output list.

9)Built using pure Python 3 of chat data.


⚙️ How It Works

1)The user provides a list of chat messages.

2)Empty and invalid messages are filtered.

3)Special characters are removed using regular expressions.

4)Extra spaces are trimmed from the text.

5)Messages are converted into a normalized format.

6)Exception handling manages invalid inputs.

7)The cleaned messages are stored in a new list.

8)The final cleaned output is displayed.


▶️ How To Run

1. Clone the repository:
   
git clone https://github.com/haasini567/chat-message-cleaner

2. Open the project folder:
   
cd chat-message-cleaner

3. Run the program:
   
python cleaner.py


📌 Sample Input

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


📤 Sample Output

['hello',
 'buy now',
 'good morning',
 'extra spaces',
 'wow amazing',
 '123456',
 'python is fun']

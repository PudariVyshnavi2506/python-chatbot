import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm good, thanks!", "Doing great!"]],
    [r"what is your name?", ["I'm a simple chatbot."]],
    [r"bye|exit", ["Goodbye!", "See you later!"]],
]

# Create chatbot object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hi! I'm your chatbot. Type 'bye' to exit.")
chatbot.converse()

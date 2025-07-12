import random

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones.",
    "Stay focused and never give up."
]

# Function to display a random quote
def show_quote():
    quote = random.choice(quotes)
    print("\n💡 Motivational Quote of the Day:")
    print(f"\"{quote}\"\n")

# Run the program
if __name__ == "__main__":
    show_quote()

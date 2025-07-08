import time
import random

# Predefined responses
reminders = {
    "happy": [
        "Keep smiling! Life's beautiful 🌟",
        "Spread your joy with others today!",
        "Keep the positive vibes going!"
    ],
    "sad": [
        "It's okay to feel sad, better days are coming 💖",
        "Take a break and do something you love!",
        "Don't give up, the sun will shine again!"
    ],
    "angry": [
        "Take a deep breath. Calmness is power 🌬️",
        "Go for a walk to release your stress.",
        "Try to speak kindly even when it's hard."
    ],
    "neutral": [
        "Stay focused and hydrated 💧",
        "Don't forget to take small breaks!",
        "Keep learning, keep growing."
    ]
}

# Detect emotion from the message
def detect_emotion(message):
    message = message.lower()
    if any(word in message for word in ["happy", "excited", "joy", "awesome", "great"]):
        return "happy"
    elif any(word in message for word in ["sad", "unhappy", "depressed", "down"]):
        return "sad"
    elif any(word in message for word in ["angry", "mad", "furious", "annoyed"]):
        return "angry"
    else:
        return "neutral"

# Main loop
print("Welcome to your Emotion-Based Reminder System!")
while True:
    msg = input("\nTell me how you're feeling (or type 'exit' to quit): ")
    if msg.lower() == 'exit':
        print("Goodbye! Stay emotionally healthy 💙")
        break

    mood = detect_emotion(msg)
    reminder = random.choice(reminders[mood])

    print(f"\nSince you're feeling {mood}, here's a reminder for you:")
    print(f"➡️  {reminder}")

    print("\nI'll remind you again in 10 seconds...\n")
    time.sleep(10)

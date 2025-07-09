import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize recognizer
recognizer = sr.Recognizer()

# To-Do list
todo_list = []

# Speak a message
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

# Main functionality
def main():
    speak("Welcome to your Voice-Controlled To-Do List!")
    
    while True:
        speak("Say 'add task', 'show tasks', or 'exit'")
        command = listen()

        if 'add task' in command:
            speak("What task would you like to add?")
            task = listen()
            if task:
                todo_list.append(task)
                speak(f"Task '{task}' added.")
        
        elif 'show tasks' in command:
            if todo_list:
                speak("Here are your tasks:")
                for i, task in enumerate(todo_list, start=1):
                    speak(f"Task {i}: {task}")
            else:
                speak("Your to-do list is empty.")

        elif 'exit' in command:
            speak("Goodbye!")
            break

        else:
            speak("Please say a valid command.")

if __name__ == "__main__":
    main()

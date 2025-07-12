import time

# Initialize hours, minutes, and seconds
hours = 0
minutes = 0
seconds = 0

# Run an infinite loop to simulate a clock
while True:
    # Display the time in HH:MM:SS format
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')

    time.sleep(1)  # Wait for 1 second (simulates clock pulse)

    # Increment seconds like a counter
    seconds += 1

    # If seconds reach 60, reset to 0 and increment minutes
    if seconds == 60:
        seconds = 0
        minutes += 1

    # If minutes reach 60, reset to 0 and increment hours
    if minutes == 60:
        minutes = 0
        hours += 1

    # If hours reach 24, reset to 0 (24-hour format)
    if hours == 24:
        hours = 0

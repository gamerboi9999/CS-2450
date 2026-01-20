import random

print("Hello! I'm going to try to guess your age.")
name = input("What's your name? ")

max_attempts = 5
attempts = 0

for attempt in range(max_attempts):
    guess = random.randint(15, 50)  # Expanded range
    attempts += 1
    print(f"\nAttempt {attempts}/{max_attempts}: Is your age {guess}?")
    print("Enter 'y' for yes, 'N' for older, 'o' for younger: ")
    answer = input().lower()
    
    if answer == 'y':
        print(f"\nYay! I guessed it! {name} is {guess} years old.")
        break
    elif answer == 'o':
        print("OK, you're older than that. Let me think...")
    elif answer == 'N':
        print("OK, you're younger than that. Let me think...")
    else:
        print("Hmm, I'll try a different guess...")
    
    if attempts == max_attempts:
        print(f"\nSorry {name}, I couldn't guess your age in {max_attempts} attempts!")
        
    
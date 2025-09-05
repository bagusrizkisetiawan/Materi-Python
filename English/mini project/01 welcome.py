# 1. Ask the player for some information
print("Welcome to the game! Let's get you set up.")
name = input("What is your name? ")
game = input("What is your favorite game? ")
level = 1

# 2. Use an f-string to create a personalized welcome message
welcome_message = f"Welcome, {name}! Get ready to play {game}. You are starting at Level {level}. Good luck!"

# 3. Print the final message to the screen
print(
    "\n--- Generating Your Profile ---"
)  # The \n creates a new line to make it look nice
print(welcome_message)
print("-----------------------------")

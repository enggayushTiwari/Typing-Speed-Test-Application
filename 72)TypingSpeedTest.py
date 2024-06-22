# Import the Tkinter module, the time module, and the random module
import tkinter as tk
import time
import random

# Define a list of sentences to be used for the typing test
sentences = [
            "The quick brown fox jumps over the lazy dog. To be or not to be doesn't matter.",
            "May the Force be with you Python is a fun and powerful programming language.",
            "A paragraph is a self-contained unit of a page specific topic.",
            "A paragraph can also be a part of a larger text A book report is an analysis.",
            "readers with insights into the books key elements but breaking it down is good.",
            "Lorem ipsum is a common placeholder text derived from a Latin text and has altered.",
            "the visual form of a document or a typeface"
             ]

# Define a function that returns a random sentence from the list
def get_random_sentence():
    return random.choice(sentences)

# Define a function that returns the current time in seconds
def get_current_time():
    return time.time()

# Define a function that calculates the accuracy of the user's input
# by comparing it with the given word
def get_accuracy(input_text, word):
    # Split the input text and the word into words
    input_words = input_text.split()
    word_words = word.split()
    # Initialize a variable to store the number of correct words
    correct_words = 0
    # Loop through the minimum length of the input words and the word words
    for i in range(min(len(input_words), len(word_words))):
        # If the words at the same index are equal, increment the correct words
        if input_words[i] == word_words[i]:
            correct_words += 1
    # Return the percentage of correct words
    return (correct_words / len(word_words)) * 100

# Define a function that calculates the words per minute (WPM) of the user's input
# by dividing the number of characters by 5 and dividing by the total time in seconds
def get_wpm(input_text, total_time):
    return (len(input_text)/5) / (total_time/60)

# Define a class that represents the game logic and the GUI elements
class Game:
    # Define the constructor method that takes a master window as an argument
    def __init__(self, master):
        # Assign the master window to an instance attribute
        self.master = window
        # Initialize some instance attributes to store the game state and data
        self.reset_flag = True # A flag to indicate whether the game is reset or not
        self.end = False # A flag to indicate whether the game is over or not

        # Set the title and the size of the master window
        self.master.title("Typing Speed Test Application")
        self.master.geometry("750x500+300+100")
        # self.master.config(bg='grey')

        # Create a label widget for the heading and place it on the master window
        self.heading = tk.Label(self.master, text="Typing Speed Test Application", font=("Arial", 25), fg='orange')
        self.heading.place(x=150, y=10)

        # Create a button widget for starting the game and place it on the master window
        self.start_button = tk.Button(self.master, text="Start", command=self.start_game, width=15, bg="light blue")
        self.start_button.place(x=125, y=75)

        # Create a button widget for resetting the game and place it on the master window
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game, width=15, bg="light blue")
        self.reset_button.place(x=500, y=75)

        # Create a label widget for showing the results and place it on the master window
        self.score_label = tk.Label(self.master, text='Time:0      Accuracy:0 %      WPM:0 ', font=("Arial", 20), fg='green')
        self.score_label.place(x=150, y=125)

        # Create a label widget for showing the instruction and place it on the master window
        self.instruction_label = tk.Label(self.master, text="Instruction: Click on the start button and then, Type the above sentence as fast and as accurately as you can:")
        self.instruction_label.place(x=75, y=300)

        # Create a text widget for showing the word to be typed and place it on the master window
        self.sentence = tk.Text(self.master, height=3, width=60, font=("Courier", 14), fg='indigo')
        self.sentence.place(x=50, y=225)

        # Create a label widget for showing the timer and place it on the master window
        self.timer_label = tk.Label(self.master, text="00:00:00", font=("Arial", 20), fg='red')
        self.timer_label.place(x=300, y=75)

        # Create a text widget for getting the user's input and place it on the master window
        self.input = tk.Text(self.master, height=3, width=60, font=("Courier", 14), fg='black')
        self.input.place(x=50, y=325)
        # Bind the key release event of the input widget to a function that checks the user's input
        self.input.bind("<KeyRelease>", self.check)

    # Define a method that starts the game
    def start_game(self):
        # If the game is reset
        if self.reset_flag:
            # Set the reset flag to False
            self.reset_flag = False
            # Set the active flag to True
            self.active = True
            # Delete the contents of the sentence and input widgets
            self.sentence.delete(1.0, tk.END)
            self.input.delete(1.0, tk.END)
            # Get a random sentence and assign it to the word attribute
            self.word = get_random_sentence()
            # Insert the word into the sentence widget
            self.sentence.insert(1.0, self.word)
            # Get the current time and assign it to the time start attribute
            self.time_start = get_current_time()
            # Call the update timer method
            self.update_timer()

    # Define a method that resets the game
    def reset_game(self):
        # If the game is not reset
        if not self.reset_flag:
            # Set the reset flag to True
            self.reset_flag = True
            # Set the active flag to False
            self.active = False
            # Reset the game state and data attributes
            self.input_text = ''
            self.word = ''
            self.time_start = 0
            self.total_time = 0
            self.results = 'Time:0      Accuracy:0 %      WPM:0'
            self.wpm = 0
            self.end = False
            # Delete the contents of the sentence and input widgets
            self.sentence.delete(1.0, tk.END)
            self.input.delete(1.0, tk.END)
            # Update the text of the score label
            self.score_label.config(text=self.results)
            # Update the text of the timer label
            self.timer_label.config(text="00:00:00")

    # Define a method that checks the user's input
    def check(self, event):
        # If the game is active and not over
        if self.active and not self.end:
            # Get the user's input from the input widget and strip any whitespace
            self.input_text = self.input.get(1.0, tk.END)
            # Set the end flag to True if the input text is equal to the word in length
            self.end = len(self.input_text) == len(self.word)
            # Calculate the results of the game
            self.calculate()
            
    # Define a method that calculates the results of the game
    def calculate(self):
        # If the game is over
        if self.end:
            # Get the current time and subtract the start time to get the total time
            self.total_time = get_current_time() - self.time_start
            # Calculate the accuracy of the user's input
            self.accuracy = get_accuracy(self.input_text, self.word)
            # Calculate the WPM of the user's input
            self.wpm = get_wpm(self.input_text, self.total_time)
            # Format the results as a string
            self.results = f"Time:{round(self.total_time)} Accuracy:{round(self.accuracy)} % WPM:{round(self.wpm)}"
            # Update the text of the score label
            self.score_label.config(text=self.results)
            # Delete the contents of the sentence widget
            self.sentence.delete(1.0, tk.END)
            # Insert a message into the sentence widget
            self.sentence.insert(1.0, "Congratulations! You have completed the test.")
            # Set the active flag to False
            self.active = False

    # Define a function to update the timer
    def update_timer(self):
        if self.active:
            # Get the current time elapsed
            self.total_time = get_current_time() - self.time_start
            # Format the time as hh:mm:ss
            time_string = time.strftime("%H:%M:%S", time.gmtime(self.total_time))
            # Update the label text
            self.timer_label.config(text=time_string)
            # Schedule the next update after 1 second
            self.master.after(1000, self.update_timer)  

# Create a Tkinter window object
window = tk.Tk()
# Create a game object with the window as the master
game = Game(window)
# Start the main loop of the windo
window.mainloop()

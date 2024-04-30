import tkinter as tk

def submit_answer():
    # Get the answer from the entry widget and process it into a list
    answer = entry.get().strip()
    answer_list = [item.strip() for item in answer.split(',')]
    # Append the processed list to the answers list
    answers.append(answer_list)
    # Print the current list of answers to the command line
    print("Current answers list:", answers)
    # Clear the entry widget for the next input
    entry.delete(0, 'end')
    # Proceed to the next question if there are more questions
    next_question()

def next_question():
    global current_question_index
    # Increase the question index
    current_question_index += 1
    # Check if there are more questions
    if current_question_index < len(questions):
        # Update the question label
        question_label.config(text=questions[current_question_index])
        # Update the label to show the current list of answers
        label.config(text=f"Answers collected: {answers}")
    else:
        # No more questions, update the GUI to show completion
        question_label.config(text="All questions answered.")
        entry.config(state='disabled')
        next_button.config(state='disabled')
        submit_button.config(state='disabled')
        label.config(text=f"Final answers: {answers}")

# Questions list
questions = [
    "What ingredient do you have? \n Please use ',' to interval the ingredients.\n For example: egg,milk,meat...",
    "What ingredient you don't want it to appear in your food? \n Please use ',' to interval the ingredients.\n For example: egg,milk,meat..."
]

# List to hold the answers
answers = []
current_question_index = -1

# Create the main window
root = tk.Tk()
root.title("Ingredient Collection App")
root.geometry("800x600")  # Set the size of the window

# Define a larger font for better readability
large_font = ('Verdana', 14)

# Create a label to display the question
question_label = tk.Label(root, text="", font=large_font)
question_label.pack(pady=20)

# Create an entry widget for input, make it larger
entry = tk.Entry(root, font=large_font, width=50)
entry.pack()

# Create a button to submit the answer
submit_button = tk.Button(root, text="Submit", command=submit_answer, font=large_font)
submit_button.pack(pady=10)

# Create a button to go to the next question
next_button = tk.Button(root, text="Next Question", command=next_question, font=large_font)
next_button.pack(pady=10)

# Create a label to display the collected answers
label = tk.Label(root, text="Answers collected: ", font=large_font)
label.pack(pady=20)

# Start with the first question
next_question()

# Start the GUI event loop
root.mainloop()

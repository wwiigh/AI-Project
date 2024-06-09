import tkinter as tk

def submit_answer():
    answer = entry.get().strip()
    answer_list = [item.strip() for item in answer.split(',')]
    answers.append(answer_list)
    update_answers_label()
    entry.delete(0, 'end')
    next_question()

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        question_label.config(text=questions[current_question_index])
    else:
        question_label.config(text="All questions answered.")
        entry.config(state='disabled')
        next_button.config(state='disabled')
        submit_button.config(state='disabled')

def update_answers_label():
    answers_text = "\n".join([f"- {', '.join(answer)}" for answer in answers])
    answers_label.config(text=f"Answers collected:\n{answers_text}")

questions = [
    "What ingredients do you have?",
    "What ingredients do you not want in your food?"
]

answers = []
current_question_index = -1

root = tk.Tk()
root.title("Ingredient Collection App")
root.geometry("800x600")

# Define colors
background_color = "#f0f0f0"
button_color = "#4CAF50"
button_hover_color = "#45a049"
text_color = "#333339"

# Apply theme
root.configure(bg=background_color)
root.option_add("*TButton*background", button_color)
root.option_add("*TButton*foreground", text_color)
root.option_add("*TButton*highlightBackground", button_hover_color)
root.option_add("*TButton*highlightColor", button_hover_color)

large_font = ('Verdana', 14)

question_label = tk.Label(root, text="", font=large_font, bg=background_color, fg=text_color)
question_label.pack(pady=20)

entry = tk.Entry(root, font=large_font, width=50)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_answer, font=large_font)
submit_button.pack(pady=10)

next_button = tk.Button(root, text="Next Question", command=next_question, font=large_font)
next_button.pack(pady=10)

answers_label = tk.Label(root, text="Answers collected:", font=large_font, bg=background_color, fg=text_color)
answers_label.pack(pady=20)

next_question()

root.mainloop()

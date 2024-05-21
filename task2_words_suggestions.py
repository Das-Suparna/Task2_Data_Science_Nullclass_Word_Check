import tkinter as tk
import enchant
import re

english_dict = enchant.Dict("en_US")

def find_suggestions(word):
    suggestions = english_dict.suggest(word)
    return suggestions[:10]  

def check_word(word):
    return english_dict.check(word)

def is_valid_input(word):
    return bool(re.match("^[a-zA-Z]+$", word))

def handle_input():
    word = entry.get().lower()
    if not is_valid_input(word):
        label_of_output.config(text="Invalid input. Please enter only letters.")
        clear_suggestions()
    elif not check_word(word):
        wrong_words.append(word)
        if len(wrong_words) == 2:
            label_of_output.config(text=f"'{word}' word is not available" , fg="red")
            labelling_wrong_wordings.config(text="Words Wrongly entered so far: " + ", ".join(wrong_words))
            suggestions_label.config(text="Suggestions for the wrong words:")
            
            clear_suggestions()
            for wrong_word in wrong_words:
                suggestions = find_suggestions(wrong_word)
                suggestion_labels.append(tk.Label(task2_window, text=f"{wrong_word}: {', '.join(suggestions)}", font=("Verdana", 13, "bold")))
            for label in suggestion_labels:
                label.pack(anchor="w")
            
            if len(wrong_words) % 2 == 0:
                wrong_words.clear()
                
        else:
            label_of_output.config(text=f"'{word}' word is not available" , fg="red")
            labelling_wrong_wordings.config(text=" ")
            suggestions = find_suggestions(word)
            if suggestions:
                suggestions_label.config(text="Suggestions:")
                
                clear_suggestions()
                suggestion_labels.append(tk.Label(task2_window, text=', '.join(suggestions), font=("Verdana", 13, "bold")))
                for label in suggestion_labels:
                    label.pack(anchor="w")
            else:
                suggestions_label.config(text="No suggestions available.")
    else:        
        wrong_words.clear()
        clear_suggestions()
        label_of_output.config(text=f"'{word}' is a valid word.", fg="green")
        labelling_wrong_wordings.config(text="")
        suggestions_label.config(text="")


def clear_input():
    entry.delete(0, tk.END)

def clear_suggestions():
    for label in suggestion_labels:
        label.destroy()
    suggestion_labels.clear()
    
task2_window = tk.Tk()
task2_window.title("Word Checker")
task2_window.configure(bg="white")


window_width = 1000
window_height = 600
screen_width = task2_window.winfo_screenwidth()
screen_height = task2_window.winfo_screenheight()
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2) - 25
task2_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

title = tk.Label(task2_window, text="Enter Correct Spelled Words : ", bg="white", font=("Verdana", 13, "bold"))
title.pack(pady=10)

input_frame = tk.Frame(task2_window, bg="white")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=40, font=("Verdana", 13))
entry.pack(side=tk.LEFT)

check_button = tk.Button(input_frame, text="Check",bg="blue", fg="white", command=handle_input, font=("Verdana", 13, "bold"))
check_button.pack(side=tk.LEFT,padx=10)

reset_button = tk.Button(input_frame, text="Reset", bg="orange",command=clear_input, font=("Verdana", 13, "bold"))
reset_button.pack(side=tk.LEFT, padx=20)

quit_button = tk.Button(task2_window, text="Close", command=task2_window.quit, bg="red", fg="white", font=("Verdana", 13, "bold"))
quit_button.place(x=830,y=56)

label_of_output = tk.Label(task2_window, text="", fg="red", bg="white", font=("Verdana", 13, "bold"))
label_of_output.pack()

suggestions_label = tk.Label(task2_window, text="", bg="white", font=("Verdana", 13, "bold"))
suggestions_label.pack()

labelling_wrong_wordings = tk.Label(task2_window, text="", bg="white", font=("Verdana", 13, "bold"))
labelling_wrong_wordings.pack()

suggestion_labels = []

wrong_words = []

task2_window.mainloop()

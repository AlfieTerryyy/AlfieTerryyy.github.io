import tkinter as tk
from tkinter import simpledialog, messagebox

def check_password():
    entered_password = password_entry.get()
    if entered_password == "0000":

        root.deiconify()
        password_popup.destroy()
    else:
        password_entry.delete(0, tk.END)
        password_entry.focus_set()
        messagebox.showerror("Incorrect Password", "Please enter the correct password.")

def apply_letter_mapping(user_input):
    letter_mapping = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w',
        'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
        'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a',
        '0': '9', '1': '8', '2': '7', '3': '6',
        '4': '5', '5': '4', '6': '3', '7': '2',
        '8': '1', '9': '0',
        '!': '!', '@': '@', '#': '#', '$': '$',
        '%': '%', '^': '^', '&': '&', '*': '*',
        '(': '(', ')': ')', '-': '-', '_': '_',
        '+': '+', '=': '=', '[': '[', ']': ']',
        '{': '{', '}': '}', ';': ';', ':': ':',
        ',': ',', '.': '.', '/': '/',
    }

    result = ""
    for char in user_input.lower():
        if char.isalpha():
            result += letter_mapping.get(char, char)
        else:
            result += char
    return result
def process_user_input():
    user_input = input_entry.get()
    output_text = apply_letter_mapping(user_input)
    output_label.config(text=f"Output: {output_text}")
    terminal_text.insert(tk.END, f"Processed Output: {output_text}\n")
root = tk.Tk()
root.title("G.L.A.M")
root.withdraw()
password_popup = tk.Toplevel(root)
password_popup.title("Password")
password_entry = tk.Entry(password_popup, show="*")
password_entry.pack()
check_button = tk.Button(password_popup, text="Enter", command=check_password)
check_button.pack()
password_entry.focus_set()
input_entry = tk.Entry(root)
input_entry.pack(pady=10, padx=10)
process_button = tk.Button(root, text="Process Input", command=process_user_input)
process_button.pack()
output_label = tk.Label()
terminal_text = tk.Text(root, height=10, width=40)
terminal_text.pack()
root.mainloop()
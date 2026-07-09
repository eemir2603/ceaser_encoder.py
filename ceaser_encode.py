import tkinter as tk
from tkinter import messagebox

# Caesar Functions
def caesar_encode(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            base = 65 if letter.isupper() else 97
            index = ord(letter) - base
            new_index = (index + shift) % 26
            result += chr(new_index + base)
        else:
            result += letter
    return result

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

def brute_force(text):
    results = ""
    for shift in range(26):
        results += f"{shift}: {caesar_decode(text, shift)}\n"
    return results

# GUI Functions
def encode_text():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())
        result = caesar_encode(text, shift)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid input!")

def decode_text():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())
        result = caesar_decode(text, shift)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid input!")

def brute_text():
    text = entry_text.get()
    result = brute_force(text)
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

# Window 
root = tk.Tk()
root.title("Ceaser Tool")
root.geometry("400x400")

# Inputs 
tk.Label(root, text="Text:").pack()
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Shift:").pack()
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

# Buttons 
tk.Button(root, text="Encode", command=encode_text).pack(pady=5)
tk.Button(root, text="Decode", command=decode_text).pack(pady=5)
tk.Button(root, text="Bruteforce", command=brute_text).pack(pady=5)

# Output
output = tk.Text(root, height=10, width=45)
output.pack(pady=10)

# Run 
root.mainloop()

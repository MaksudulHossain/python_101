import tkinter as tk
from tkinter import messagebox

# Step 1: Dictionary of Prophets and Famous Facts
prophets_facts = {
    "Adam": "The first human and Prophet, created by Allah.",
    "Idris": "Known for his wisdom and patience.",
    "Nuh": "Built the Ark to save people from the flood.",
    "Hud": "Sent to the people of 'Ad who were arrogant and powerful.",
    "Salih": "Sent to Thamud and had the miracle of the she-camel.",
    # Add the rest...
}

# Step 2: Function to handle button click
def show_fact(name):
    fact = prophets_facts.get(name, "Fact not found.")
    messagebox.showinfo(title=name, message=fact)

# Step 3: Build the GUI
root = tk.Tk()
root.title("Facts about Prophets")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Step 4: Create buttons dynamically
for i, prophet in enumerate(prophets_facts.keys()):
    btn = tk.Button(frame, text=prophet, width=20, 
                    command=lambda p=prophet: show_fact(p))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

root.mainloop()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#SAMPLING SCHEMA FOR CREATING STEP VALUES 

import tkinter as tk
from tkinter import ttk
from pyDOE import lhs
import numpy as np
import random
import itertools

def modified_fullfact(levels):
    num_factors = len(levels)
    H = np.array(np.meshgrid(*[np.linspace(start, end, num=level) for start, end, level in levels])).T.reshape(-1, num_factors)
    return H.astype(int)

def random_sampling():
    x = round(random.uniform(-5, 5))
    y = round(random.uniform(-5, 5))
    return x, y

def lhs_sampling():
    samples = lhs(2, samples=5, criterion='maximin')
    x, y = -5 + 10 * samples[0]
    return round(x), round(y)

def generate_samples():
    random_sample = random_sampling()
    lhs_sample = lhs_sampling()
    full_factorial_sample = full_factorial_design[random.choice(range(len(full_factorial_design)))]

    result_text.set(f"Random Sampling: {random_sample}\n"
                    f"LHS Sampling: {lhs_sample}\n"
                    f"Full Factorial Sample: {full_factorial_sample}")

    # Start the rotation
    rotate_dice()

def rotate_dice():
    dice_values = [-5, -4, -3, -2, -1, 0 , 1, 2, 3, 4, 5]
    for dice_value in itertools.cycle(dice_values):
        dice_label.config(text=f"⚀ {dice_value}")  # Unicode dice character
        root.update()
        root.after(500, lambda: None)  # Pause for 500 milliseconds
        
# Define the number of levels for each factor
levels_per_factor = [(-5, 5, 10), (-5, 5, 10)]
full_factorial_design = modified_fullfact(levels_per_factor)

# Create the main window
root = tk.Tk()
root.title("Sampling Interface")

# Create a label for the rotating dice
dice_label = ttk.Label(root, text="", font=('Arial', 50))
dice_label.pack()

# Create a custom style for the button
style = ttk.Style()
style.configure("TButton", font=('Arial', 25))

# Create and pack widgets
generate_button = ttk.Button(root, text="Generate Samples", command=generate_samples, style="TButton")
generate_button.pack(pady=50) 

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=('Arial', 30))
result_label.pack()

# Center the window on the screen
root.eval('tk::PlaceWindow . center')

# Run the main loop
root.mainloop()


# In[ ]:





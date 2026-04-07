import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

# RGB to HEX
def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

bg_color = rgb(0, 128, 128)

# Main window
root = tk.Tk()
root.title("JoSAA Predictor")
root.geometry("800x500")
root.configure(bg=bg_color)

# ---------------- DATA ----------------

exams = ["JEE Mains", "JEE Advanced"]

genders = ["Gender-Neutral", "Female-only (including Supernumerary)"]

categories = [
    "SC", "ST (PwD)", "SC(PwD)", "OPEN",
    "OBC-NCL(PwD)", "EWS(PwD)", "OPEN(PwD)",
    "ST", "EWS", "OBC-NCL"
]

states = [
    "Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa",
    "Gujarat", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand",
    "Karnataka", "Kerala","Ladakh", "Madhya Pradesh", "Maharashtra", "Odisha",
    "Punjab", "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh",
    "Uttarakhand", "West Bengal"
]

# 🔥 Load Academic Programs
try:
    with open("programs.txt", "r", encoding="utf-8") as f:
        academic_programs = [line.strip() for line in f if line.strip()]
except:
    academic_programs = ["Error loading programs"]

# 🔥 Load Colleges
try:
    with open("colleges.txt", "r", encoding="utf-8") as f:
        colleges = [line.strip() for line in f if line.strip()]
except:
    colleges = ["Error loading colleges"]

# ---------------- UI ----------------

label_style = {"bg": bg_color, "fg": "white", "font": ("Arial", 12)}



# Rank
tk.Label(root, text="Enter Rank", **label_style).pack(pady=5)
rank_entry = tk.Entry(root)
rank_entry.pack(pady=5)

# Exams
tk.Label(root, text="Select Exam", **label_style).pack(pady=5)
exam_combo = ttk.Combobox(root, values=exams, state="readonly")
exam_combo.pack(pady=5)

# Gender
tk.Label(root, text="Select Gender", **label_style).pack(pady=5)
gender_combo = ttk.Combobox(root, values=genders, state="readonly")
gender_combo.pack(pady=5)

# State
tk.Label(root, text="Select State", **label_style).pack(pady=5)
state_combo = ttk.Combobox(root, values=states, state="readonly")
state_combo.pack(pady=5)

# Category
tk.Label(root, text="Select Category", **label_style).pack(pady=5)
category_combo = ttk.Combobox(root, values=categories, state="readonly")
category_combo.pack(pady=5)

# Academic Programme
tk.Label(root, text="Select Academic Programme", **label_style).pack(pady=5)
program_combo = ttk.Combobox(root, values=academic_programs, state="readonly", width=70)
program_combo.pack(pady=5)

# 🔥 NEW: Preferred Colleges
tk.Label(root, text="Select Preferred College", **label_style).pack(pady=5)
college_combo = ttk.Combobox(root, values=colleges, state="readonly", width=70)
college_combo.pack(pady=5)

# ---------------- LOGIC ----------------
user_input=[]
home_state=[]
def submit():
    rank = rank_entry.get()
    
    if not rank.isdigit():
        result_label.config(text="Enter valid rank")
        return

    rank = int(rank)
    user_input.append(rank)

    exam = exam_combo.get()
    user_input.append(exam)
    state = state_combo.get()
    home_state.append(state)
    user_input.append(state)
    gender = gender_combo.get()
    user_input.append(gender)
    category = category_combo.get()
    user_input.append(category)
    program = program_combo.get()
    user_input.append(program)
    college = college_combo.get()
    user_input.append(college)

    # ✅ user input list
    #user_input = user_input+[rank, exam, gender, state, category, program, college]
    



    # All India list
    all_india = [s for s in states if s != state]

    # Terminal output
    print("User Input:", user_input)

    # GUI output
    result_label.config(
        text=f"Rank: {rank}\nExam: {exam}\nGender: {gender}\nState: {state}\nCategory: {category}\nProgram: {program}\nCollege: {college}"
    )

# Button
tk.Button(root, text="Submit", command=submit).pack(pady=20)

# Result
result_label = tk.Label(root, text="", bg=bg_color, fg="white")
result_label.pack(pady=10)

# Run app
root.mainloop()




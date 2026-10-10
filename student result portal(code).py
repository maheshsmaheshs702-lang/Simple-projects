from tkinter import *

# Function to calculate result
def calculate_result():
    name = int(entry_name.get())
    roll = entry_roll.get()

    m1 = int(entry_m1.get())
    m2 = int(entry_m2.get())
    m3 = int(entry_m3.get())
    m4 = int(entry_m4.get())
    m5 = int(entry_m5.get())

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
        result = "PASS"
    else:
        result = "FAIL"

    output.config(
        text=f"Student Name: {name}\n"
             f"Roll No: {roll}\n"
             f"Total Marks: {total}/500\n"
             f"Percentage: {percentage:.2f}%\n"
             f"Result: {result}"
    )

# Main window
root = Tk()
root.title("Student Result Portal")
root.geometry("450x550")

# Heading
Label(root, text="STUDENT RESULT PORTAL", font=("Arial", 16, "bold")).pack(pady=10)

# Student Details
Label(root, text="Student Name").pack()
entry_name = Entry(root, width=30)
entry_name.pack()

Label(root, text="Roll Number").pack()
entry_roll = Entry(root, width=30)
entry_roll.pack()

# Subject Marks
Label(root, text="Subject 1 Marks").pack()
entry_m1 = Entry(root, width=30)
entry_m1.pack()

Label(root, text="Subject 2 Marks").pack()
entry_m2 = Entry(root, width=30)
entry_m2.pack()

Label(root, text="Subject 3 Marks").pack()
entry_m3 = Entry(root, width=30)
entry_m3.pack()

Label(root, text="Subject 4 Marks").pack()
entry_m4 = Entry(root, width=30)
entry_m4.pack()

Label(root, text="Subject 5 Marks").pack()
entry_m5 = Entry(root, width=30)
entry_m5.pack()

# Button
Button(root, text="Calculate Result",
       command=calculate_result,
       bg="green", fg="white").pack(pady=15)

# Output Label
output = Label(root, text="", font=("Arial", 12))
output.pack(pady=20)

root.mainloop()
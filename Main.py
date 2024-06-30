import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def mainscript():   
    def execute_code1():
        from Grades import main_function_code1
        root.destroy()
        main_function_code1()
    def execute_code2():
        from Attendance import main_function_code2
        root.destroy()

        main_function_code2()

    def feedback_system():

        from Survay import main_function_code3
        root.destroy()
        main_function_code3()

    root = tk.Tk()
    root.title("Teacher's guide")
    root.geometry("300x150")

    frame = ttk.Frame(root)
    frame.pack(expand=True, fill="both")

    label = ttk.Label(frame, text="Choose an option:")
    label.pack(pady=10)

    button_grades = ttk.Button(frame, text="Grades", command=execute_code1)
    button_grades.pack(pady=5)

    button_attendance = ttk.Button(frame, text="Attendance", command=execute_code2)
    button_attendance.pack(pady=5)

    button_feedback = ttk.Button(frame, text="Survey", command=feedback_system)
    button_feedback.pack(pady=5)

    root.mainloop()



if __name__ == "__main__":
    mainscript()
import tkinter as tk
import tkinter as tk
from tkinter import messagebox,ttk
from Main import mainscript
def main_function_code1():
    def save_data():
        student_name = name_entry.get()
        student_id = id_entry.get()
        assignment_grade = assignment_entry.get()
        midterm_grade = midterm_entry.get()
        final_grade = final_entry.get()

        # Save data to text file
        with open("student_grades.txt", "a") as file:
            file.write(f"Student Name: {student_name}\n")
            file.write(f"Student ID: {student_id}\n")
            file.write(f"Assignment Grade: {assignment_grade}\n")
            file.write(f"Midterm Grade: {midterm_grade}\n")
            file.write(f"Final Grade: {final_grade}\n")
            file.write("-" * 50 + "\n")  # Separator for different entries

        messagebox.showinfo("Success", "Data saved successfully!")

    def open_add_grades_window():
        add_grades_window = tk.Toplevel()
        add_grades_window.title("Add Grades")

        # Labels and Entry Widgets
        tk.Label(add_grades_window, text="Student Name:").pack(pady=5)
        global name_entry
        name_entry = tk.Entry(add_grades_window)
        name_entry.pack(pady=5)

        tk.Label(add_grades_window, text="Student ID:").pack(pady=5)
        global id_entry
        id_entry = tk.Entry(add_grades_window)
        id_entry.pack(pady=5)

        tk.Label(add_grades_window, text="Assignment Grade (0-40):").pack(pady=5)
        global assignment_entry
        assignment_entry = tk.Entry(add_grades_window)
        assignment_entry.pack(pady=5)

        tk.Label(add_grades_window, text="Midterm Grade (0-40):").pack(pady=5)
        global midterm_entry
        midterm_entry = tk.Entry(add_grades_window)
        midterm_entry.pack(pady=5)

        tk.Label(add_grades_window, text="Final Grade (0-100):").pack(pady=5)
        global final_entry
        final_entry = tk.Entry(add_grades_window)
        final_entry.pack(pady=5)

        # Save Button
        save_button = tk.Button(add_grades_window, text="Save", command=save_data)
        save_button.pack(pady=20)
    def fetch_grades_for_id():
        target_id = id_to_fetch.get()
        found = False
        with open("student_grades.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):  # Each student entry is 6 lines long
                if f"Student ID: {target_id}\n" in lines[i + 1]:
                    found = True
                    grades_info = "".join(lines[i:i + 5])  # Extracting grades for the ID
                    messagebox.showinfo("Grades Info", grades_info)
                    break
        if not found:
            messagebox.showerror("Error", "No grades found for the entered ID.")

    def open_fetch_grades_window():
        fetch_window = tk.Toplevel()
        fetch_window.title("Fetch Grades by ID")

        tk.Label(fetch_window, text="Enter Student ID to fetch grades:").pack(pady=10)
        
        global id_to_fetch
        id_to_fetch = tk.Entry(fetch_window)
        id_to_fetch.pack(pady=10)

        fetch_button = tk.Button(fetch_window, text="Fetch Grades", command=fetch_grades_for_id)
        fetch_button.pack(pady=10)
    def show_all_grades():
        all_grades_window = tk.Toplevel()
        all_grades_window.title("All Grades")

        text_widget = tk.Text(all_grades_window, height=20, width=50)
        text_widget.pack(padx=10, pady=10)

        try:
            with open("student_grades.txt", "r") as file:
                text_widget.insert(tk.END, file.read())
        except FileNotFoundError:
            messagebox.showerror("Error", "No grades data found.")
    def delete_grades_for_id():
        target_id = id_to_delete.get()
        lines_to_keep = []
        found = False

        try:
            with open("student_grades.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 6):  # Each student entry is 6 lines long
                    if f"Student ID: {target_id}\n" not in lines[i + 1]:
                        lines_to_keep.extend(lines[i:i + 6])
                    else:
                        found = True
                if found:
                    with open("student_grades.txt", "w") as file:
                        file.writelines(lines_to_keep)
                    messagebox.showinfo("Success", f"Grades for ID {target_id} deleted successfully.")
                else:
                    messagebox.showerror("Error", "No grades found for the entered ID.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No grades data found.")

    def open_delete_grades_window():
        delete_window = tk.Toplevel()
        delete_window.title("Delete Grades by ID")

        tk.Label(delete_window, text="Enter Student ID to delete grades:").pack(pady=10)
        
        global id_to_delete
        id_to_delete = tk.Entry(delete_window)
        id_to_delete.pack(pady=10)

        delete_button = tk.Button(delete_window, text="Delete", command=delete_grades_for_id)
        delete_button.pack(pady=10)
    def update_grades_for_id():
        target_id = id_to_update.get()
        new_assignment_grade = new_assignment_entry.get()
        new_midterm_grade = new_midterm_entry.get()
        new_final_grade = new_final_entry.get()
        found = False
        lines_to_keep = []

        try:
            with open("student_grades.txt", "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 6):  # Each student entry is 6 lines long
                    if f"Student ID: {target_id}\n" not in lines[i + 1]:
                        lines_to_keep.extend(lines[i:i + 6])
                    else:
                        found = True
                        updated_lines = [
                            f"Student Name: {lines[i].split(': ')[1].strip()}",
                            f"Student ID: {target_id}",
                            f"Assignment Grade: {new_assignment_grade}\n",
                            f"Midterm Grade: {new_midterm_grade}\n",
                            f"Final Grade: {new_final_grade}\n",
                            "-" * 50 + "\n"
                        ]
                        lines_to_keep.extend(updated_lines)

            if found:
                with open("student_grades.txt", "w") as file:
                    file.writelines(lines_to_keep)
                messagebox.showinfo("Success", f"Grades for ID {target_id} updated successfully.")
            else:
                messagebox.showerror("Error", "No grades found for the entered ID.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No grades data found.")

    def open_update_grades_window():
        update_window = tk.Toplevel()
        update_window.title("Update Grades by ID")

        tk.Label(update_window, text="Enter Student ID to update grades:").pack(pady=10)
        
        global id_to_update, new_assignment_entry, new_midterm_entry, new_final_entry

        id_to_update = tk.Entry(update_window)
        id_to_update.pack(pady=5)

        tk.Label(update_window, text="New Assignment Grade (0-40):").pack(pady=5)
        new_assignment_entry = tk.Entry(update_window)
        new_assignment_entry.pack(pady=5)

        tk.Label(update_window, text="New Midterm Grade (0-40):").pack(pady=5)
        new_midterm_entry = tk.Entry(update_window)
        new_midterm_entry.pack(pady=5)

        tk.Label(update_window, text="New Final Grade (0-100):").pack(pady=5)
        new_final_entry = tk.Entry(update_window)
        new_final_entry.pack(pady=5)

        update_button = tk.Button(update_window, text="Update", command=update_grades_for_id)
        update_button.pack(pady=10)
    def run_mainscript():
        root.destroy()
        mainscript()

        # Create the main window
    root = tk.Tk()
    root.title("Grades")
    root.geometry("286x567")

    # Create a Frame to act as central widget
    central_frame = tk.Frame(root)
    central_frame.pack(pady=20)

    # Create Buttons
    button1 = tk.Button(central_frame, text="Add grades", width=30, height=2)
    button1.pack(pady=10)

    button2 = tk.Button(central_frame, text="Inform A Grade", width=30, height=2)
    button2.pack(pady=10)

    button3 = tk.Button(central_frame, text="Show all grades", width=30, height=2)
    button3.pack(pady=10)

    button4 = tk.Button(central_frame, text="Delete student grade", width=30, height=2)
    button4.pack(pady=10)

    button5 = tk.Button(central_frame, text="Update a grade", width=30, height=2)
    button5.pack(pady=10)

    button6 = tk.Button(central_frame, text="Back to the main Window", width=30, height=2, command=root.quit)
    button6.pack(pady=10)

    # Create a Menu Bar (empty as an example)
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    
        # Create a Status Bar Label at the bottom
    status_bar = tk.Label(root, text="Ahmed Hamdy Kotp", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    button1.config(command=open_add_grades_window)
    button2.config(command=open_fetch_grades_window)  # Modify button2 command
    button3.config(command=show_all_grades)  # Modify button3 command
    button4.config(command=open_delete_grades_window)  # Add command for button4
    button5.config(command=open_update_grades_window)  # Add command for button5
    button6.config(command=run_mainscript)


        # Start the main event loop
    root.mainloop()

    
       
if __name__ == "__main__":
    main_function_code1()
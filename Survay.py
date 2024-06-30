import tkinter as tk
from tkinter import messagebox
from Main import mainscript
def main_function_code3():
    feedback = []
    file_path = "feedback_system.txt"
    def save_feedback():
        with open(file_path, 'w') as file:
            for entry in feedback:
                file.write(f"Student Name: {entry['Student Name']}\n")
                file.write(f"Lecture Rating: {entry['Lecture Rating']}\n")
                file.write(f"Comments: {entry['Comments']}\n")
                file.write("-" * 20 + "\n")
    def load_feedback():
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                feedback.clear()
                entry = {}
                for line in lines:
                    if line.startswith("Student Name:"):
                        entry['Student Name'] = line.split(":")[1].strip()
                    elif line.startswith("Lecture Rating:"):
                        entry['Lecture Rating'] = int(line.split(":")[1].strip())
                    elif line.startswith("Comments:"):
                        entry['Comments'] = line.split(":")[1].strip()
                    elif line.startswith("-" * 20):
                        feedback.append(entry)
                        entry = {}
        except FileNotFoundError:
            pass
    def add_feedback():
        top = tk.Toplevel(root)
        top.title("Add Feedback")
        top.configure(bg='#3498db')  # Blue background
        tk.Label(top, text="Student Name:", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        student_name_entry = tk.Entry(top)
        student_name_entry.pack(pady=5)
        tk.Label(top, text="Lecture Rating (1-5):", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        lecture_rating_entry = tk.Entry(top)
        lecture_rating_entry.pack(pady=5)
        tk.Label(top, text="Comments:", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        comments_entry = tk.Entry(top)
        comments_entry.pack(pady=5)
        submit_button = tk.Button(top, text="Submit", command=lambda: submit_feedback(
            student_name_entry.get(),
            lecture_rating_entry.get(),
            comments_entry.get(),
            top
        ), bg='#2ecc71', fg='#ecf0f1')
        submit_button.pack(pady=10)
    def submit_feedback(student_name, lecture_rating, comments, top):
        try:
            lecture_rating = int(lecture_rating)
            feedback_entry = {
                'Student Name': student_name,
                'Lecture Rating': lecture_rating,
                'Comments': comments
            }
            feedback.append(feedback_entry)
            save_feedback()
            messagebox.showinfo("Success", "Feedback submitted successfully!")
            top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for lecture rating.")
    def view_feedback():
        top = tk.Toplevel(root)
        top.title("View Feedback")
        top.configure(bg='#3498db')  # Blue background
        text = tk.Text(top, bg='#3498db', fg='#ecf0f1', font=('Arial', 12))
        text.pack()
        if not feedback:
            text.insert(tk.END, "No feedback available.")
        else:
            for index, entry in enumerate(feedback, 1):
                text.insert(tk.END, f"\nFeedback {index}:\n")
                for key, value in entry.items():
                    text.insert(tk.END, f"{key}: {value}\n")
                text.insert(tk.END, "-" * 20 + "\n")
    def delete_feedback():
        top = tk.Toplevel(root)
        top.title("Delete Feedback")
        top.configure(bg='#3498db')  # Blue background
        tk.Label(top, text="Enter student name to delete feedback ('all' to delete all):", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        student_name_entry = tk.Entry(top)
        student_name_entry.pack(pady=5)
        delete_button = tk.Button(top, text="Delete", command=lambda: perform_delete_feedback(
            student_name_entry.get(),
            top
        ), bg='#c0392b', fg='#ecf0f1')
        delete_button.pack(pady=10)
    def perform_delete_feedback(student_name, top):
        if student_name.lower() == "all":
            feedback.clear()
            save_feedback()
            messagebox.showinfo("Success", "All feedback entries deleted successfully!")
        else:
            found_entries = [entry for entry in feedback if entry['Student Name'] == student_name]
            if not found_entries:
                messagebox.showerror("Error", f"No feedback found for {student_name}.")
            else:
                for entry in found_entries:
                    feedback.remove(entry)
                save_feedback()
                messagebox.showinfo("Success", f"Feedback for {student_name} deleted successfully.")
        top.destroy()
    def edit_feedback():
        top = tk.Toplevel(root)
        top.title("Edit Feedback")
        top.configure(bg='#3498db')  # Blue background
        tk.Label(top, text="Enter student name to edit feedback ('all' to delete all):", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        student_name_entry = tk.Entry(top)
        student_name_entry.pack(pady=5)
        edit_button = tk.Button(top, text="Edit", command=lambda: perform_edit_feedback(
            student_name_entry.get(),
            top
        ), bg='#e74c3c', fg='#ecf0f1')
        edit_button.pack(pady=10)
    def perform_edit_feedback(student_name, top):
        if student_name.lower() == "all":
            feedback.clear()
            save_feedback()
            messagebox.showinfo("Success", "All feedback entries deleted successfully!")
        else:
            found_entries = [entry for entry in feedback if entry['Student Name'] == student_name]
            if not found_entries:
                messagebox.showerror("Error", f"No feedback found for {student_name}.")
            else:
                top.destroy()
                edit_feedback_window(student_name, found_entries)
    def edit_feedback_window(student_name, entries):
        top = tk.Toplevel(root)
        top.title(f"Editing Feedback for {student_name}")
        top.configure(bg='#3498db')  # Blue background
        text = tk.Text(top, bg='#3498db', fg='#ecf0f1', font=('Arial', 12))
        text.pack()
        tk.Label(top, text="Enter new lecture rating (1-5):", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        lecture_rating_entry = tk.Entry(top)
        lecture_rating_entry.pack(pady=5)
        tk.Label(top, text="Enter new comments:", bg='#3498db', fg='#ecf0f1', font=('Arial', 12)).pack(pady=5)
        comments_entry = tk.Entry(top)
        comments_entry.pack(pady=5)
        submit_button = tk.Button(top, text="Submit", command=lambda: submit_edit_feedback(
            student_name,
            entries,
            lecture_rating_entry.get(),
            comments_entry.get(),
            top
        ), bg='#2ecc71', fg='#ecf0f1')
        submit_button.pack(pady=10)
    def submit_edit_feedback(student_name, entries, lecture_rating, comments, top):
        try:
            lecture_rating = int(lecture_rating)
            if 1 <= lecture_rating <= 5:
                for entry in entries:
                    entry['Lecture Rating'] = lecture_rating
                    entry['Comments'] = comments
                save_feedback()
                messagebox.showinfo("Success", f"Feedback for {student_name} edited successfully!")
                top.destroy()
            else:
                messagebox.showerror("Error", "Please enter a valid lecture rating (1-5).")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for lecture rating.")
    def main():
        global root
        root = tk.Tk()
        root.title ("Feedback management")# Set the size of the window
        root.geometry("400x400") # Set background color
        root.configure(bg='#3498db')  # Blue background
        label = tk.Label(root, text="Feedback System", bg='#3498db', fg='#ecf0f1', font=('Arial', 16))
        label.pack(pady=10)
        status_bar = tk.Label(root, text="Abdulrahman mohamed", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        button_add = tk.Button(root, text="Add Feedback", command=add_feedback, bg='#2ecc71', fg='#ecf0f1')
        button_add.pack(pady=5)
        button_view = tk.Button(root, text="View Feedback", command=view_feedback, bg='#f39c12', fg='#ecf0f1')
        button_view.pack(pady=5)
        button_edit = tk.Button(root, text="Edit Feedback", command=edit_feedback, bg='#e74c3c', fg='#ecf0f1')
        button_edit.pack(pady=5)
        button_delete = tk.Button(root, text="Delete Feedback", command=delete_feedback, bg='#c0392b', fg='#ecf0f1')
        button_delete.pack(pady=5)
        button_exit = tk.Button(root, text="Exit", command=run_mainscript, bg='#7f8c8d', fg='#ecf0f1')
        button_exit.pack(pady=10)
    
        load_feedback()  # Load existing feedback data
        root.mainloop()
    def run_mainscript():
        root.destroy()
        mainscript()

    main()

if __name__ == "__main__":
    main_function_code3()
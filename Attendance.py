import tkinter as tk
from tkinter import ttk, messagebox
from Main import mainscript  # Assuming Main is the file containing the mainscript function

def main_function_code2():
    def calculate_percentage(attend_id):
        try:
            with open("attendance_data.txt", "r") as file:
                lines = file.readlines()

            total_entries = 0
            present_entries = 0

            for line in lines:
                _, existing_attendid, _, attendstate = line.strip().split(" = ")

                if existing_attendid == attend_id:
                    total_entries += 1
                    if attendstate.lower() == 'present':
                        present_entries += 1

            if total_entries == 0:
                print(f"No attendance records found for student ID {attend_id}.")
                messagebox.showinfo("Information", f"No attendance records found for student ID {attend_id}.")
            else:
                percentage = (present_entries / total_entries) * 100
                print(f"Attendance percentage for student ID {attend_id}: {percentage:.2f}%")
                messagebox.showinfo("Attendance Percentage", f"Attendance percentage for student ID {attend_id}: {percentage:.2f}%")

        except FileNotFoundError:
            print("File 'attendance_data.txt' not found.")
            messagebox.showerror("Error", "File 'attendance_data.txt' not found.")

    def attend_add(date, attendid, attendname, attendstate):
        try:
            with open("attendance_data.txt", "a") as attendance:
                attendance_record = f"{date} = {attendid} = {attendname} = {attendstate}\n"
                attendance.write(attendance_record)
            print("Attendance recorded successfully.")
            messagebox.showinfo("Success", "Attendance recorded successfully.")
        except FileNotFoundError:
            print("File 'attendance_data.txt' not found.")
            messagebox.showerror("Error", "File 'attendance_data.txt' not found.")

    def attend_show():
        try:
            with open("attendance_data.txt", "r") as file:
                lines = file.readlines()

            if not lines:
                print("Attendance data is empty.")
                messagebox.showinfo("Information", "Attendance data is empty.")
            else:
                show_table_text.config(state=tk.NORMAL)
                show_table_text.delete(1.0, tk.END)
                show_table_text.insert(tk.END, "{:<12} {:<12} {:<20} {:<10}\n".format("Date", "Student ID", "Student Name", "Attendance"))
                show_table_text.insert(tk.END, "=" * 58 + "\n")
                for line in lines:
                    date, attendid, attendname, attendstate = line.strip().split(" = ")
                    show_table_text.insert(tk.END, "{:<12} {:<12} {:<20} {:<10}\n".format(date, attendid, attendname, attendstate))
                show_table_text.config(state=tk.DISABLED)
        except FileNotFoundError:
            print("Attendance file not found.")
            messagebox.showerror("Error", "Attendance file not found.")

    def attend_update(date, attendid, attendstate):
        try:
            with open("attendance_data.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_records = []

            for line in lines:
                record_data = line.strip().split(" = ")
                existing_date, existing_attendid, student_name, existing_state = record_data

                if existing_attendid == attendid and existing_date == date:
                    found = True
                    updated_record = f"{date} = {attendid} = {student_name} = {attendstate}\n"
                    updated_records.append(updated_record)
                else:
                    updated_records.append(line)

            if not found:
                print(f"No matching record found for student ID {attendid} on {date}.")
                messagebox.showinfo("Information", f"No matching record found for student ID {attendid} on {date}.")
            else:
                with open("attendance_data.txt", "w") as file:
                    file.writelines(updated_records)

                print("Attendance updated successfully.")
                messagebox.showinfo("Success", "Attendance updated successfully.")

        except FileNotFoundError:
            print("File 'attendance_data.txt' not found.")
            messagebox.showerror("Error", "File 'attendance_data.txt' not found.")

    def attend_delete(date, attendid):
        try:
            with open("attendance_data.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_records = []

            for line in lines:
                record_data = line.strip().split(" = ")
                existing_date, existing_attendid, _, _ = record_data

                if existing_attendid == attendid and existing_date == date:
                    found = True
                    print("Record deleted successfully.")
                    messagebox.showinfo("Success", "Record deleted successfully.")
                else:
                    updated_records.append(line)

            if not found:
                print(f"No matching record found for student ID {attendid} on {date}.")
                messagebox.showinfo("Information", f"No matching record found for student ID {attendid} on {date}.")

            with open("attendance_data.txt", "w") as file:
                file.writelines(updated_records)

        except FileNotFoundError:
            print("File 'attendance_data.txt' not found.")
            messagebox.showerror("Error", "File 'attendance_data.txt' not found.")

    def run_mainscript():
        root.destroy()
        mainscript()

    root = tk.Tk()
    root.title("Attendance Management")
    root.geometry("600x600")

    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    record_tab = ttk.Frame(notebook)
    show_tab = ttk.Frame(notebook)
    update_tab = ttk.Frame(notebook)
    delete_tab = ttk.Frame(notebook)
    percentage_tab = ttk.Frame(notebook)



    notebook.add(record_tab, text='Record Attendance')
    notebook.add(show_tab, text='Show Attendance Table')
    notebook.add(update_tab, text='Update Attendance Record')
    notebook.add(delete_tab, text='Delete Attendance Record')
    notebook.add(percentage_tab, text='Attendance Percentage')

    record_tab.grid_rowconfigure(1, weight=0)
    record_tab.grid_columnconfigure(1, weight=1)
    show_tab.grid_rowconfigure(1, weight=0)
    show_tab.grid_columnconfigure(1, weight=1)
    update_tab.grid_rowconfigure(1, weight=0)
    update_tab.grid_columnconfigure(1, weight=1)
    delete_tab.grid_rowconfigure(1, weight=0)
    delete_tab.grid_columnconfigure(1, weight=1)

    date_entry = ttk.Entry(record_tab)
    name_entry = ttk.Entry(record_tab)
    id_entry = ttk.Entry(record_tab)
    state_entry = ttk.Entry(record_tab)
    percentage_id_entry = ttk.Entry(percentage_tab)


    ttk.Label(record_tab, text="Date (YYYY-MM-DD):").grid(column=0, row=0, padx=10, pady=10, sticky='e')
    date_entry.grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(record_tab, text="Student Name:").grid(column=0, row=1, padx=10, pady=10, sticky='e')
    name_entry.grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(record_tab, text="Student ID:").grid(column=0, row=2, padx=10, pady=10, sticky='e')
    id_entry.grid(column=1, row=2, padx=10, pady=10)

    ttk.Label(record_tab, text="Attendance State (Present/Absence):").grid(column=0, row=3, padx=10, pady=10, sticky='e')
    state_entry.grid(column=1, row=3, padx=10, pady=10)
    

    def record_attendance():
        date = date_entry.get()
        name = name_entry.get()
        id = id_entry.get()
        state = state_entry.get()

        attend_add(date, id, name, state)

    exit_button = tk.Button(root, text="Exit", command=run_mainscript)
    exit_button.pack()
    status_bar = tk.Label(root, text="Abdullah ayman", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    record_button = ttk.Button(record_tab, text="Record Attendance", command=record_attendance)
    record_button.grid(column=1, row=4, pady=10)

    show_table_text = tk.Text(show_tab, height=20, width=80, state=tk.DISABLED)
    show_table_text.grid(row=1, column=0, padx=10, pady=10)

    show_button = ttk.Button(show_tab, text="Show Attendance Table", command=attend_show)
    show_button.grid(row=2, column=0, pady=10)

    update_id_entry = ttk.Entry(update_tab)
    update_date_entry = ttk.Entry(update_tab)
    update_state_entry = ttk.Entry(update_tab)

    ttk.Label(update_tab, text="Student ID:").grid(column=0, row=0, padx=10, pady=10, sticky='e')
    update_id_entry.grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(update_tab, text="Date (YYYY-MM-DD):").grid(column=0, row=1, padx=10, pady=10, sticky='e')
    update_date_entry.grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(update_tab, text="New Attendance State (Present/Absence):").grid(column=0, row=2, padx=10, pady=10, sticky='e')
    update_state_entry.grid(column=1, row=2, padx=10, pady=10)

    def update_attendance():
        id = update_id_entry.get()
        date = update_date_entry.get()
        state = update_state_entry.get()

        attend_update(date, id, state)

    update_button = ttk.Button(update_tab, text="Update Attendance", command=update_attendance)
    update_button.grid(column=1, row=3, pady=10)

    delete_id_entry = ttk.Entry(delete_tab)
    delete_date_entry = ttk.Entry(delete_tab)

    ttk.Label(delete_tab, text="Student ID:").grid(column=0, row=0, padx=10, pady=10, sticky='e')
    delete_id_entry.grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(delete_tab, text="Date (YYYY-MM-DD):").grid(column=0, row=1, padx=10, pady=10, sticky='e')
    delete_date_entry.grid(column=1, row=1, padx=10, pady=10)

    def delete_attendance():
        id = delete_id_entry.get()
        date = delete_date_entry.get()

        attend_delete(date, id)

    delete_button = ttk.Button(delete_tab, text="Delete Attendance Record", command=delete_attendance)
    delete_button.grid(column=1, row=2, pady=10)
    percentage_id_entry.grid(column=1, row=0, padx=10, pady=10)
    ttk.Label(percentage_tab, text="Student ID:").grid(column=0, row=0, padx=10, pady=10, sticky='e')

    def calculate_percentage_button():
        attend_id = percentage_id_entry.get()
        calculate_percentage(attend_id)

    calculate_percentage_button = ttk.Button(percentage_tab, text="Calculate Percentage", command=calculate_percentage_button)
    calculate_percentage_button.grid(column=1, row=1, pady=10)


    root.mainloop()

if __name__ == "__main__":
    main_function_code2()

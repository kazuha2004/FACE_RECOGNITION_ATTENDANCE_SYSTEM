import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Report")
        self.root.geometry("1500x790+0+0")
        self.root.configure(bg="#f4f4f9")

        # Back button
        back_btn = ttk.Button(root, text="Back", command=self.go_back, style="TButton")
        back_btn.place(x=1400, y=9, width=80, height=30)

        # Sample data list
        self.sample_data = []

        # Apply custom styles
        self.setup_style()

        # UI Setup
        self.setup_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Treeview style
        style.configure("Treeview",
                        background="#dfe6e9",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#dfe6e9")
        style.map("Treeview", background=[('selected', '#74b9ff')])

        # Button style
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=4,
                        bg='gray',
                        fg='white')

    def setup_ui(self):
        # Import button
        self.import_button = ttk.Button(self.root, text="Import CSV", command=self.import_csv)
        self.import_button.pack(pady=20)

        # Report Treeview Frame
        tree_frame = tk.Frame(self.root, bg="#f4f4f9")
        tree_frame.pack(pady=20, padx=20, expand=True, fill="both")

        # Updated: Added "Period" as a new column
        self.report_tree = ttk.Treeview(tree_frame, columns=("Student ID", "Class ID", "Student Name", "Department", "Time", "Date", "Status", "Period"), show="headings")
        self.report_tree.heading("Student ID", text="Student ID")
        self.report_tree.heading("Class ID", text="Class ID")
        self.report_tree.heading("Student Name", text="Student Name")
        self.report_tree.heading("Department", text="Department")  # Assuming this is the 4th column from the CSV
        self.report_tree.heading("Time", text="Time")
        self.report_tree.heading("Date", text="Date")
        self.report_tree.heading("Status", text="Status")
        self.report_tree.heading("Period", text="Period")  # New column for "Period"
        self.report_tree.pack(expand=True, fill="both")

        # Graph Frame
        self.graph_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.graph_frame.pack(pady=20, padx=20)

    def import_csv(self):
        """Function to import attendance data from a CSV file."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")], parent=self.root)
        if file_path:
            try:
                # Clear previous data
                self.sample_data.clear()
                for item in self.report_tree.get_children():
                    self.report_tree.delete(item)

                # Read the CSV file (DO NOT SKIP THE FIRST ROW)
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file)

                    for row in reader:
                        # Debugging: Print the row being read
                        print(f"Row: {row}")

                        # Check for valid row length (expecting 8 columns: Student ID, Class ID, Student Name, Department, Time, Date, Status, Period)
                        if len(row) == 8:
                            # Insert all 8 values into sample data
                            self.sample_data.append(tuple(row))

                            # Insert all 8 values into Treeview
                            self.report_tree.insert("", tk.END, values=row)
                        else:
                            print(f"Skipping invalid row: {row}")

                # Generate the graph based on the imported data
                self.show_graph()
                messagebox.showinfo("Success", "Data imported successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while importing data: {str(e)}", parent=self.root)

    def show_graph(self):
        """Function to generate a graph based on the attendance data."""
        # Initialize a dictionary to count attendance statuses by period
        periods = {f"Period {i}": {'Present': 0, 'Absent': 0, 'Late': 0} for i in range(1, 9)}

        # Populate the period data
        for row in self.sample_data:
            period = row[7]  # Period is now the 8th element in the row
            status = row[6].capitalize()  # Status: Present, Absent, Late
            if period in periods and status in periods[period]:
                periods[period][status] += 1

        # Create a stacked bar chart for each period
        labels = list(periods.keys())
        present_count = [periods[period]['Present'] for period in labels]
        absent_count = [periods[period]['Absent'] for period in labels]
        late_count = [periods[period]['Late'] for period in labels]

        fig, ax = plt.subplots(figsize=(8, 6))

        ax.bar(labels, present_count, label='Present', color='#55efc4')
        ax.bar(labels, absent_count, label='Absent', color='#ff7675', bottom=present_count)
        ax.bar(labels, late_count, label='Late', color='#ffeaa7', bottom=[i + j for i, j in zip(present_count, absent_count)])

        ax.set_ylabel('Number of Students')
        ax.set_title('Attendance by Period')
        ax.legend()

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Add the new graph
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def go_back(self):
        """Close the current window."""
        try:
            self.root.destroy()  # Close the window
        except Exception as e:
            print(f"Error when trying to close the window: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Developer(root)
    root.mainloop()

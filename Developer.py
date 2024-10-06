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
        self.root.configure(bg="#f4f4f9")  # Light gray background for better contrast

        # Sample data list
        self.sample_data = []

        # Apply custom styles
        self.setup_style()

        # UI Setup
        self.setup_ui()

    def setup_style(self):
        """Configure style for ttk widgets."""
        style = ttk.Style()
        style.theme_use("clam")  # Using a modern theme
        
        # Treeview style
        style.configure("Treeview",
                        background="#dfe6e9",  # light background for treeview rows
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#dfe6e9")  # Background of cells
        style.map("Treeview", background=[('selected', '#74b9ff')])  # Blue color on select

        # Button style
        style.configure("TButton",
                        font=("Helvetica", 12),
                        padding=10,
                        background="#0984e3",
                        foreground="white")

    def setup_ui(self):
        """Set up the UI with buttons, treeview, and graph."""
        # Import button
        self.import_button = ttk.Button(self.root, text="Import CSV", command=self.import_csv)
        self.import_button.pack(pady=20)

        # Report Treeview Frame
        tree_frame = tk.Frame(self.root, bg="#f4f4f9")
        tree_frame.pack(pady=20, padx=20, expand=True, fill="both")

        self.report_tree = ttk.Treeview(tree_frame, columns=("ID", "Student ID", "Student Name", "Class ID", "Time", "Date", "Status"), show="headings")
        self.report_tree.heading("ID", text="ID")
        self.report_tree.heading("Student ID", text="Student ID")
        self.report_tree.heading("Student Name", text="Student Name")
        self.report_tree.heading("Class ID", text="Class ID")
        self.report_tree.heading("Time", text="Time")
        self.report_tree.heading("Date", text="Date")
        self.report_tree.heading("Status", text="Status")
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

                # Read the CSV file
                with open(file_path, mode='r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row
                    for row in reader:
                        # Assuming CSV structure: ID, Student ID, Student Name, Class ID, Time, Date, Status
                        if len(row) == 7:
                            self.sample_data.append(tuple(row))
                            self.report_tree.insert("", tk.END, values=row)

                # Generate the graph based on the imported data
                self.show_graph()
                messagebox.showinfo("Success", "Data imported successfully!", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while importing data: {str(e)}", parent=self.root)

    def show_graph(self):
        """Function to generate a graph based on the attendance data."""
        # Count the attendance statuses
        present_count = sum(1 for row in self.sample_data if row[6].lower() == "present")
        absent_count = sum(1 for row in self.sample_data if row[6].lower() == "absent")
        late_count = sum(1 for row in self.sample_data if row[6].lower() == "late")

        # Create a bar chart
        labels = ['Present', 'Absent', 'Late']
        counts = [present_count, absent_count, late_count]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(labels, counts, color=['#55efc4', '#ff7675', '#ffeaa7'])
        ax.set_ylabel('Count')
        ax.set_title('Attendance Status')

        # Clear previous graph
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        # Add the new graph
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Developer(root)
    root.mainloop()

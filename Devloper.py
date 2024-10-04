from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import cv2
import mysql.connector
import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from tkinter import filedialog, messagebox

# Developer Class with Reports & Analytics on the same page
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # Create a frame to hold all content using grid layout
        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=TRUE)

        # Heading
        title_lbl = Label(main_frame, text="Developer & Reports Analytics", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.grid(row=0, column=0, columnspan=2, pady=20)

        # Report Type Dropdown
        report_type_label = Label(main_frame, text="Select Report Type:", font=("times new roman", 15, "bold"))
        report_type_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.report_type_var = StringVar()
        self.report_type_dropdown = ttk.Combobox(main_frame, textvariable=self.report_type_var, values=["daily", "weekly", "monthly", "student-specific"], state='readonly')
        self.report_type_dropdown.grid(row=1, column=1, padx=10, pady=10)
        self.report_type_dropdown.current(0)

        # Date Range Inputs
        start_date_label = Label(main_frame, text="Start Date (YYYY-MM-DD):", font=("times new roman", 15, "bold"))
        start_date_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.start_date_entry = Entry(main_frame, font=("times new roman", 15))
        self.start_date_entry.grid(row=2, column=1, padx=10, pady=10)

        end_date_label = Label(main_frame, text="End Date (YYYY-MM-DD):", font=("times new roman", 15, "bold"))
        end_date_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.end_date_entry = Entry(main_frame, font=("times new roman", 15))
        self.end_date_entry.grid(row=3, column=1, padx=10, pady=10)

        # Student ID Input (only for student-specific reports)
        self.student_id_label = Label(main_frame, text="Student ID:", font=("times new roman", 15, "bold"))
        self.student_id_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.student_id_entry = Entry(main_frame, font=("times new roman", 15))
        self.student_id_entry.grid(row=4, column=1, padx=10, pady=10)
        self.student_id_label.grid_remove()
        self.student_id_entry.grid_remove()

        # Show/hide Student ID entry based on report type
        self.report_type_var.trace("w", self.update_fields)

        # Button to generate report
        generate_button = Button(main_frame, text="Generate Report", command=self.generate_report, font=("times new roman", 15, "bold"), bg="blue", fg="white")
        generate_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Button to import CSV
        import_button = Button(main_frame, text="Import CSV", command=self.import_csv, font=("times new roman", 15, "bold"), bg="purple", fg="white")
        import_button.grid(row=5, column=1, pady=20)

        # Create a frame for the report table with a scrollbar
        report_frame = Frame(main_frame)
        report_frame.grid(row=6, column=0, columnspan=2, pady=20, sticky=W + E)

        # Scrollbar for the report table
        self.scrollbar = Scrollbar(report_frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Treeview for report
        self.report_tree = ttk.Treeview(report_frame, yscrollcommand=self.scrollbar.set)
        self.report_tree.pack(fill=BOTH, expand=TRUE)

        # Configure scrollbar
        self.scrollbar.config(command=self.report_tree.yview)

        # Define columns for the Treeview
        self.report_tree['columns'] = ("ID", "Student ID", "Student Name", "Class ID", "Time", "Date", "Status")
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("ID", anchor=CENTER, width=80)
        self.report_tree.column("Student ID", anchor=CENTER, width=120)
        self.report_tree.column("Student Name", anchor=CENTER, width=120)
        self.report_tree.column("Class ID", anchor=CENTER, width=120)
        self.report_tree.column("Time", anchor=CENTER, width=100)
        self.report_tree.column("Date", anchor=CENTER, width=120)
        self.report_tree.column("Status", anchor=CENTER, width=100)

        self.report_tree.heading("#0", text="", anchor=CENTER)
        self.report_tree.heading("ID", text="ID", anchor=CENTER)
        self.report_tree.heading("Student ID", text="Student ID", anchor=CENTER)
        self.report_tree.heading("Student Name", text="Student Name", anchor=CENTER)
        self.report_tree.heading("Class ID", text="Class ID", anchor=CENTER)
        self.report_tree.heading("Time", text="Time", anchor=CENTER)
        self.report_tree.heading("Date", text="Date", anchor=CENTER)
        self.report_tree.heading("Status", text="Status", anchor=CENTER)

        # Sample attendance data for display
        self.sample_data = []

        # Create a frame to hold the attendance report graph
        graph_frame = Frame(main_frame)
        graph_frame.grid(row=6, column=2, pady=20, sticky=W + E)

        # Create a canvas for the graph
        self.graph_canvas = Canvas(graph_frame, width=400, height=300)  # Reduced size for better visibility
        self.graph_canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

    def update_fields(self, *args):
        """Update input fields based on the selected report type."""
        if self.report_type_var.get() == "student-specific":
            self.student_id_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
            self.student_id_entry.grid(row=4, column=1, padx=10, pady=10)
        else:
            self.student_id_label.grid_remove()
            self.student_id_entry.grid_remove()

    def generate_report(self):
        """Function to generate the report based on user inputs."""
        # Clear previous data in the Treeview
        for item in self.report_tree.get_children():
            self.report_tree.delete(item)

        # Here you would implement the logic to fetch and display the relevant report data
        # For demonstration, we just print the input values
        report_type = self.report_type_var.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        student_id = self.student_id_entry.get()

        print(f"Report Type: {report_type}, Start Date: {start_date}, End Date: {end_date}, Student ID: {student_id}")

        # Add sample data to the Treeview
        for row in self.sample_data:
            self.report_tree.insert("", END, values=row)

        # Generate the graph based on the sample data
        self.show_graph()

    def import_csv(self):
        """Function to import attendance data from a CSV file."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
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
                            self.report_tree.insert("", END, values=row)

                # Generate the graph based on the imported data
                self.show_graph()
                messagebox.showinfo("Success", "Data imported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while importing data: {str(e)}")

    def show_graph(self):
        """Function to display the attendance graph."""
        # Clear the previous canvas if it exists
        self.graph_canvas.delete("all")

        # Create a figure for the graph
        fig = Figure(figsize=(5, 4), dpi=100)  # Adjusted size
        ax = fig.add_subplot(111)

        # Count Present and Absent statuses
        present_count = sum(1 for _, _, _, _, _, _, status in self.sample_data if status == "Present")
        absent_count = sum(1 for _, _, _, _, _, _, status in self.sample_data if status == "Absent")

        # Bar graph data
        categories = ['Present', 'Absent']
        values = [present_count, absent_count]

        ax.bar(categories, values, color=['green', 'red'])
        ax.set_ylabel('Number of Days')
        ax.set_title('Attendance Report')

        # Draw the figure on the canvas
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_canvas)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()

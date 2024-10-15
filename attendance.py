import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_period = StringVar()  # For period column

        # IMAGE 1 (Left side)
        img = Image.open(r"D:\wallpapers\attendence2.jpg")
        img = img.resize((750, 230), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=750, height=230)

        # IMAGE 2 (Right side)
        img1 = Image.open(r"D:\wallpapers\attendence3.jpg")
        img1 = img1.resize((750, 230), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=750, y=0, width=750, height=230)

        # Background image
        bg_img = Image.open(r"D:\wallpapers\bg.jpg")
        bg_img = bg_img.resize((1530, 710), Image.BILINEAR)
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photoimg)
        bg_label.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(root, text="ATTENDANCE MANAGEMENT SOFTWARE",
                          font=("Helvetica", 32, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        back_btn = Button(root, text="Back", command=self.go_back, font=("Helvetica", 12), bg='gray', fg='white')
        back_btn.place(x=1400, y=138, width=80, height=30)  # Adjust x and y for positioning

        # Main Frame
        main_frame = Frame(root, bd=2, bg="white")
        main_frame.place(x=10, y=180, width=1480, height=600)

        # Left frame
        LEFT_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("Helvetica", 12, "bold"))
        LEFT_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"D:\wallpapers\attendance1.jpg")
        img_left = img_left.resize((720, 130), Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=720, height=130)

        # Inner frame for details
        left_inside_frame = Frame(LEFT_frame, bd=2, relief="ridge", bg="white")
        left_inside_frame.place(x=5, y=140, width=720, height=400)

        # Attendance ID
        AttendanceID_label = Label(left_inside_frame, text="Attendance ID:", font=("Helvetica", 12, "bold"))
        AttendanceID_label.grid(row=0, column=0, padx=(10), pady=(10), sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("Helvetica", 12, "bold"))
        AttendanceID_entry.grid(row=0, column=1, padx=10, pady=(10), sticky=W)

        # Roll No
        roll_no_label = Label(left_inside_frame, text="Roll NO:", font=("Helvetica", 12, "bold"))
        roll_no_label.grid(row=0, column=2, padx=(10), pady=(10), sticky=W)

        roll_no_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_roll, font=("Helvetica", 12, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=10, pady=(10), sticky=W)

        # Student Name
        studentname_label = Label(left_inside_frame, text="Student Name:", font=("Helvetica", 12, "bold"))
        studentname_label.grid(row=2, column=0, padx=(10), pady=(10), sticky=W)

        studentname_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("Helvetica", 12, "bold"))
        studentname_entry.grid(row=2, column=1, padx=10, pady=(10), sticky=W)

        # Department
        department_label = Label(left_inside_frame, text="Department:", font=("Helvetica", 12, "bold"))
        department_label.grid(row=2, column=2, padx=(10), pady=(10), sticky=W)

        department_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("Helvetica", 12, "bold"))
        department_entry.grid(row=2, column=3, padx=10, pady=(10), sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("Helvetica", 12, "bold"))
        time_label.grid(row=3, column=0, padx=(10), pady=(10), sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("Helvetica", 12, "bold"))
        time_entry.grid(row=3, column=1, padx=10, pady=(10), sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("Helvetica", 12, "bold"))
        date_label.grid(row=3, column=2, padx=(10), pady=(5), sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("Helvetica", 12, "bold"))
        date_entry.grid(row=3, column=3, padx=10, pady=(5), sticky=W)

        # Attendance Status
        attendence_status_label = Label(left_inside_frame, text="Attendance:", font=("Helvetica", 12, "bold"))
        attendence_status_label.grid(row=4, column=0, padx=(10), pady=(10), sticky=W)

        status_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("Helvetica", 12, "bold"), width=18, state="readonly")
        status_combo["value"] = ("Status", "Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=4, column=1, padx=(10), pady=10, sticky=W)

        # Period
        period_label = Label(left_inside_frame, text="Period:", font=("Helvetica", 12, "bold"))
        period_label.grid(row=4, column=2, padx=(10), pady=(10), sticky=W)

        period_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_period, font=("Helvetica", 12, "bold"))
        period_entry.grid(row=4, column=3, padx=10, pady=(10), sticky=W)

        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=250, width=710, height=70)

        import_btn = Button(btn_frame, text="Import Csv", command=self.importCsv, width=17, font=("Helvetica", 12, "bold"), bg="black", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export Csv", command=self.exportCsv, width=17, font=("Helvetica", 12, "bold"), bg="black", fg="white")
        export_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.reset_data, width=17, font=("Helvetica", 12, "bold"), bg="black", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("Helvetica", 12, "bold"), bg="black", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",
                                 font=("Helvetica", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=540)

        # Scroll bar table
        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview configuration with period column
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "period", "attendance"),
                                                   xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side="bottom", fill=X)
        Scroll_y.pack(side="right", fill=Y)

        Scroll_x.config(command=self.AttendanceReportTable.xview)
        Scroll_y.config(command=self.AttendanceReportTable.yview)

        # Set headings
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("period", text="Period")  # Moved period column before attendance
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        # Set column widths
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("period", width=100)  # Moved period column before attendance
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def get_cursor(self, event):
        cursor_row = self.AttendanceReportTable.focus()
        contents = self.AttendanceReportTable.item(cursor_row)
        row = contents['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_period.set(row[6])  # Get period value
        self.var_atten_attendance.set(row[7])

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All File", "*.*")], parent=self.root)
        try:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)  # Call fetchData to update the Treeview
        except Exception as es:
            messagebox.showerror("Error", f"Error occurred: {str(es)}", parent=self.root)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data found to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=[("CSV File", "*.csv"), ("All File", "*.*")], parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                csvwriter = csv.writer(myfile)
                csvwriter.writerow(["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Period", "Attendance"])  # Updated header
                csvwriter.writerows(mydata)  # Write data
            messagebox.showinfo("Success", "Data exported successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error occurred: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        self.var_atten_period.set("")  # Reset period variable

    def go_back(self):
        # Logic to go back or exit to previous screen
        self.root.destroy()  # Example logic to close the application

if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()

# VEDIO NO. 4 --->  pip install opencv-python(OPEN CV install)
import cv2 # OPEN CV IS A OPEN SOURCE COMPUTER VISION LIBRARY  MAIN PURPOSE IS TO RECOGNIZE OBJECT OR FACES
            #OPENC CV MEIN HARCASCADE ALGORITHM HOTI HAI WHOSE MAJOR PURPOSE IS TO DETECT FACE
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Student:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1500x790+0+0")
            self.root.title("Face Recognition System")

      
            #===========variable======================
            self.var_dep=StringVar()
            self.var_course=StringVar()
            self.var_year=StringVar()
            self.var_semester=StringVar()
            self.var_std_id=StringVar()
            self.var_std_name=StringVar()
            self.var_div=StringVar()
            self.var_roll=StringVar()
            self.var_gender=StringVar()
            self.var_dob=StringVar()
            self.var_email=StringVar()
            self.var_phone=StringVar()
            self.var_address=StringVar()
            self.var_teacher=StringVar()
            self.var_radio1=StringVar()

            # IMAGE 1
            img = Image.open(r"D:\wallpapers\student1.jpg")
            img = img.resize((500,130), Image.BILINEAR)
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=130)

            # IMAGE 2   
            img1 = Image.open(r"D:\wallpapers\student2.jpg")
            img1 = img1.resize((500,130), Image.BILINEAR)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=500, y=0, width=520, height=130)

            # IMAGE 3
            img2 = Image.open(r"D:\wallpapers\student3.jpg")
            img2 = img2.resize((500,130), Image.BILINEAR)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=1000, y=0, width=520, height=130)

            #bg image
            bg_img = Image.open(r"D:\wallpapers\background.jpg")
            bg_img = bg_img.resize((1530, 710), Image.BILINEAR)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img)

            bg_label = Label(self.root, image=self.bg_photoimg)
            bg_label.place(x=0, y=130, width=1530, height=710)

            title_lbl = Label(root, text="STUDENT MANAGEMENT",font=("Helvetica", 32, "bold" , "underline"), bg="black", fg="white")
            title_lbl.place(x=0,y=130,width=1530,height=45)


            main_frame=Frame(root,bd=2,bg="white")
            main_frame.place(x=10,y=180,width=1480,height=600)

            #left frame
            LEFT_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
            LEFT_frame.place(x=10,y=10,width=730,height=580)

            img_left = Image.open(r"D:\wallpapers\attendance1.jpg")
            img_left = img_left.resize((720,130), Image.BILINEAR)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl2 = Label(LEFT_frame, image=self.photoimg_left)
            f_lbl2.place(x=5, y=0, width=720, height=130)

            #current cousre
            current_course_frame=LabelFrame(LEFT_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("Helvetica",12,"bold"))
            current_course_frame.place(x=5,y=135,width=720,height=150)

            # Department Label
            dep_label = Label(current_course_frame, text="Department", font=("Helvetica", 12, "bold"))
            dep_label.grid(row=0, column=0, padx=(10, 20), sticky=W)  

            # Department Combobox
            dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Helvetica", 12, "bold"), width=17, state="readonly")
            dep_combo["value"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
            dep_combo.current(0)
            dep_combo.grid(row=0, column=1, padx=(2, 10), pady=10, sticky=W)  

            # Course Label
            course_label = Label(current_course_frame, text="Course", font=("Helvetica", 12, "bold"))
            course_label.grid(row=0, column=2, padx=(10, 20), sticky=W)  
            # Course Combobox
            course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("Helvetica", 12, "bold"), width=17, state="readonly")
            course_combo["value"] = ("Select Course", "TE", "SE", "FE", "BE")
            course_combo.current(0)
            course_combo.grid(row=0, column=3, padx=(2, 10), pady=10, sticky=W)  


            # Year Label
            year_label = Label(current_course_frame, text="Year", font=("Helvetica", 12, "bold"))
            year_label.grid(row=1, column=0, padx=(10, 20), sticky=W)  

            # Year Combobox
            year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("Helvetica", 12, "bold"), width=17, state="readonly")
            year_combo["value"] = ("Select year", "2020-21", "2021-22", "2022-23", "2023-24")
            year_combo.current(0)
            year_combo.grid(row=1, column=1, padx=(2, 10), pady=10, sticky=W)  

            # Semester Label
            semester_label = Label(current_course_frame, text="Semester", font=("Helvetica", 12, "bold"))
            semester_label.grid(row=1, column=2, padx=(10, 20), sticky=W)

            # Semester Combobox
            semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("Helvetica", 12, "bold"), width=17, state="readonly")
            semester_combo["value"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semster 4")
            semester_combo.current(0)
            semester_combo.grid(row=1, column=3, padx=(2, 10), pady=10, sticky=W)  


            #Class Student information 
            class_student_frame = LabelFrame(LEFT_frame, bd=2, relief=RIDGE, text="Class Student information ", font=("Helvetica", 12, "bold"))
            class_student_frame.place(x=5, y=250, width=720, height=300)


            #Student Id
            studentID_label = Label(class_student_frame, text="Student ID:", font=("Helvetica", 12, "bold"))
            studentID_label.grid(row=0, column=0, padx=(10),pady=(5),sticky=W)

            studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Helvetica", 12, "bold"))
            studentID_entry.grid(row=0,column=1,padx=10,pady=(5),sticky=W)

            #Student name
            studentname_label = Label(class_student_frame, text="Student Name:", font=("Helvetica", 12, "bold"))
            studentname_label.grid(row=0, column=2, padx=(10),pady=(5), sticky=W)

            studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Helvetica", 12, "bold"))
            studentname_entry.grid(row=0,column=3,padx=10,pady=(5),sticky=W)

            #Class division
            class_div_label = Label(class_student_frame, text="Class Division:", font=("Helvetica", 12, "bold"))
            class_div_label.grid(row=1, column=0, padx=(10),pady=(5), sticky=W)

            div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("Helvetica", 12, "bold"), width=18, state="readonly")
            div_combo["value"] = ("A", "B", "C")
            div_combo.current(0)
            div_combo.grid(row=1, column=1, padx=(10), pady=5, sticky=W)  

            #Roll no
            roll_no_label = Label(class_student_frame, text="Roll NO:", font=("Helvetica", 12, "bold"))
            roll_no_label.grid(row=1, column=2, padx=(10),pady=(5), sticky=W)

            roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Helvetica", 12, "bold"))
            roll_no_entry.grid(row=1,column=3,padx=10,pady=(5),sticky=W)

            #Gender
            gender_label = Label(class_student_frame, text="Gender:", font=("Helvetica", 12, "bold"))
            gender_label.grid(row=2, column=0, padx=(10),pady=(5), sticky=W)

            gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("Helvetica", 12, "bold"), width=18, state="readonly")
            gender_combo["value"] = ("Male", "Female", "Others")
            gender_combo.current(0)
            gender_combo.grid(row=2, column=1, padx=(10), pady=5, sticky=W)  

            #DOB
            dob_label = Label(class_student_frame, text="DOB:", font=("Helvetica", 12, "bold"))
            dob_label.grid(row=2, column=2, padx=(10),pady=(5), sticky=W)

            dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Helvetica", 12, "bold"))
            dob_entry.grid(row=2,column=3,padx=10,pady=(5),sticky=W)

            #Email
            email_label = Label(class_student_frame, text="Email:", font=("Helvetica", 12, "bold"))
            email_label.grid(row=3, column=0, padx=(10),pady=(5), sticky=W)

            email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Helvetica", 12, "bold"))
            email_entry.grid(row=3,column=1,padx=10,pady=(5),sticky=W)

            #Phone no
            phone_no_label = Label(class_student_frame, text="Phone NO:", font=("Helvetica", 12, "bold"))
            phone_no_label.grid(row=3, column=2, padx=(10),pady=(5), sticky=W)

            phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Helvetica", 12, "bold"))
            phone_no_entry.grid(row=3,column=3,padx=10,pady=(5),sticky=W)

            #Address 
            address_label = Label(class_student_frame, text="Address:", font=("Helvetica", 12, "bold"))
            address_label.grid(row=4, column=0, padx=(10),pady=(5), sticky=W)

            address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Helvetica", 12, "bold"))
            address_entry.grid(row=4,column=1,padx=10,pady=(5),sticky=W)

            #Teachers name
            teacher_label = Label(class_student_frame, text="Teacher Name:", font=("Helvetica", 12, "bold"))
            teacher_label.grid(row=4, column=2, padx=(10),pady=(5), sticky=W)

            teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Helvetica", 12, "bold"))
            teacher_entry.grid(row=4,column=3,padx=10,pady=(5),sticky=W)

            # radio button
            Radiobtn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample",variable=self.var_radio1, value="Yes")
            Radiobtn1.grid(row=6, column=0)

            Radiobtn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample",variable=self.var_radio1, value="No")
            Radiobtn2.grid(row=6, column=1)

            # Button frame
            btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame.place(x=0,y=210,width=725,height=70)

            save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            save_btn.grid(row=0,column=0)

            update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            update_btn.grid(row=0,column=1)

            delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            delete_btn.grid(row=0,column=2)

            reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            reset_btn.grid(row=0,column=3)

            btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame1.place(x=0,y=245,width=717,height=35)

            take_photo_btn=Button(btn_frame1,command=self.generte_dataset,text="Take Photo Sample",width=35,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            take_photo_btn.grid(row=0,column=0)

            update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            update_photo_btn.grid(row=0,column=1)


            # right frame
            Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
            Right_frame.place(x=750,y=10,width=720,height=580)

            img_right = Image.open(r"D:\wallpapers\student1.jpg")
            img_right = img_right.resize((720, 130), Image.BILINEAR)
            self.photoimg_right = ImageTk.PhotoImage(img_right)

            f_lbl2 = Label(Right_frame, image=self.photoimg_right)
            f_lbl2.place(x=5, y=0, width=720, height=130)

            #Search system 
            Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=("Helvetica", 12, "bold"))
            Search_frame.place(x=5, y=135, width=710, height=70)

            search_label = Label(Search_frame, text="Search By:", font=("Helvetica", 12, "bold"),bg="black",fg="white")
            search_label.grid(row=0, column=0, padx=(10),pady=(5), sticky=W)

            search_combo = ttk.Combobox(Search_frame, font=("Helvetica", 12, "bold"), width=17)
            search_combo["value"] = ("Select", "Roll no","Phone no")
            search_combo.current(0)
            search_combo.grid(row=0, column=1, padx=(2, 10), pady=10, sticky=W)

            search_entry=ttk.Entry(Search_frame,width=15,font=("Helvetica", 12, "bold"))
            search_entry.grid(row=0,column=2,padx=10,pady=(5),sticky=W)

            search_btn=Button(Search_frame,text="Search",width=11,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            search_btn.grid(row=0,column=3,padx=4)

            ShowAll_btn=Button(Search_frame,text="ShowAll",width=11,font=("Helvetica", 12, "bold"),bg="black",fg="white")
            ShowAll_btn.grid(row=0,column=4)


            #==================Table frame=====================
            Table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
            Table_frame.place(x=5, y=210, width=710, height=350)

            scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

            self.student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)
            


            self.student_table.heading("dep", text="Department")
            self.student_table.heading("course", text="Course")
            self.student_table.heading("year", text="Year")
            self.student_table.heading("sem", text="Semester")
            self.student_table.heading("id", text="Student ID")
            self.student_table.heading("name", text="Name")
            self.student_table.heading("div", text="Division")
            self.student_table.heading("roll", text="Roll No")
            self.student_table.heading("gender", text="Gender")
            self.student_table.heading("dob", text="DOB")
            self.student_table.heading("email", text="Email")
            self.student_table.heading("phone", text="Phone")
            self.student_table.heading("address", text="Address")
            self.student_table.heading("teacher", text="Teacher")
            self.student_table.heading("photo", text="Photo Sample Status")
            self.student_table["show"]="headings"

            # Adjust column widths
            self.student_table.column("dep", width=100)
            self.student_table.column("course", width=100)
            self.student_table.column("year", width=100)
            self.student_table.column("sem", width=100)
            self.student_table.column("id", width=100)
            self.student_table.column("name", width=100)  
            self.student_table.column("div", width=100)
            self.student_table.column("roll", width=100)
            self.student_table.column("gender", width=100)
            self.student_table.column("dob", width=100)
            self.student_table.column("email", width=100)  
            self.student_table.column("phone", width=100)  
            self.student_table.column("address", width=100)  
            self.student_table.column("teacher", width=100)  
            self.student_table.column("photo", width=150)
            

            # Remove unnecessary padding
            self.student_table.pack(fill=BOTH, expand=1, padx=5, pady=5)
            self.student_table.bind("<ButtonRelease>", self.get_cursor)
            self.fetch_data()


      #=====================function button====================================

      def add_data(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                  messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                  try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
                        my_cursor = conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                          (self.var_dep.get(),
                                          self.var_course.get(),
                                          self.var_year.get(),
                                          self.var_semester.get(),
                                          self.var_std_id.get(),
                                          self.var_std_name.get(),
                                          self.var_div.get(),
                                          self.var_roll.get(),
                                          self.var_gender.get(),
                                          self.var_dob.get(),
                                          self.var_email.get(),
                                          self.var_phone.get(),
                                          self.var_address.get(),
                                          self.var_teacher.get(),
                                          self.var_radio1.get()
                                          ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
                  except Exception as es:
                        messagebox.showerror("Error", f"Error occurred: {str(es)}", parent=self.root)


      #======================Fetch data =============================
      def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for i in data:
                        self.student_table.insert("",END,values=i)
                  conn.commit()
            conn.close()

      #==========================Get cursor==========================

      #384 LINE::> INDEX OUT OF RANGE
      def get_cursor(self,event=" "):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]

            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])

      #=========================== Update function=============================
      def update_data(self):
                  if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                        messagebox.showerror("Error", "All fields are required", parent=self.root)
                  else:
                        try:
                              update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                              if update:
                                    conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
                                    my_cursor = conn.cursor()
                                    my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",

                                                                                                                                                                                                      (     self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get() 
                                                                                                                                                                                                            
                                                                                                                                                                                                            ))

                              else:
                                    if not update:
                                          return
                              messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                              self.fetch_data()
                              conn.commit()
                              conn.close()
                        except Exception as e:
                              messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

      #=========================== delete function=============================
      def delete_data(self):
            if self.var_std_id.get()=="":
                  messagebox.showerror("Error","Student id must be required" ,parent=self.root)
            else:
                  try:
                        delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                        if delete>0:
                              conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
                              my_cursor = conn.cursor()
                              sql="delete from student where Student_id=%s"
                              val=(self.var_std_id.get(),)
                              my_cursor.execute(sql,val)
                        else:
                              if not delete:
                                    return 
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete", "Successfully delete student details", parent=self.root)
                  except Exception as e:
                              messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)


      #=========================== reset function=============================
      def reset_data(self):
            self.var_dep.set("Select Department"),
            self.var_course.set("Select Course"),
            self.var_year.set("Select year"),
            self.var_semester.set("Select Semester"),
            self.var_std_id.set(""),
            self.var_std_name.set(""),
            self.var_div.set("A"),
            self.var_roll.set(""),
            self.var_gender.set("Male"),
            self.var_dob.set(""),
            self.var_email.set(""),
            self.var_phone.set(""),
            self.var_address.set(""),
            self.var_teacher.set(""),
            self.var_radio1.set("")


      #==========GENERATE DATA SET OR TAKE PHOTO SAMPLE=================
      def  generte_dataset(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                  messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                  try:
                        conn = mysql.connector.connect(host="localhost", username="root", password="0607",database="face_recognition")
                        my_cursor = conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                              id+=1
                        my_cursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",

                                                                                                      (self.var_dep.get(),
                                                                                                       self.var_course.get(),
                                                                                                       self.var_year.get(),
                                                                                                       self.var_semester.get(),
                                                                                                       self.var_std_name.get(),
                                                                                                       self.var_div.get(),
                                                                                                       self.var_roll.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_dob.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_teacher.get(),
                                                                                                       self.var_radio1.get(),
                                                                                                       self.var_std_id.get()==id+1
                                                                                               ))
                        conn.commit()
                        self.fetch_data()
                        # self.reset_data()
                        conn.close()

                        #  =========== LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV================
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                        def face_cropped(img):
                              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                              faces=face_classifier.detectMultiScale(gray,1.3,5)
                              #scalling factor=1.3
                              #Minimum Neighbour=5
                              for (x,y,w,h) in faces:
                                    face_cropped=img[y: y+h, x:x+w]
                                    return face_cropped
                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:

                              ret,my_frame=cap.read()
                              if face_cropped(my_frame) is not None:
                                    img_id+=1
                                    face=cv2.resize(face_cropped(my_frame),(450,450))
                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg" #.jpg nahi aa raha hai age
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                    cv2.imshow("Cropped Face",face)

                              if cv2.waitKey(1)==13 or int(img_id)==100:
                                    break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result", " 100 samples captured successfully!", parent=self.root)

                  
                  except Exception as e:
                              messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)
                  


                        




#==========>HAAR CASCADE ALGO GIVES EYE DETECTION AND FACE DETECTION


if __name__ == "__main__":
      root=Tk()
      obj=Student(root)
      root.mainloop()
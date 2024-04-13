from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Student:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1500x790+0+0")
            self.root.title("Face Recognition System")

      
            # IMAGE 1
            img = Image.open(r"F:\wallpapers\student1.jpg")
            img = img.resize((500,130), Image.BILINEAR)
            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=130)

            # IMAGE 2   
            img1 = Image.open(r"F:\wallpapers\student2.jpg")
            img1 = img1.resize((500,130), Image.BILINEAR)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lbl1 = Label(self.root, image=self.photoimg1)
            f_lbl1.place(x=500, y=0, width=520, height=130)

            # IMAGE 3
            img2 = Image.open(r"F:\wallpapers\student3.jpg")
            img2 = img2.resize((500,130), Image.BILINEAR)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lbl2 = Label(self.root, image=self.photoimg2)
            f_lbl2.place(x=1000, y=0, width=520, height=130)

            #bg image
            bg_img = Image.open(r"F:\wallpapers\background.jpg")
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

            img_left = Image.open(r"F:\wallpapers\attendance1.jpg")
            img_left = img_left.resize((720,130), Image.BILINEAR)
            self.photoimg_left = ImageTk.PhotoImage(img_left)

            f_lbl2 = Label(LEFT_frame, image=self.photoimg_left)
            f_lbl2.place(x=5, y=0, width=720, height=130)

            #current cousre
            current_course_frame=LabelFrame(LEFT_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("Helvetica",12,"bold"))
            current_course_frame.place(x=5,y=135,width=720,height=150)

            # Department Label
            dep_label = Label(current_course_frame, text="Department", font=("Helvetica", 12, "bold"), state="disabled")
            dep_label.grid(row=0, column=0, padx=(10, 20), sticky=W)  

            # Department Combobox
            dep_combo = ttk.Combobox(current_course_frame, font=("Helvetica", 12, "bold"), width=17)
            dep_combo["value"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
            dep_combo.current(0)
            dep_combo.grid(row=0, column=1, padx=(2, 10), pady=10, sticky=W)  

            # Course Label
            course_label = Label(current_course_frame, text="Course", font=("Helvetica", 12, "bold"), state="disabled")
            course_label.grid(row=0, column=2, padx=(10, 20), sticky=W)  
            # Course Combobox
            course_combo = ttk.Combobox(current_course_frame, font=("Helvetica", 12, "bold"), width=17)
            course_combo["value"] = ("Select Course", "TE", "SE", "FE", "BE")
            course_combo.current(0)
            course_combo.grid(row=0, column=3, padx=(2, 10), pady=10, sticky=W)  


            # Year Label
            course_label = Label(current_course_frame, text="Year", font=("Helvetica", 12, "bold"), state="disabled")
            course_label.grid(row=1, column=0, padx=(10, 20), sticky=W)  

            # Year Combobox
            course_combo = ttk.Combobox(current_course_frame, font=("Helvetica", 12, "bold"), width=17)
            course_combo["value"] = ("Select year", "2020-21", "2021-22", "2022-23", "2023-24")
            course_combo.current(0)
            course_combo.grid(row=1, column=1, padx=(2, 10), pady=10, sticky=W)  

            # Semester Label
            course_label = Label(current_course_frame, text="Semester", font=("Helvetica", 12, "bold"), state="disabled")
            course_label.grid(row=1, column=2, padx=(10, 20), sticky=W)

            # Semester Combobox
            course_combo = ttk.Combobox(current_course_frame, font=("Helvetica", 12, "bold"), width=17)
            course_combo["value"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semster 4")
            course_combo.current(0)
            course_combo.grid(row=1, column=3, padx=(2, 10), pady=10, sticky=W)  


            #Class Student information 
            class_student_frame=LabelFrame(LEFT_frame,bd=2,relief=RIDGE,text="Class Student information ",font=("Helvetica",12,"bold"))
            class_student_frame.place(x=5,y=250,width=720,height=300)





            # right frame
            right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Helvetica",12,"bold"))
            right_frame.place(x=750,y=10,width=720,height=580)


            

            




if __name__ == "__main__":
      root=Tk()
      obj=Student(root)
      root.mainloop()
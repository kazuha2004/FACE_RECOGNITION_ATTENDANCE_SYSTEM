from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime, timedelta
import cv2
import mysql.connector
import numpy as np
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 32, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        back_btn = Button(root, text="Back", command=self.go_back, font=("Helvetica", 12), bg='gray', fg='white')
        back_btn.place(x=1400, y=9, width=80, height=30)

        # Simplified image loading for testing
        try:
            img_top = Image.open(r"D:\wallpapers\facerecognizer1.jpg")
            img_top = img_top.resize((750, 900), Image.BILINEAR)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl1 = Label(self.root, image=self.photoimg_top)
            f_lbl1.place(x=0, y=50, width=750, height=750)

            img_bottom = Image.open(r"D:\wallpapers\facerecognizer2.jpg")
            img_bottom = img_bottom.resize((750, 900), Image.BILINEAR)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl2 = Label(self.root, image=self.photoimg_bottom)
            f_lbl2.place(x=750, y=50, width=750, height=750)

        except Exception as e:
            print(f"Error loading images: {str(e)}")

        b3_1 = Button(self.root, text="Start Face Recognition", command=self.start_recognition, cursor="hand2",
                      font=("Helvetica", 15, "bold"), bg="darkgreen", fg="white")
        b3_1.place(x=600, y=700, width=300, height=50)

    # ======================== ATTENDANCE MARKING FUNCTION ============================
    def mark_attendance(self, student_id, roll, name, dep):
        today_date = datetime.now().strftime("%d-%m-%Y")
        marked_today = False

        # Path for attendance data
        attendance_dir = 'attendance_data'
        if not os.path.exists(attendance_dir):
            os.makedirs(attendance_dir)

        # Creating the file path with today's date
        file_path = os.path.join(attendance_dir, f"{today_date}.csv")

        # Open file for attendance, create if it doesn't exist
        try:
            with open(file_path, "a+", newline="\n") as f:  # Use "a+" mode for appending
                f.seek(0)  # Move to the beginning of the file
                myDataList = f.readlines()
                name_list = []

                for line in myDataList:
                    entry = line.split(",")
                    if student_id == entry[0] and today_date == entry[5]:
                        marked_today = True
                        break

                if marked_today:
                    return False

                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")

                # Define lecture periods from timetable
                lecture_periods = {
                    1: {"start": now.replace(hour=9, minute=5), "end": now.replace(hour=9, minute=20)},
                    2: {"start": now.replace(hour=9, minute=55), "end": now.replace(hour=10, minute=10)},
                    3: {"start": now.replace(hour=10, minute=55), "end": now.replace(hour=11, minute=10)},
                    4: {"start": now.replace(hour=11, minute=45), "end": now.replace(hour=12, minute=0)},
                    5: {"start": now.replace(hour=13, minute=25), "end": now.replace(hour=13, minute=40)},
                    6: {"start": now.replace(hour=14, minute=15), "end": now.replace(hour=14, minute=30)},
                    7: {"start": now.replace(hour=15, minute=15), "end": now.replace(hour=15, minute=30)},
                    8: {"start": now.replace(hour=16, minute=5), "end": now.replace(hour=16, minute=20)},
                }

                attendance_status = "Absent"  # Default to Absent if the time doesn't match a period
                current_period = None

                # Check if the current time falls within any lecture period
                for period, times in lecture_periods.items():
                    if times["start"] <= now < times["end"]:
                        attendance_status = "Present"
                        current_period = period

                # Write attendance status to the CSV file
                if current_period:
                    f.write(f"{student_id},{roll},{name},{dep},{dtString},{today_date},Period {current_period},{attendance_status}\n")
                    return True
                else:
                    # Mark the student as Absent if outside any period
                    f.write(f"{student_id},{roll},{name},{dep},{dtString},{today_date},--,{attendance_status}\n")
                    return True

        except Exception as e:
            print(f"Error handling attendance file: {str(e)}")

    # ======================== FACE RECOGNITION FUNCTION ============================
    def start_recognition(self):
        print("Face Recognition Process Started")
        recognized_ids = set()
        students_in_class = set()  # Track all students who are in the class

        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            video_cap = cv2.VideoCapture(0)

            # Fetch all students from the database
            conn = mysql.connector.connect(host="localhost", username="root", password="Sahil30@", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student")
            all_students = cursor.fetchall()
            conn.close()

            # Store all student IDs in a set for later comparison
            for student in all_students:
                students_in_class.add(student[0])

            while True:
                ret, img = video_cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.1, 4)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    student_id, predict = clf.predict(gray[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    if confidence > 75 : # Recognized face
                        conn = mysql.connector.connect(host="localhost", username="root", password="Sahil30@", database="face_recognition")
                        cursor = conn.cursor()

                        cursor.execute(f"SELECT Name, Roll, Dep FROM student WHERE Student_id={student_id}")
                        result = cursor.fetchone()

                        if result:
                            name, roll, dep = result
                            cv2.putText(img, f"ID: {student_id}", (x, y - 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll: {roll}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name: {name}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Dept: {dep}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                            if student_id not in recognized_ids:
                                attendance_marked = self.mark_attendance(student_id, roll, name, dep)
                                if attendance_marked:
                                    recognized_ids.add(student_id)

                        conn.close()

                    else:  # Unknown face
                        cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

                cv2.imshow("Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                    break

            # After face recognition ends, mark absent students
            absent_students = students_in_class - recognized_ids
            for student_id in absent_students:
                conn = mysql.connector.connect(host="localhost", username="root", password="Sahil30@", database="face_recognition")
                cursor = conn.cursor()

                cursor.execute(f"SELECT Name, Roll, Dep FROM student WHERE Student_id={student_id}")
                result = cursor.fetchone()

                if result:
                    name, roll, dep = result
                    self.mark_attendance(student_id, roll, name, dep)  # Mark absent for the student

                conn.close()

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error during face recognition: {str(e)}")

    # ======================== BACK FUNCTION ============================
    def go_back(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

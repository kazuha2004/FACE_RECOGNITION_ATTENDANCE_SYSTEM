from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import cv2
import mysql.connector
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

    def mark_attendance(self, student_id, roll, name, dep):
        today_date = datetime.now().strftime("%d-%m-%Y")
        current_time = datetime.now()

        attendance_dir = 'attendance_data'
        if not os.path.exists(attendance_dir):
            os.makedirs(attendance_dir)

        file_path = os.path.join(attendance_dir, f"{today_date}.csv")

        try:
            with open(file_path, "a+", newline="\n") as f:
                f.seek(0)
                myDataList = f.readlines()

                lecture_periods = {
                    1: {"start": current_time.replace(hour=9, minute=5), "end": current_time.replace(hour=9, minute=55)},
                    2: {"start": current_time.replace(hour=9, minute=55), "end": current_time.replace(hour=10, minute=45)},
                    3: {"start": current_time.replace(hour=10, minute=55), "end": current_time.replace(hour=11, minute=45)},
                    4: {"start": current_time.replace(hour=11, minute=45), "end": current_time.replace(hour=12, minute=35)},
                    5: {"start": current_time.replace(hour=13, minute=25), "end": current_time.replace(hour=14, minute=15)},
                    6: {"start": current_time.replace(hour=14, minute=15), "end": current_time.replace(hour=15, minute=5)},
                    7: {"start": current_time.replace(hour=15, minute=15), "end": current_time.replace(hour=16, minute=5)},
                    8: {"start": current_time.replace(hour=16, minute=5), "end": current_time.replace(hour=16, minute=55)},
                }

                current_period = None
                for period, times in lecture_periods.items():
                    if times["start"] <= current_time < times["end"]:
                        current_period = period
                        break

                for line in myDataList:
                    entry = line.split(",")
                    if (student_id == entry[0] and today_date == entry[5] and
                            (current_period is None or f"Period {current_period}" == entry[6])):
                        return "Already Marked"

                dtString = current_time.strftime("%H:%M:%S")
                attendance_status = "Absent" if current_period is None else "Present"
                period_text = "--" if current_period is None else f"Period {current_period}"

                f.write(f"{student_id},{roll},{name},{dep},{dtString},{today_date},{period_text},{attendance_status}\n")
                return "Marked"

        except Exception as e:
            print(f"Error handling attendance file: {str(e)}")

    def start_recognition(self):
        print("Face Recognition Process Started")
        recognized_ids = set()
        students_in_class = set()

        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            video_cap = cv2.VideoCapture(0)

            conn = mysql.connector.connect(host="localhost", username="root", password="Sahil30@", database="face_recognition")
            cursor = conn.cursor()
            cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student")
            all_students = cursor.fetchall()
            conn.close()

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

                    if confidence > 75:
                        conn = mysql.connector.connect(host="localhost", username="root", password="Sahil30@", database="face_recognition")
                        cursor = conn.cursor()

                        cursor.execute(f"SELECT Name, Roll, Dep FROM student WHERE Student_id={student_id}")
                        result = cursor.fetchone()

                        if result:
                            name, roll, dep = result
                            if student_id not in recognized_ids:
                                attendance_status = self.mark_attendance(student_id, roll, name, dep)
                                if attendance_status == "Marked":
                                    recognized_ids.add(student_id)
                                    message = "Attendance Marked"
                                else:
                                    message = "Already Marked"
                            else:
                                message = "Already Marked"

                            cv2.putText(img, message, (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                            cv2.putText(img, f"ID: {student_id}", (x, y - 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Roll: {roll}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name: {name}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Dept: {dep}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                        conn.close()

                    else:
                        cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

                cv2.imshow("Face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error during face recognition: {str(e)}")

    def go_back(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

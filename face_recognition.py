from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
# pip install numpy
# pip install opencv-contrib-python --user
# pip install opencv-contrib-python

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 32, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image(LEFT SIDE)
        img_top = Image.open(r"D:\wallpapers\facerecognizer1.jpg")
        img_top = img_top.resize((750, 900), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=50, width=750, height=750)

        # 2nd image(RIGHT SIDE)
        img_bottom = Image.open(r"D:\wallpapers\facerecognizer2.jpg")
        img_bottom = img_bottom.resize((750, 900), Image.BILINEAR)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl1 = Label(self.root, image=self.photoimg_bottom)
        f_lbl1.place(x=750, y=50, width=750, height=750)

        # ==================BUTTON=======================
        b3_1 = Button(f_lbl1, text="Face Recognition", command=self.face_recog, cursor="hand2", font=("Helvetica", 15, "bold"), bg="darkgreen", fg="white")
        b3_1.place(x=280, y=660, width=200, height=40)

    # ====================== Face Recognition Method ======================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            #PUSH
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
                my_cursor = conn.cursor()

                # Fetch Name
                my_cursor.execute("SELECT Name FROM student WHERE Student_id="+str(id))
                n = my_cursor.fetchone()
                n =str(n)  # If None, use "Unknown"


                # Fetch Roll
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id="+str(id))
                r = my_cursor.fetchone()
                r =str(r)  # If None, use "Unknown"

                # Fetch Department
                my_cursor.execute("SELECT Dep FROM student WHERE Student_id="+ str(id))
                d = my_cursor.fetchone()
                d =str(d)  # If None, use "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, "Unknown face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]

            return coord


        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Helvetica", 32, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Simplified image loading for testing
        try:
            # 1st image (LEFT SIDE)
            img_top = Image.open(r"D:\wallpapers\facerecognizer1.jpg")
            img_top = img_top.resize((750, 900), Image.BILINEAR)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            f_lbl1 = Label(self.root, image=self.photoimg_top)
            f_lbl1.place(x=0, y=50, width=750, height=750)

            # 2nd image (RIGHT SIDE)
            img_bottom = Image.open(r"D:\wallpapers\facerecognizer2.jpg")
            img_bottom = img_bottom.resize((750, 900), Image.BILINEAR)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            f_lbl2 = Label(self.root, image=self.photoimg_bottom)
            f_lbl2.place(x=750, y=50, width=750, height=750)

        except Exception as e:
            print(f"Error loading images: {str(e)}")

        # ================ BUTTON ================
        b3_1 = Button(self.root, text="Start Face Recognition", command=self.start_recognition, cursor="hand2",
                      font=("Helvetica", 15, "bold"), bg="darkgreen", fg="white")
        b3_1.place(x=600, y=700, width=300, height=50)

    def start_recognition(self):
        print("Face Recognition Process Started")
        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()  # Ensure you have opencv-contrib-python installed
            clf.read("classifier.xml")
            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, 1.1, 4)
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    id, predict = clf.predict(gray[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    if confidence > 77:  # Recognized face with high confidence
                        # Fetch student details from the database
                        conn = mysql.connector.connect(host="localhost", username="root", password="0607", database="face_recognition")
                        cursor = conn.cursor()

                        cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=" + str(id))
                        result = cursor.fetchone()

                        if result:
                            name, roll, dep = result
                            cv2.putText(img, f"Roll: {roll}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Name: {name}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(img, f"Dept: {dep}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        else:
                            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
                        
                        conn.close()
                    else:  # Unknown face
                        cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

                cv2.imshow("Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error during recognition: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

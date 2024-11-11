from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
import pyttsx3
import threading

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty('rate', 150)

        # Set a black background for the entire window
        self.root.configure(bg="black")

        # Title label with black background and white text
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Helvetica", 32, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1500, height=50)

        back_btn = Button(root, text="Back", command=self.go_back, font=("Helvetica", 12), bg='gray', fg='white')
        back_btn.place(x=1400, y=13, width=80, height=30)  # Adjust x and y for positioning

        # Load and place top image
        img_top = Image.open(r"D:\wallpapers\train1.jpg")
        img_top = img_top.resize((1450, 300), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # Top image with dark border
        f_lbl_top = Label(self.root, image=self.photoimg_top, bd=2, relief=RIDGE, bg="black")
        f_lbl_top.place(x=25, y=60, width=1450, height=300)

        # Train button with modern black styling
        b3_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", 
                      font=("Helvetica", 28, "bold"), bg="gray20", fg="white", activebackground="gray30", 
                      activeforeground="white", bd=5, relief=GROOVE)
        b3_1.place(x=500, y=380, width=500, height=70)

        # Load and place bottom image
        img_bottom = Image.open(r"D:\wallpapers\train2.jpg")
        img_bottom = img_bottom.resize((1450, 300), Image.BILINEAR)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # Bottom image with dark border
        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom, bd=2, relief=RIDGE, bg="black")
        f_lbl_bottom.place(x=25, y=470, width=1450, height=300)

    # Function to train classifier
    def announce_in_thread(self, message):
            threading.Thread(target=self.announce, args=(message,)).start()

    def announce(self, message):
            self.speech_engine.say(message)
            self.speech_engine.runAndWait()

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier and save it
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        self.announce_in_thread("Training dataset completed")
        messagebox.showinfo("RESULT", "Training dataset completed")
    
    def go_back(self):
            try:
                  # Close the current window (student.py)
                  self.root.destroy()
            except Exception as e:
                  print(f"Error when trying to close the window: {e}")       



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

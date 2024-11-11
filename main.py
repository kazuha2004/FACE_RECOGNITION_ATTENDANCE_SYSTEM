import pyttsx3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from chatbot2 import ChatBot
from Developer import Developer
from login import LoginSystem  # Import your Login class from login.py


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # Initialize text-to-speech engine
        self.speech_engine = pyttsx3.init()
        self.speech_engine.setProperty('rate', 150)  # Set the speech rate to slow down the audio

        self.chatbot_window = None  # To keep track of the ChatBot window
        self.chatbot_open = False  # Flag to check if ChatBot is open

        # IMAGE 1
        img = Image.open(r"D:\wallpapers\glasses.jpg")
        img = img.resize((500, 130), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # IMAGE 2
        img1 = Image.open(r"D:\wallpapers\ai.jpg")
        img1 = img1.resize((500, 130), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # IMAGE 3
        img2 = Image.open(r"D:\wallpapers\screen.jpg")
        img2 = img2.resize((500, 130), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)

        # Background image
        bg_img = Image.open(r"D:\wallpapers\background.jpg")
        bg_img = bg_img.resize((1530, 710), Image.BILINEAR)
        self.bg_photoimg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.bg_photoimg)
        bg_label.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("Helvetica", 32, "bold", "underline"), bg="black", fg="white")
        title_lbl.place(x=0, y=130, width=1530, height=45)

        # Student button
        button_img = Image.open(r"D:\wallpapers\work.jpg")
        button_img = button_img.resize((220, 220), Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(button_img)

        b3 = Button(self.root, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b3.place(x=200, y=200, width=220, height=220)

        b3_1 = Button(self.root, text="Student Details", command=self.student_details, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=200, y=400, width=220, height=40)

        # Detect face button
        button_img1 = Image.open(r"D:\wallpapers\detect.jpg")
        button_img1 = button_img1.resize((220, 220), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(button_img1)

        b3 = Button(self.root, image=self.photoimg5, cursor="hand2", command=self.face_recognition_data)
        b3.place(x=500, y=200, width=220, height=220)

        b3_1 = Button(self.root, text="Face Recognition", command=self.face_recognition_data, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=500, y=400, width=220, height=40)

        # Attendance button
        button_img2 = Image.open(r"D:\wallpapers\attendance.jpg")
        button_img2 = button_img2.resize((220, 220), Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(button_img2)

        b3 = Button(self.root, image=self.photoimg6, cursor="hand2", bg="black", command=self.Attendance_data)
        b3.place(x=800, y=200, width=220, height=220)

        b3_1 = Button(self.root, text="Attendance", command=self.Attendance_data, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=800, y=400, width=220, height=40)

        # Help Desk button (Chat Bot)
        button_img3 = Image.open(r"D:\wallpapers\chatbot.jpg")
        button_img3 = button_img3.resize((220, 220), Image.BILINEAR)
        self.photoimg7 = ImageTk.PhotoImage(button_img3)

        b3 = Button(self.root, image=self.photoimg7, cursor="hand2", bg="black", command=self.toggle_chat_bot)
        b3.place(x=1100, y=200, width=220, height=220)

        b3_1 = Button(self.root, text="Chat Bot", cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white", command=self.toggle_chat_bot)
        b3_1.place(x=1100, y=400, width=220, height=40)

        # Train face button
        button_img4 = Image.open(r"D:\wallpapers\train.jpg")
        button_img4 = button_img4.resize((220, 220), Image.BILINEAR)
        self.photoimg8 = ImageTk.PhotoImage(button_img4)

        b3 = Button(self.root, image=self.photoimg8, cursor="hand2", bg="black", command=self.train_data)
        b3.place(x=200, y=480, width=220, height=220)

        b3_1 = Button(self.root, text="Train Data", cursor="hand2", command=self.train_data, font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=200, y=680, width=220, height=40)

        # Photos button
        button_img5 = Image.open(r"D:\wallpapers\Photos.jpg")
        button_img5 = button_img5.resize((220, 220), Image.BILINEAR)
        self.photoimg9 = ImageTk.PhotoImage(button_img5)

        b3 = Button(self.root, image=self.photoimg9, cursor="hand2", bg="black", command=self.open_img)
        b3.place(x=500, y=480, width=220, height=220)

        b3_1 = Button(self.root, command=self.open_img, text="Photos", cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=500, y=680, width=220, height=40)

        # Developer button
        button_img6 = Image.open(r"D:\wallpapers\report and analytics.jpg")
        button_img6 = button_img6.resize((220, 220), Image.BILINEAR)
        self.photoimg10 = ImageTk.PhotoImage(button_img6)

        b3 = Button(self.root, image=self.photoimg10, cursor="hand2", bg="black", command=self.open_developer_window)
        b3.place(x=800, y=480, width=220, height=220)

        b3_1 = Button(self.root, text="Report and Analytics", command=self.open_developer_window, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=800, y=680, width=220, height=40)

        # Exit button
        button_img7 = Image.open(r"D:\wallpapers\exit.jpg")
        button_img7 = button_img7.resize((220, 220), Image.BILINEAR)
        self.photoimg11 = ImageTk.PhotoImage(button_img7)

        b3 = Button(self.root, image=self.photoimg11, cursor="hand2", bg="black", command=self.exit_program)
        b3.place(x=1100, y=480, width=220, height=220)

        b3_1 = Button(self.root, text="Exit", command=self.exit_program, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black", fg="white")
        b3_1.place(x=1100, y=680, width=220, height=40)

    def announce_opening(self, module_name):
        self.speech_engine.say(f"{module_name} is opening now.")
        self.speech_engine.runAndWait()

    def student_details(self):
        self.announce_opening("Student Details Module")
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def toggle_chat_bot(self):
        if not self.chatbot_open:
            self.chatbot_window = Toplevel(self.root)
            self.app = ChatBot(self.chatbot_window)
            self.chatbot_open = True
            self.announce_opening("Chat Bot")

            # Close chatbot window when window is destroyed
            self.chatbot_window.protocol("WM_DELETE_WINDOW", self.close_chat_bot)
        else:
            self.close_chat_bot()  # Close the chatbot if it's already open

    def close_chat_bot(self):
        if self.chatbot_open:
            self.chatbot_open = False
            self.chatbot_window.destroy()

    def open_developer_window(self):
        self.announce_opening("Developer Report and Analytics")
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def open_img(self):
        self.announce_opening("Photos")
        os.startfile("data")

    def train_data(self):
        self.announce_opening("Training Data")
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognition_data(self):
        self.announce_opening("Face Recognition")
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def Attendance_data(self):
        self.announce_opening("Attendance")
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def exit_program(self):
        choice = messagebox.askyesno("Exit", "Do you really want to exit?")
        if choice > 0:
            self.speech_engine.say("Exiting the program now. Goodbye!")
            self.speech_engine.runAndWait()
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
7
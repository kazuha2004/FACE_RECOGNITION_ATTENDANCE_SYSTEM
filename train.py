import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Train:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1500x790+0+0")
            self.root.title("Face Recognition System")

            title_lbl = Label(self.root, text=" TRAIN DATA SET", font=("Helvetica", 32, "bold"), bg="black",
                              fg="white")
            title_lbl.place(x=0, y=0, width=1530, height=45)

            img_top = Image.open(r"D:\wallpapers\attendance1.jpg")
            img_top = img_top.resize((1530, 325), Image.BILINEAR)
            self.photoimg_top = ImageTk.PhotoImage(img_top)



            f_lbl2 = Label(self.root, image=self.photoimg_top)
            f_lbl2.place(x=0, y=45, width=1530, height=325)

            #==================BUTTON=======================

            b3_1 = Button(self.root, text="Train data", cursor="hand2", font=("Helvetica", 15, "bold"), bg="black",fg="white")
            b3_1.place(x=0, y=380, width=1530, height=60)



            img_bottom = Image.open(r"D:\wallpapers\student3.jpg")
            img_bottom = img_top.resize((1530, 325), Image.BILINEAR)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl2 = Label(self.root, image=self.photoimg_bottom)
            f_lbl2.place(x=0, y=440, width=1530, height=325)




if __name__ == "__main__":
      root=Tk()
      obj=Train(root)
      root.mainloop()
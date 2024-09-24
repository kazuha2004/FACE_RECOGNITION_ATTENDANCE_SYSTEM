
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2

class Train:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1500x790+0+0")
            self.root.title("Face Recognition System")

            title_lbl = Label(self.root, text=" TRAIN DATA SET", font=("Helvetica", 32, "bold"), bg="black",fg="white")
            title_lbl.place(x=0, y=0, width=1530, height=45)

            img_top = Image.open(r"D:\wallpapers\attendance1.jpg")
            img_top = img_top.resize((1530, 325), Image.BILINEAR)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl2 = Label(self.root, image=self.photoimg_top)
            f_lbl2.place(x=0, y=45, width=1530, height=325)

            #==================BUTTON=======================

            b3_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier,cursor="hand2", font=("Helvetica", 30, "bold"), bg="black",fg="white")
            b3_1.place(x=0, y=380, width=1530, height=60)#BUTTON UPER SIDE SHIFT KARNA PADEGA THODA YA PHIR UPAR VALI IMAGE KO NICHE KARNA PADEGA THODA SO PLEASE REMEMBER TO MAKE THE CHANGES IN FUTURE..........




            img_bottom = Image.open(r"D:\wallpapers\student3.jpg")
            img_bottom = img_top.resize((1530, 325), Image.BILINEAR)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl2 = Label(self.root, image=self.photoimg_bottom)
            f_lbl2.place(x=0, y=440, width=1530, height=325)

          #======================LBPH IS PRESENT HERE===================
      def train_classifier(self):
            data_dir="data"
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            faces=[]
            ids=[]
            for image in path:
                  img=Image.open(image).convert('L')# CONVERTING TO GRAY SCALE IMAGE
                  imageNp=np.array(img,'uint8')
                  id = int(os.path.split(image)[1].split('.')[1])
                  faces.append(imageNp)
                  ids.append(id)
                  cv2.imshow("TRAINING",imageNp)
                  cv2.waitKey(1)==13
            ids=np.array(ids)


          #======================TRAIN THE CLASSIFIER AND SAVE=============================
            clf=cv2.face.LBPHFaceRecognizer_create()#pip install opencv-contrib-python   WARNA ERROR DEGA
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("RESULT","TRAINING DATASET COMPLETED")




if __name__ == "__main__":
      root=Tk()
      obj=Train(root)
      root.mainloop()
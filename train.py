from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
#pip install numpy
#pip install opencv-contrib-python --user
#pip install opencv-contrib-python

class Train:
      def __init__(self,root):
            self.root=root
            self.root.geometry("1500x790+0+0")
            self.root.title("Face Recognition System")

            title_lbl = Label(self.root, text=" TRAIN DATA SET", font=("Helvetica", 32, "bold"), bg="black",fg="white")
            title_lbl.place(x=0, y=0, width=1530, height=45)

            # Load and resize the top image
            img_top = Image.open(r"D:\wallpapers\train2.jpg")
            img_top = img_top.resize((1530, 325), Image.BILINEAR)
            self.photoimg_top = ImageTk.PhotoImage(img_top)

            f_lbl1 = Label(self.root, image=self.photoimg_top)
            f_lbl1.place(x=0, y=45, width=1530, height=325)

            #==================BUTTON=======================
            b3_1 = Button(self.root, text="Train data",command=self.train_classifier, cursor="hand2", font=("Helvetica", 15, "bold"), bg="black",fg="white")
            b3_1.place(x=0, y=380, width=1530, height=60)

            # Load and resize the bottom image
            img_bottom = Image.open(r"D:\wallpapers\train1.jpg")
            img_bottom = img_bottom.resize((1530, 325), Image.BILINEAR)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

            f_lbl3 = Label(self.root, image=self.photoimg_bottom)
            f_lbl3.place(x=0, y=450, width=1530, height=325)

      def train_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            

            faces=[] #image od the same person have the same id 
            ids=[]


            for image in path:
                  img = Image.open(image).convert('L')  # gray scale image
                  imageNp = np.array(img, 'uint8')
                  # id = int(os.path.split(image)[1].split('.')[1])
                  id = int(os.path.split(image)[1].split('.')[1])  


                  faces.append(imageNp)
                  ids.append(id)
                  cv2.imshow("Training", imageNp)
                  cv2.waitKey(1) == 13
  
            ids = np.array(ids)


#================================= Train the classifier and save =================================

            
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write('classifier.xml')
            cv2.destroyAllWindows()
            messagebox.showinfo('Result',"Training data sets completed!!",parent=self.root)

            

if __name__ == "__main__":
      root=Tk()
      obj=Train(root)
      root.mainloop()

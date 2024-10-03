from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        # Main frame
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)  # Adjusted width
        main_frame.pack()

        # Image loading
        img_chat = Image.open('chat.jpg')
        img_chat = img_chat.resize((200, 70), Image.BILINEAR)  # Updated from Image.ANTIALIAS
        self.photoimg = ImageTk.PhotoImage(img_chat)

        # Title label
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, image=self.photoimg,
                            text='CHAT ME', font=('arial', 30, 'bold'), fg='green', bg='white', compound='left')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=20, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry=StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry, width=40, font=('times new roman', 16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send_btn = Button(btn_frame, text="Send>>", font=('arial', 15, 'bold'), width=8, bg='green',
                               command=self.send)  # Link to send method
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frame,text="Clear Chat", font=('arial', 15, 'bold'), width=8, bg='red', fg='white',
                                command=self.clear_chat)  # Optional clear chat feature
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    # ======== Function to send a message ===============
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')    
    
    def send(self):
        user_input = self.entry.get()  # Store input in a variable
        self.text.yview(END)
        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

            send_message = '\t\t\tYou: ' + user_input
            self.text.insert(END, '\n' + send_message)

            # Bot responses
            if user_input.lower() == 'hello':
                self.text.insert(END, '\n\n' + "Bot: Hi")
            elif user_input.lower() == 'hi':
                self.text.insert(END, '\n\n' + "Bot: Hello")
            elif user_input.lower() == 'how are you':
                self.text.insert(END, '\n\n' + "Bot: I'm fine, and you?")
            elif user_input.lower() == 'who created you':
                self.text.insert(END, '\n\n' + "Bot: Mr. Sandeep Vishwakarma") 
            else:
                self.text.insert(END, "\n\n" + "Bot: Sorry, I didn't get it")

            # Clear the entry after sending the message
            self.entry.delete(0, END)

    # Optional: Function to clear the chatbox
    def clear_chat(self):
        self.text.delete(1.0, END)


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)  # Binding the Enter key to the send function

        # Main frame
        main_frame = Frame(self.root, bd=4, bg='#2c2f33', width=610)
        main_frame.pack()

        # Image loading
        img_chat = Image.open('chat.jpg')  # Ensure this image is accessible
        img_chat = img_chat.resize((200, 70), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        # Title label
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730,
                            image=self.photoimg, text='CHAT ME', font=('arial', 30, 'bold'),
                            fg='white', bg='#23272a', compound='left')
        Title_label.pack(side=TOP)

        # Scrollable Text Box
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=20, relief=RAISED, 
                         font=('arial', 14), bg='#2c2f33', fg='white', 
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.config(command=self.text.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # Button Frame
        btn_frame = Frame(self.root, bd=4, bg='#2c2f33', width=730)
        btn_frame.pack()

        # Entry Box Label
        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='white', bg='#2c2f33')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        # User Input Field
        self.entry = StringVar()
        self.entry_field = ttk.Entry(btn_frame, textvariable=self.entry, width=40, 
                                     font=('times new roman', 16, 'bold'), foreground='black', background='#23272a')
        self.entry_field.grid(row=0, column=1, padx=5, sticky=W)

        # Send Button
        self.send_btn = Button(btn_frame, text="Send>>", font=('arial', 15, 'bold'), width=8, bg='#7289da', fg='white',
                               command=self.send)
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        # Clear Chat Button
        self.clear_btn = Button(btn_frame, text="Clear Chat", font=('arial', 15, 'bold'), width=8, bg='#99aab5',
                                fg='black', command=self.clear_chat)
        self.clear_btn.grid(row=1, column=0, padx=5, sticky=W)

        # Error/Info Label
        self.msg = ''
        self.label_11 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='#2c2f33')
        self.label_11.grid(row=1, column=1, padx=5, sticky=W)

    # Function to handle 'Enter' key press
    def enter_func(self, event):
        self.send()  # Call the send function when Enter is pressed

    # Function to send a message
    def send(self):
        user_input = self.entry.get().strip()  # Trim whitespace
        if user_input == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')
            self.display_message("You", user_input, side='right')  # Display user's message on the right
            self.generate_bot_response(user_input.lower())  # Generate bot response

            # Clear the entry after sending the message
            self.entry_field.delete(0, END)
            self.entry_field.focus()  # Auto-focus on entry field

    # Function to clear the chatbox
    def clear_chat(self):
        self.text.delete(1.0, END)
        self.entry.set('')
        self.label_11.config(text='')

    # Function to display messages with a slight indentation on the right for user messages
    def display_message(self, sender, message, side='left'):
        # Right-aligned message (for user) with padding from the right
        if side == 'right':
            self.text.tag_configure('right', justify='right', spacing1=5, wrap='word', lmargin1=50)  # Add left margin for right-aligned text
            self.text.insert(END, f"{sender}: {message}\n", 'right')
        # Left-aligned message (for bot)
        else:
            self.text.tag_configure('left', justify='left', spacing1=5, wrap='word')
            self.text.insert(END, f"{sender}: {message}\n", 'left')

        # Auto-scroll to the end of the conversation
        self.text.yview(END)

    # Function to generate bot responses based on user input
    def generate_bot_response(self, user_input):
        responses = {
          'hello': "Hi! How can I assist you with the attendance system today?",
          'hi': "Hello! Need help with the attendance system?",
          'how are you': "I'm here and ready to help with your attendance queries!",
          'who created you': "I was developed as part of a project to enhance attendance management using face recognition technology.",
          'bye': "Goodbye! Have a great day!",
          'thanks': "You're welcome! Let me know if you need more help.",
    
          # Attendance System Specific Questions
          'how does this attendance system work': "The system captures your face image, identifies you using face recognition technology, and marks your attendance automatically.",
          'what is face recognition attendance system': "It’s an automated system that uses face recognition to identify users and record their attendance, ensuring an efficient and secure process.",
          'can this system mark my attendance automatically': "Yes! Once the system recognizes your face, it marks your attendance automatically and records the time.",
          'is my data safe with this attendance system': "Yes, your data is stored securely and is only used for attendance purposes. We ensure compliance with privacy guidelines.",
          'how accurate is the face recognition': "The system is designed to be highly accurate, but factors like lighting and camera quality can affect the results.",
          'how is attendance recorded': "Once your face is recognized, your attendance is marked along with the date and time in the system's database.",
          'can this system detect multiple people at once': "Yes, it can handle multiple faces, allowing the system to mark attendance for several people at once if they are recognized.",
          'what if my face is not recognized': "If your face isn’t recognized, ensure you are facing the camera properly. You may also need to register or re-register in the system.",
          'can i view my attendance history': "Yes, you can request your attendance history if this feature is enabled by your organization.",
          'how can i register my face': "To register, look at the camera while the system records your facial features for future recognition.",
          'what happens if someone else tries to check in for me': "The system is designed to identify unique facial features, so only you can check in with your own face.",
          'can this be used for remote attendance': "If the system is set up for remote recognition, you can mark your attendance from other locations.",
          'what if i am wearing glasses or a mask': "Glasses usually won’t be an issue, but masks can affect recognition accuracy. It's best to ensure your face is fully visible for reliable attendance marking.",
          'what are the benefits of face recognition attendance': "It offers a fast, hands-free way to mark attendance, reduces the chance of proxy attendance, and keeps attendance data secure.",
    
          # General Questions
          'what technology is used in this system': "This system uses Python, OpenCV for face recognition, and a secure database to store attendance records.",
          'how can you help me': "I can answer questions about the attendance system, help with troubleshooting, and explain features.",
          'tell me a joke': "Sure! Why did the computer take a nap? It had a hard drive!",
          'who can access my attendance data': "Only authorized personnel can access attendance records, ensuring your privacy and data security.",

              # Detailed Attendance System Questions
          'how is attendance recorded in this system': "Once the system recognizes your face, it marks your attendance along with the date and time, saving it securely in the attendance database.",
          'how accurate is the face recognition system': "The system is highly accurate under good lighting and with clear images, but factors like image quality, facial obstructions, or low light can impact accuracy.",
          'what technology does this system use': "This system uses Python with OpenCV for face detection, and a database for securely storing attendance records.",
          'is my attendance recorded in real-time': "Yes, once your face is recognized, your attendance is marked instantly in real-time and saved with a timestamp.",
          'can this system mark attendance for multiple people at once': "Yes, it can recognize and record attendance for multiple faces simultaneously, allowing for efficient group check-ins.",
    
          # Data Privacy and Security
          'is my data safe with this attendance system': "Yes, your data is stored securely and is used solely for attendance tracking. The system complies with privacy and data security protocols.",
          'who can access my attendance data': "Only authorized personnel can access attendance records to ensure your privacy and data security.",
          'how is my data stored': "Your attendance data is stored in a secure, encrypted database, and facial data is used only temporarily for real-time recognition.",
    
    # Registration and User Queries
          'how do i register my face': "To register, simply look at the camera as the system captures your facial features and stores them securely for future recognition.",
          'can i view my attendance history': "Yes, if enabled, you can request your attendance history through authorized access or a specific portal provided by your organization.",
          'what if my face is not recognized': "Ensure that you are facing the camera directly, with good lighting. If issues persist, re-registration may be required.",
          'can this system work if i have a new hairstyle or wear glasses': "The system is designed to recognize you despite minor changes, but drastic changes might require re-registration.",
          'does this system work if i am wearing a mask': "Face recognition accuracy may be affected by masks, as it needs to capture your facial features clearly.",
          'can someone else mark attendance for me': "No, the system identifies unique facial features to prevent proxy attendance and ensure secure, accurate records.",
          'what happens if i miss a check-in': "If you miss a check-in, you may be able to manually request attendance adjustments, depending on your organization's policy.",
    
            # Troubleshooting and FAQs
          'what do i do if my attendance was not recorded': "Check to ensure your face is fully visible to the camera. You may also contact the administrator for troubleshooting if issues persist.",
          'what if there is an error during face recognition': "Errors may happen due to lighting or network issues. Try again, or contact support if the problem continues.",
          'what are the benefits of face recognition attendance': "It’s fast, hands-free, reduces errors, and prevents proxy attendance, all while keeping your data secure.",
          'is this system secure from hackers': "The system is designed with data security in mind, using encryption and access control to protect against unauthorized access."


}


        # Fallback response for unrecognized input
        bot_response = responses.get(user_input, self.default_response(user_input))
        self.display_message("Bot", bot_response, side='left')  # Display bot's message on the left

    # Function to generate a default response for unrecognized input
    def default_response(self, user_input):
        if 'help' in user_input:
            return "How can I assist you? You can ask me about my features."
        return "Sorry, I didn't understand that."


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()

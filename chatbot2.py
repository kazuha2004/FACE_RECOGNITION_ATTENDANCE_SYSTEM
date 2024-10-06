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
                                     font=('times new roman', 16, 'bold'), foreground='white', background='#23272a')
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
            'hello': "Hi! How can I assist you today?",
            'hi': "Hello! What would you like to talk about?",
            'how are you': "I'm just a bot, but I'm doing great! How about you?",
            'who created you': "I was created by Mr. Sandeep Vishwakarma.",
            'bye': "Goodbye! Have a great day!",
            'thanks': "You're welcome! Let me know if you need anything else."
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

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
from PIL import Image, ImageTk

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1500x790+0+0")

        # Load and set the background image
        self.background_image = Image.open(r"D:\wallpapers\background.jpg")  # Change to your image path
        self.background_image = self.background_image.resize((1500, 790), Image.BILINEAR)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.bg_label = Label(self.root, image=self.background_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Variables
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.otp_var = StringVar()
        self.otp = None

        # Frame for better organization with rounded corners
        main_frame = Frame(self.root, bg='#2c2f33', bd=10, relief=RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Labels and Entries
        title_lbl = Label(main_frame, text="Login System", font=("Helvetica", 36, "bold"), bg='#2c2f33', fg='#7289da')
        title_lbl.grid(row=0, column=0, columnspan=2, pady=20)

        username_lbl = Label(main_frame, text="Username", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        username_lbl.grid(row=1, column=0, pady=10, padx=20, sticky=E)
        self.username_entry = Entry(main_frame, textvariable=self.username_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.username_entry.grid(row=1, column=1, pady=10, padx=20)

        email_lbl = Label(main_frame, text="Email", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        email_lbl.grid(row=2, column=0, pady=10, padx=20, sticky=E)
        self.email_entry = Entry(main_frame, textvariable=self.email_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.email_entry.grid(row=2, column=1, pady=10, padx=20)

        password_lbl = Label(main_frame, text="Password", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        password_lbl.grid(row=3, column=0, pady=10, padx=20, sticky=E)
        self.password_entry = Entry(main_frame, textvariable=self.password_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', show="*", width=30)
        self.password_entry.grid(row=3, column=1, pady=10, padx=20)

        # Buttons with better alignment and spacing
        btn_frame = Frame(main_frame, bg='#2c2f33')
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)

        login_btn = Button(btn_frame, text="Login", command=self.login, font=("Helvetica", 16), bg='#7289da', fg='white', width=15)
        login_btn.grid(row=0, column=0, padx=10)

        register_btn = Button(btn_frame, text="Register", command=self.register_window, font=("Helvetica", 16), bg='#99aab5', fg='black', width=15)
        register_btn.grid(row=0, column=1, padx=10)

        forgot_btn = Button(main_frame, text="Forgot Password", command=self.forgot_password_window, font=("Helvetica", 16), bg='#99aab5', fg='black', width=32)
        forgot_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Connect to MySQL Database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0607",  # Change to your MySQL password
                database="register"
            )
            cursor = connection.cursor()

            # Query to check the username and password using case-insensitive comparison
            query = "SELECT * FROM users WHERE LOWER(username)=%s AND password=%s"
            cursor.execute(query, (username.lower(), password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", f"Welcome, {result[1]}!")
                self.root.destroy()  # Close the login window after successful login
                subprocess.Popen(['python', 'main.py'])
            else:
                messagebox.showerror("Error", "Invalid Username or Password!")
            connection.close()

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def forgot_password_window(self):
        self.new_window = Toplevel(self.root)
        self.app = ForgotPassword(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register New User")
        self.root.geometry("1500x790+0+0")

        # Load and set the background image
        self.background_image = Image.open(r"D:\wallpapers\background.jpg")  # Change to your image path
        self.background_image = self.background_image.resize((1500, 790), Image.BILINEAR)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.bg_label = Label(self.root, image=self.background_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Variables
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()

        # Frame for better organization, increased size
        main_frame = Frame(self.root, bg='#2c2f33', bd=10, relief=RIDGE, width=850, height=500)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Labels and Entries
        title_lbl = Label(main_frame, text="Register New User", font=("Helvetica", 36, "bold"), bg='#2c2f33', fg='#7289da')
        title_lbl.grid(row=0, column=0, columnspan=2, pady=20)

        username_lbl = Label(main_frame, text="Username", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        username_lbl.grid(row=1, column=0, pady=10, padx=20, sticky=E)
        self.username_entry = Entry(main_frame, textvariable=self.username_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.username_entry.grid(row=1, column=1, pady=10, padx=20)

        email_lbl = Label(main_frame, text="Email", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        email_lbl.grid(row=2, column=0, pady=10, padx=20, sticky=E)
        self.email_entry = Entry(main_frame, textvariable=self.email_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.email_entry.grid(row=2, column=1, pady=10, padx=20)

        password_lbl = Label(main_frame, text="Password", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        password_lbl.grid(row=3, column=0, pady=10, padx=20, sticky=E)
        self.password_entry = Entry(main_frame, textvariable=self.password_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', show="*", width=30)
        self.password_entry.grid(row=3, column=1, pady=10, padx=20)

        # Buttons
        button_frame = Frame(main_frame, bg='#23272a')
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # Buttons
        register_btn = Button(button_frame, text="Register", command=self.register, font=("Helvetica", 16), bg='#7289da', fg='white', width=15)
        register_btn.grid(row=0, column=0, padx=10)

        back_btn = Button(button_frame, text="Back", command=self.root.destroy, font=("Helvetica", 16), bg='#99aab5', fg='black', width=15)
        back_btn.grid(row=0, column=1, padx=10)



    def register(self):
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get()

        if username == "" or email == "" or password == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Connect to MySQL database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0607",  # Change to your MySQL password
                database="register"
            )
            cursor = connection.cursor()

            # Check if username or email already exists
            cursor.execute("SELECT * FROM users WHERE username=%s OR email=%s", (username, email))
            existing_user = cursor.fetchone()

            if existing_user:
                messagebox.showerror("Error", "Username or Email already exists!")
            else:
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                connection.commit()
                messagebox.showinfo("Success", "Registration Successful!")
                self.root.destroy()
            connection.close()


class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("1500x790+0+0")

        # Load and set the background image
        self.background_image = Image.open(r"D:\wallpapers\background.jpg")  # Change to your image path
        self.background_image = self.background_image.resize((1500, 790), Image.BILINEAR)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.bg_label = Label(self.root, image=self.background_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Variables
        self.email_var = StringVar()
        self.otp_var = StringVar()
        self.password_var = StringVar()
        self.confirm_password_var = StringVar()
        self.otp = None

        # Frame for better organization
        main_frame = Frame(self.root, bg='#2c2f33', bd=10, relief=RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Labels and Entries
        title_lbl = Label(main_frame, text="Reset Password", font=("Helvetica", 36, "bold"), bg='#2c2f33', fg='#7289da')
        title_lbl.grid(row=0, column=0, columnspan=2, pady=30)

        email_lbl = Label(main_frame, text="Email", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        email_lbl.grid(row=1, column=0, pady=15)
        self.email_entry = Entry(main_frame, textvariable=self.email_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.email_entry.grid(row=1, column=1, pady=15, padx=20)

        otp_lbl = Label(main_frame, text="OTP", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        otp_lbl.grid(row=2, column=0, pady=15)
        self.otp_entry = Entry(main_frame, textvariable=self.otp_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', width=30)
        self.otp_entry.grid(row=2, column=1, pady=15, padx=20)

        password_lbl = Label(main_frame, text="New Password", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        password_lbl.grid(row=3, column=0, pady=15)
        self.password_entry = Entry(main_frame, textvariable=self.password_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', show="*", width=30)
        self.password_entry.grid(row=3, column=1, pady=15, padx=20)

        confirm_password_lbl = Label(main_frame, text="Confirm Password", font=("Helvetica", 16), bg='#2c2f33', fg='white')
        confirm_password_lbl.grid(row=4, column=0, pady=15)
        self.confirm_password_entry = Entry(main_frame, textvariable=self.confirm_password_var, font=("Helvetica", 16), bg='#4b4f56', fg='white', show="*", width=30)
        self.confirm_password_entry.grid(row=4, column=1, pady=15, padx=20)

        # Frame for OTP, Reset, and Back buttons
        otp_reset_frame = Frame(main_frame, bg='#23272a')
        otp_reset_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # Buttons
        send_otp_btn = Button(otp_reset_frame, text="Send OTP", command=self.send_otp, font=("Helvetica", 16), bg='#7289da', fg='white', width=15)
        send_otp_btn.grid(row=0, column=0, padx=10)

        reset_password_btn = Button(otp_reset_frame, text="Reset Password", command=self.reset_password, font=("Helvetica", 16), bg='#7289da', fg='white', width=15)
        reset_password_btn.grid(row=0, column=1, padx=10)

        back_btn = Button(otp_reset_frame, text="Back", command=self.root.destroy, font=("Helvetica", 16), bg='#99aab5', fg='black', width=15)
        back_btn.grid(row=0, column=2, padx=10)


    def send_otp(self):
        email = self.email_var.get().strip()

        if email == "":
            messagebox.showerror("Error", "Email is required!")
        else:
            # Generate OTP
            self.otp = str(random.randint(1000, 9999))

            # Send OTP via email
            try:
                sender_email = "minglemarket72@gmail.com"  # Change to your email
                sender_password = "sspx vrba rdwq qwcn"  # Change to your email password
                recipient_email = email

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg['Subject'] = "Password Reset OTP"
                body = f"Your OTP for password reset is: {self.otp}"
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, recipient_email, text)
                server.quit()

                messagebox.showinfo("Success", "OTP sent to your email!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send OTP. {str(e)}")

    def reset_password(self):
        otp = self.otp_var.get().strip()
        new_password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if otp == "" or new_password == "" or confirm_password == "":
            messagebox.showerror("Error", "All fields are required!")
        elif otp != self.otp:
            messagebox.showerror("Error", "Invalid OTP!")
        elif new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
        else:
            # Update password in the database
            email = self.email_var.get().strip()

            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0607",  # Change to your MySQL password
                database="register"
            )
            cursor = connection.cursor()

            cursor.execute("UPDATE users SET password=%s WHERE email=%s", (new_password, email))
            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Password reset successfully!")
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()

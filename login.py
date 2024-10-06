import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
from tkinter import messagebox
import mysql.connector

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x450")
        self.root.config(bg='#2c2f33')  # Dark background

        # Variables
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.otp_var = StringVar()
        self.otp = None

        # Labels and Entries
        title_lbl = Label(self.root, text="Login System", font=("Helvetica", 20, "bold"), bg='#2c2f33', fg='white')
        title_lbl.pack(pady=10)

        username_lbl = Label(self.root, text="Username", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        username_lbl.pack(pady=5)
        self.username_entry = Entry(self.root, textvariable=self.username_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.username_entry.pack(pady=5)

        email_lbl = Label(self.root, text="Email", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        email_lbl.pack(pady=5)
        self.email_entry = Entry(self.root, textvariable=self.email_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.email_entry.pack(pady=5)

        password_lbl = Label(self.root, text="Password", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        password_lbl.pack(pady=5)
        self.password_entry = Entry(self.root, textvariable=self.password_var, font=("Helvetica", 12), bg='#23272a', fg='white', show="*")
        self.password_entry.pack(pady=5)

        # Buttons
        login_btn = Button(self.root, text="Login", command=self.login, font=("Helvetica", 12), bg='#7289da', fg='white')
        login_btn.pack(pady=10)

        register_btn = Button(self.root, text="Register", command=self.register_window, font=("Helvetica", 12), bg='#99aab5', fg='black')
        register_btn.pack(pady=5)

        forgot_btn = Button(self.root, text="Forgot Password", command=self.forgot_password_window, font=("Helvetica", 12), bg='#99aab5', fg='black')
        forgot_btn.pack(pady=5)

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
                database="face_recognition"
            )
            cursor = connection.cursor()

            # Query to check the username and password using case-insensitive comparison
            query = "SELECT * FROM users WHERE LOWER(username)=%s AND password=%s"
            cursor.execute(query, (username.lower(), password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", f"Welcome, {result[1]}!")
                self.root.destroy()  # Close the login window after successful login
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
        self.root.geometry("400x450")
        self.root.config(bg='#2c2f33')  # Dark background

        # Variables
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()

        # Labels and Entries
        title_lbl = Label(self.root, text="Register New User", font=("Helvetica", 18, "bold"), bg='#2c2f33', fg='white')
        title_lbl.pack(pady=10)

        username_lbl = Label(self.root, text="Username", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        username_lbl.pack(pady=5)
        self.username_entry = Entry(self.root, textvariable=self.username_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.username_entry.pack(pady=5)

        email_lbl = Label(self.root, text="Email", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        email_lbl.pack(pady=5)
        self.email_entry = Entry(self.root, textvariable=self.email_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.email_entry.pack(pady=5)

        password_lbl = Label(self.root, text="Password", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        password_lbl.pack(pady=5)
        self.password_entry = Entry(self.root, textvariable=self.password_var, font=("Helvetica", 12), bg='#23272a', fg='white', show="*")
        self.password_entry.pack(pady=5)

        # Buttons
        register_btn = Button(self.root, text="Register", command=self.register, font=("Helvetica", 12), bg='#7289da', fg='white')
        register_btn.pack(pady=10)

    def register(self):
        username = self.username_var.get().strip()
        email = self.email_var.get().strip()
        password = self.password_var.get()

        if username == "" or password == "" or email == "":
            messagebox.showerror("Error", "All fields are required!")
        else:
            # Connect to MySQL Database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0607",  # Change to your MySQL password
                database="face_recognition"
            )
            cursor = connection.cursor()

            # Query to insert new user (ensure unique username)
            query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (username, email, password))
                connection.commit()
                messagebox.showinfo("Success", "User registered successfully!")
                self.root.destroy()  # Close the registration window
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Username or Email already exists!")
            connection.close()


class ForgotPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("400x400")
        self.root.config(bg='#2c2f33')  # Dark background

        # Variables
        self.email_var = StringVar()
        self.otp_var = StringVar()
        self.new_password_var = StringVar()

        # Labels and Entries
        title_lbl = Label(self.root, text="Forgot Password", font=("Helvetica", 18, "bold"), bg='#2c2f33', fg='white')
        title_lbl.pack(pady=10)

        email_lbl = Label(self.root, text="Email", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        email_lbl.pack(pady=5)
        self.email_entry = Entry(self.root, textvariable=self.email_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.email_entry.pack(pady=5)

        otp_btn = Button(self.root, text="Send OTP", command=self.send_otp, font=("Helvetica", 12), bg='#7289da', fg='white')
        otp_btn.pack(pady=10)

        otp_lbl = Label(self.root, text="OTP", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        otp_lbl.pack(pady=5)
        self.otp_entry = Entry(self.root, textvariable=self.otp_var, font=("Helvetica", 12), bg='#23272a', fg='white')
        self.otp_entry.pack(pady=5)

        new_password_lbl = Label(self.root, text="New Password", font=("Helvetica", 12), bg='#2c2f33', fg='white')
        new_password_lbl.pack(pady=5)
        self.new_password_entry = Entry(self.root, textvariable=self.new_password_var, font=("Helvetica", 12), bg='#23272a', fg='white', show="*")
        self.new_password_entry.pack(pady=5)

        reset_btn = Button(self.root, text="Reset Password", command=self.reset_password, font=("Helvetica", 12), bg='#7289da', fg='white')
        reset_btn.pack(pady=10)

    def send_otp(self):
        email = self.email_var.get().strip()

        if email == "":
            messagebox.showerror("Error", "Email field is required!")
            return

        # Generate OTP
        self.otp = random.randint(100000, 999999)

        # Send OTP via email
        try:
            sender_email = "minglemarket72@gmail.com"  # Change to your sender email
            sender_password = "oynx subh zeut zvbk"     # Change to your app password
            subject = "Your OTP Code"
            body = f"Your OTP code is {self.otp}"

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)

            messagebox.showinfo("Success", "OTP sent to your email!")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Failed to authenticate. Check your email and app password.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP: {str(e)}")

    def reset_password(self):
        otp = self.otp_var.get().strip()
        new_password = self.new_password_var.get().strip()

        if not otp or not new_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if self.otp and otp == str(self.otp):
            email = self.email_var.get().strip()

            # Update the user's password in the database
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="0607",  # Change to your MySQL password
                database="face_recognition"
            )
            cursor = connection.cursor()

            query = "UPDATE users SET password=%s WHERE email=%s"
            cursor.execute(query, (new_password, email))
            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Password reset successfully!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid OTP!")


if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()

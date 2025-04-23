import  tkinter as tk
from tkinter import messagebox
import cv2
import os
import datetime
import face_recognition
from PIL import Image, ImageTk

blocked_images_db = "blocked_images.txt"
def register_student():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter both username and password!")
    else:
        with open("student_database.txt", "a") as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Success", "Student registered successfully!")
        reg_window.destroy()  # Close registration window after successful registration

def open_register_window():
    global reg_window
    reg_window = tk.Toplevel(root)
    reg_window.title("Register Student")

    reg_frame = tk.LabelFrame(reg_window, text="Register Student", padx=20, pady=20)
    reg_frame.pack(padx=20, pady=20)

    tk.Label(reg_frame, text="Username:").grid(row=0, column=0, pady=5, sticky="w")
    global reg_username_entry
    reg_username_entry = tk.Entry(reg_frame)
    reg_username_entry.grid(row=1, column=0, pady=5)

    tk.Label(reg_frame, text="Password:").grid(row=2, column=0, pady=5, sticky="w")
    global reg_password_entry
    reg_password_entry = tk.Entry(reg_frame, show="*")
    reg_password_entry.grid(row=3, column=0, pady=5)

    register_button = tk.Button(reg_frame, text="Register", command=register_student)
    register_button.grid(row=4, column=0, pady=10)
def capture_image_student():
    username = login_username_entry.get()

    with open(blocked_images_db, "r") as file:
        blocked_users = file.readlines()
    if username + "\n" in blocked_users:
        messagebox.showerror("Error", "Camera access is blocked for this user.")
        return

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    image_folder = "student_images"
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    image_path = os.path.join(image_folder, f"{username}.png")
    cv2.imwrite(image_path, frame)
    messagebox.showinfo("Image Captured", "Image captured successfully!")
def capture_attendance_dialog():
    capture_attendance_window = tk.Toplevel(root)
    capture_attendance_window.title("Capture Attendance")

    courses = ["Math", "Science", "History"]  # Example courses
    faculties = ["Dr. Smith", "Prof. Johnson", "Dr. Brown"]  # Example faculties

    course_label = tk.Label(capture_attendance_window, text="Select Course:")
    course_label.pack()
    course_var = tk.StringVar()
    course_dropdown = tk.OptionMenu(capture_attendance_window, course_var, *courses)
    course_dropdown.pack()

    faculty_label = tk.Label(capture_attendance_window, text="Select Faculty:")
    faculty_label.pack()
    faculty_var = tk.StringVar()
    faculty_dropdown = tk.OptionMenu(capture_attendance_window, faculty_var, *faculties)
    faculty_dropdown.pack()

    capture_button = tk.Button(capture_attendance_window, text="Capture Image", command=lambda: capture_student_attendance(course_var.get(), faculty_var.get()))
    capture_button.pack()
# ... (Previous code remains the same)
def capture_student_attendance(selected_course, selected_faculty):
    username = login_username_entry.get()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    # Assuming you have a folder named 'attendance_images' to store attendance images
    attendance_folder = "attendance_images"
    if not os.path.exists(attendance_folder):
        os.makedirs(attendance_folder)

    attendance_image_path = os.path.join(attendance_folder, f"{selected_course}_{selected_faculty}_{username}.png")
    cv2.imwrite(attendance_image_path, frame)

    # Load the captured image for face recognition
    captured_image = face_recognition.load_image_file(attendance_image_path)
    captured_face_encodings = face_recognition.face_encodings(captured_image)

    # Load the registered student's image for comparison
    student_image_folder = "student_images"
    student_image_path = os.path.join(student_image_folder, f"{username}.png")
    if not os.path.exists(student_image_path):
        messagebox.showerror("Error", "No registered image found for the student.")
        return

    registered_image = face_recognition.load_image_file(student_image_path)
    registered_face_encodings = face_recognition.face_encodings(registered_image)

    if not captured_face_encodings or not registered_face_encodings:
        messagebox.showerror("Error", "Face encodings not found. Attendance not captured.")
        return

    # Compare the face encodings
    for captured_face_encoding in captured_face_encodings:
        for registered_face_encoding in registered_face_encodings:
            results = face_recognition.compare_faces([captured_face_encoding], registered_face_encoding)

            # If faces match, record attendance details
            if results[0]:  # Assuming results indicate successful recognition
                # Get the current date
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")

                # Append attendance record to the file
                with open("attendance_records.txt", "a") as file:
                    file.write(f"{current_date},{selected_course},{selected_faculty},{username},Present\n")

                # Show attendance captured message
                messagebox.showinfo("Attendance Captured", "Attendance captured successfully!")
                return

    # Show error if face recognition fails
    messagebox.showerror("Error", "Attendance not captured. Face recognition failed.")

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    with open("student_database.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", f"Welcome {username} (Student)")
                open_student_panel(username)
                return
    if username == "teacher" and password == "teacher@123":
        messagebox.showinfo("Success", "Welcome Teacher")
        open_teacher_panel()
        return

    messagebox.showerror("Error", "Invalid credentials!")
def read_student_data():
    try:
        with open("student_database.txt", "r") as file:
            lines = file.readlines()

        return [line.strip().split(",") for line in lines]
    except FileNotFoundError:
        messagebox.showerror("Error", "Student database not found.")
        return []
def view_student_details():
    student_data = read_student_data()
    if student_data:
        details = "\n".join([f"Username: {line[0]}, Password: {line[1]}" for line in student_data])
        messagebox.showinfo("Student Details", f"Student Details:\n{details}")
    else:
        messagebox.showinfo("Student Details", "No students found.")

def view_student_images():
    image_folder = "student_images"
    if not os.path.exists(image_folder):
        messagebox.showinfo("Info", "No student images found.")
        return

    image_files = os.listdir(image_folder)
    if not image_files:
        messagebox.showinfo("Info", "No student images found.")
    else:
        # Create a new window to display the images and names
        image_display_window = tk.Toplevel(root)
        image_display_window.title("Student Images")

        # Fetch student data (assuming the images' names correspond to the student usernames)
        student_data = read_student_data()

        # Loop through each image file and display it along with the name
        for image_file in image_files:
            username, _ = os.path.splitext(image_file)  # Get the username from the image file name

            # Find the corresponding name from student data
            student_name = ""
            for student in student_data:
                if student[0] == username:
                    student_name = student[0]  # Assuming username is the first element in student_data

            if student_name:
                image_path = os.path.join(image_folder, image_file)

                # Open and resize the image using PIL
                image = Image.open(image_path)
                image.thumbnail((200, 200))  # Adjust the size as needed

                # Convert the image to a format compatible with Tkinter
                tk_image = ImageTk.PhotoImage(image)

                # Display the name and image in a label
                name_label = tk.Label(image_display_window, text=student_name)
                name_label.pack()

                image_label = tk.Label(image_display_window, image=tk_image)
                image_label.image = tk_image  # Keep a reference to avoid garbage collection
                image_label.pack()

def block_camera_access():
    username_to_block = block_camera_entry.get()
    with open(blocked_images_db, "a") as file:
        file.write(username_to_block + "\n")
    messagebox.showinfo("Success", f"Camera access blocked for {username_to_block}")
def unblock_camera_access():
    username_to_unblock = block_camera_entry.get()
    with open(blocked_images_db, "r") as file:
        lines = file.readlines()
    with open(blocked_images_db, "w") as file:
        for line in lines:
            if line.strip() != username_to_unblock:
                file.write(line)
    messagebox.showinfo("Success", f"Camera access unblocked for {username_to_unblock}")

def delete_student():
    student_data = read_student_data()
    if student_data:
        username_to_delete = delete_username_entry.get()
        remaining_students = [student for student in student_data if student[0] != username_to_delete]

        with open("student_database.txt", "w") as file:
            for student in remaining_students:
                file.write(",".join(student) + "\n")
        messagebox.showinfo("Success", f"Student {username_to_delete} deleted.")
    else:
        messagebox.showinfo("Student Details", "No students found.")

# Function to open the student panel
def open_student_panel(username):
    student_panel = tk.Toplevel(root)
    student_panel.title(f"Welcome {username} (Student)")

    welcome_label = tk.Label(student_panel, text=f"Welcome {username}!", font=("Arial", 20))
    welcome_label.pack(padx=20, pady=20)

    capture_attendance_button = tk.Button(student_panel, text="Capture Attendance", command=capture_attendance_dialog)
    capture_attendance_button.pack(padx=0, pady=10)

    capture_image_button = tk.Button(student_panel, text="Capture Image", command=capture_image_student)
    capture_image_button.pack(padx=0, pady=10)

    logout_button = tk.Button(student_panel, text="Logout", command=student_panel.destroy)
    logout_button.pack(padx=0, pady=10)
def recognize_face(username):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    # Assuming you have a folder named 'student_images' to store student images
    student_image_folder = "student_images"
    if not os.path.exists(student_image_folder):
        messagebox.showerror("Error", "No student images found.")
        return

    # Load the student's image
    student_image_path = os.path.join(student_image_folder, f"{username}.png")
    student_image = face_recognition.load_image_file(student_image_path)
    student_face_encodings = face_recognition.face_encodings(student_image)

    # Encode the captured face
    captured_face_encoding = face_recognition.face_encodings(frame)

    # Compare the face encodings
    if captured_face_encoding:
        for captured_encoding in captured_face_encoding:
            for student_encoding in student_face_encodings:
                results = face_recognition.compare_faces([captured_encoding], student_encoding)

                # If faces match, show a success message
                if results[0]:
                    messagebox.showinfo("Face Recognition", "Face recognized successfully!")
                    return

        # If faces do not match, show an error message
        messagebox.showerror("Face Recognition", "Face recognition failed. Face does not match the student's image.")

def read_attendance_data():
    try:
        with open("attendance_records.txt", "r") as file:
            attendance_data = file.readlines()
        return attendance_data
    except FileNotFoundError:
        return []
def view_attendance_dialog():
    view_attendance_window = tk.Toplevel(root)
    view_attendance_window.title("View Attendance")

    attendance_data = read_attendance_data()  # Function to read attendance data

    if attendance_data:
        for record in attendance_data:
            record_details = record.split(',')
            if len(record_details) == 5:
                current_date, selected_course, selected_faculty, username, status = record_details

                # Assuming the images are stored in the 'attendance_images' folder
                attendance_image_path = f"attendance_images/{selected_course}_{selected_faculty}_{username}.png"

                attendance_frame = tk.Frame(view_attendance_window, padx=10, pady=10)
                attendance_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

                # Display the attendance details
                details_label = tk.Label(attendance_frame, text=f"Date: {current_date}, Course: {selected_course}, Faculty: {selected_faculty}, Username: {username}, Status: {status}")
                details_label.pack()

                # Open the captured image using PIL
                try:
                    image = Image.open(attendance_image_path)
                    image.thumbnail((200, 200))  # Adjust the size as needed

                    # Convert the image to a format compatible with Tkinter
                    tk_image = ImageTk.PhotoImage(image)

                    # Display the image in a label
                    image_label = tk.Label(attendance_frame, image=tk_image)
                    image_label.image = tk_image  # Keep a reference to avoid garbage collection
                    image_label.pack()
                except FileNotFoundError:
                    error_label = tk.Label(attendance_frame, text="Image not found.")
                    error_label.pack()
            else:
                error_label = tk.Label(view_attendance_window, text=f"Invalid attendance record: {record}")
                error_label.pack(padx=20, pady=20)
    else:
        no_data_label = tk.Label(view_attendance_window, text="No attendance records found.")
        no_data_label.pack(padx=20, pady=20)

def open_teacher_panel():
    teacher_panel = tk.Toplevel(root)
    teacher_panel.title("Welcome Teacher")

    welcome_label = tk.Label(teacher_panel, text="Welcome Teacher!", font=("Arial", 20))
    welcome_label.pack(padx=20, pady=20)

    view_attendance_button = tk.Button(teacher_panel, text="View Attendance", command=view_attendance_dialog)
    view_attendance_button.pack(pady=(0, 10))  # Add vertical space between this button and the next one

    view_details_button = tk.Button(teacher_panel, text="View Student Details", command=view_student_details)
    view_details_button.pack(pady=(0, 10))  # Add vertical space between this button and the next one

    delete_username_label = tk.Label(teacher_panel, text="Enter Student Username to Delete:")
    delete_username_label.pack()

    global delete_username_entry
    delete_username_entry = tk.Entry(teacher_panel)
    delete_username_entry.pack()

    delete_student_button = tk.Button(teacher_panel, text="Delete Student", command=delete_student)
    delete_student_button.pack(pady=(10, 0))  # Add vertical space between this button and the previous one

    view_images_button = tk.Button(teacher_panel, text="View Student Images", command=view_student_images)
    view_images_button.pack(pady=(10, 0))  # Add vertical space between this button and the previous one

    block_camera_label = tk.Label(teacher_panel, text="Enter Username to Block Camera Access:")
    block_camera_label.pack()

    global block_camera_entry
    block_camera_entry = tk.Entry(teacher_panel)
    block_camera_entry.pack()

    block_camera_button = tk.Button(teacher_panel, text="Block Camera", command=block_camera_access)
    block_camera_button.pack(pady=(10, 0))  # Add vertical space between this button and the previous one

    unblock_camera_button = tk.Button(teacher_panel, text="Unblock Camera", command=unblock_camera_access)
    unblock_camera_button.pack(pady=(10, 0))  # Add vertical space between this button and the previous one

    logout_button = tk.Button(teacher_panel, text="Logout", command=teacher_panel.destroy)
    logout_button.pack(padx=0, pady=10)

root = tk.Tk()
root.title("Student Attendance System")
root.configure(bg="black")
def set_styles():
    root.tk_setPalette(background="#000000", foreground="#ffffff")
    root.option_add("*Font", "Arial 10")
    root.option_add("*Label.Font", "Arial 12 bold")
    root.option_add("*Button.Background", "#4caf50")
    root.option_add("*Button.Foreground", "white")
    root.option_add("*Button.Relief", "flat")
    root.option_add("*Button.Width", 15)
    root.option_add("*Entry.Width", 20)

set_styles()

title_label = tk.Label(root, text="Attendance Recognition System", bg="black", fg="white")
title_label.pack(padx=20, pady=20)

login_frame = tk.LabelFrame(root, text="Login", padx=20, pady=20)
login_frame.pack(padx=20, pady=20)

tk.Label(login_frame, text="Username:").grid(row=0, column=0, pady=5, sticky="w")
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=1, column=0, pady=5)

tk.Label(login_frame, text="Password:").grid(row=2, column=0, pady=5, sticky="w")
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.grid(row=3, column=0, pady=5)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=4, column=0, pady=10)

register_window_button = tk.Button(login_frame, text="Register", command=open_register_window)
register_window_button.grid(row=5, column=0, pady=10)

root.mainloop()

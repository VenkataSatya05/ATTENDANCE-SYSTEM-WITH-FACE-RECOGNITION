# Attendance System with Face Recognition

## 📌 Introduction

The **Attendance System with Face Recognition** is a Python-based application that automates attendance tracking using advanced facial recognition technology. Featuring an intuitive graphical user interface (GUI) built with Tkinter, the system leverages computer vision and a folder-based database to deliver a secure, scalable, and user-friendly solution for educational institutions, offices, and events.

**Key Features:**
- 😊 **Facial Recognition**: Accurately identifies students using the `face_recognition` library for real-time attendance marking.
- 🖥️ **GUI Interface**: Tkinter-powered interface ensures seamless navigation for students and teachers.
- 👩‍🎓 **Student Management**: Supports registration, image capture, and attendance tracking, with teacher controls for record access and management.
- 🔒 **Security Features**: Enables camera access blocking/unblocking to prevent attendance malpractice.
- 📂 **Scalable Database**: Stores images and records in folders (`student_images`, `attendance_records.txt`) for flexible management.
- ⚡ **Real-Time Processing**: Instantly captures and processes facial data for efficient attendance monitoring.

This system boosts accuracy, minimizes manual errors, and provides a robust platform for modern attendance management.

## 🛠 Tech Stack

| Layer              | Tools/Frameworks           |
|--------------------|----------------------------|
| Frontend (GUI)     | Tkinter                    |
| Computer Vision    | OpenCV                     |
| Facial Recognition | face_recognition           |
| Image Processing   | PIL (Pillow)               |
| Database           | Folder-based (text files)  |

## 🏛️ Overall Workflow

1. **Login/Registration**: Students register with a username and password, stored in `student_database.txt`. Teachers use default credentials (`teacher`, `teacher@123`).
2. **Image Capture**: Students capture facial images, saved in the `student_images` folder.
3. **Attendance Marking**: Students select a course and faculty, capture an image, and the system verifies it against the registered image using facial recognition.
4. **Teacher Controls**: Teachers view attendance records, student details, and images, delete students, and manage camera access via `blocked_images.txt`.
5. **Output**: Attendance records are saved in `attendance_records.txt`, with visual feedback provided through the GUI.

![Workflow Diagram Placeholder]
*(Note: Include a diagram illustrating the login, image capture, recognition, and record storage process if possible.)*

## 📦 Libraries Used

- **Tkinter**: Creates the graphical user interface.
- **OpenCV**: Handles image acquisition and processing.
- **face_recognition**: Extracts and compares facial features.
- **Pillow (PIL)**: Manages image handling and display in the GUI.
- **datetime**: Timestamps attendance records.
- **os**: Manages file and folder operations.

## 🏃‍♂️ Getting Started

These instructions will help you set up and run the Attendance System on your local machine for development and testing.

### 📋 Prerequisites

- Python 3.8 or higher.
- A webcam for image capture.
- Git for repository cloning.

### 🧱 Setting Up Your Development Environment

1. **Install Git**:
   - Download and install Git from [git-scm.com](https://git-scm.com/).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/VenkataSatya05/Attendance-System-Face-Recognition.git

3. **Install Dependencies**:
   - Navigate to the project directory and install the required Python libraries:
   ```bash
   pip install opencv-python face_recognition pillow

4. **Run the Application**:
   - Execute the main script to launch the GUI:
   ```bash
   python main.py

5.Default Teacher Credentials:

- **Username**: teacher

- **Password**: teacher@123

## 👀 Application Preview

![image](https://github.com/user-attachments/assets/6a97a710-e774-45f7-afe7-95954f729611)

![image](https://github.com/user-attachments/assets/6b6492df-46e7-4a8a-b9bc-13e4877b3e75)

- After get registered student can login with their respective credentials.

![image](https://github.com/user-attachments/assets/a149992d-a620-4600-875b-048ef9f28120)

- Teacher may log in using the default credentials, which are teacher@123 and user name:teacher.

![image](https://github.com/user-attachments/assets/d6c39452-a865-4a8c-8212-1ecb9acfc9b9)
![image](https://github.com/user-attachments/assets/f6cb6b80-c663-43ea-b45f-7b4be3bd730a)

- Students must take a picture of themselves as soon as they log in to their desks in order for facial detection to be utilized to take attendance.

![image](https://github.com/user-attachments/assets/9c911c4a-b638-4907-b5e0-00833b3945f0)

- Teachers are required to block student images once they are taken in order to prevent subsequent students from taking pictures of themselves until the instructor removes the block. This prevents future students from engaging in unethical attendance practices.

![image](https://github.com/user-attachments/assets/02ccb4a2-8cf4-4e0e-b795-23821ee58480)

- Following this, students can record their attendance by choosing a subject and faculty member. If the image recognition process matches the picture the student took, they will receive their attendance; if not, it will be denied.

![image](https://github.com/user-attachments/assets/42433b1a-aa1b-490c-aff5-2d73c65aabd0)

![image](https://github.com/user-attachments/assets/83e90eca-7774-4f4c-a38f-13a8dec9d592)

![image](https://github.com/user-attachments/assets/517cb3dc-f1f5-47db-93c2-c6c2afe0c495)

- Once students give their attendance teacher can view students attendance in their desk.

![image](https://github.com/user-attachments/assets/a7e16501-4403-4e40-92b3-681aacd4f85d)

## 📝 Why This Project?

Manual attendance systems are prone to errors, time-consuming, and vulnerable to proxy attendance. The Attendance System with Face Recognition addresses these issues by:

- Enhancing Accuracy: Uses facial recognition to ensure only authorized individuals are marked present.

- Improving Efficiency: Automates attendance tracking, saving time for educators and administrators.

- Ensuring Security: Features like camera access blocking prevent misuse.

- User-Friendly Design: The Tkinter GUI is accessible to users with minimal technical expertise.

- Scalability: The folder-based database supports dynamic organizational needs.

6.This project showcases the integration of computer vision and GUI design to solve real-world problems in attendance management.

## 🏃‍♂️ How We Came to Solve This Problem?

The project was developed to address the limitations of traditional attendance systems:

- Automation: Replaces manual roll-calls with real-time facial recognition.

- **Security**: Prevents proxy attendance through image-based verification and access controls.

- **Accessibility**: Provides an intuitive GUI for students and teachers, regardless of technical background.

- **Flexibility**: Supports diverse environments like classrooms, offices, or events.

- **Future Potential**: Can be enhanced with real-time notifications, cloud storage, or advanced recognition algorithms.

## 🎓 Resources

New to Python or computer vision? Start here:

- https://docs.opencv.org/4.x/index.html

- https://pypi.org/project/face-recognition/

- https://docs.python.org/3/library/tkinter.html

- https://pillow.readthedocs.io/en/stable/

## ✨ Team

Thanks to these contributors:

- Venkata Satya (CB.EN.U4AIE22005)

- Kolla Lokesh (CB.EN.U4AIE22027)

- Goli Surya Teja (CB.EN.U4AIE22069)

- Rama Krishna Prasad (CB.EN.U4AIE22070)

- Project Guide: Ms. Sreelakshmi K

## 🙌 Contributing

We welcome contributions! Please read our Contributing Guidelines and submit pull requests to enhance features or fix issues.

Built with 💻 by Group-12, Batch A, at Amrita School of Artificial Intelligence, Amrita Vishwa Vidyapeetham.

## 🧠 Remember

- A webcam and sufficient lighting are required for accurate facial recognition.
- Ensure dlib is installed for face_recognition (may require CMake and a C++ compiler).
- The folder-based database (student_images, attendance_images) must be writable.
- Replace VenkataSatya05 in the clone command with your actual GitHub username if different.











































































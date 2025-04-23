# Attendance System with Face Recognition

## 📌 Introduction

The Attendance System with Face Recognition is a Python-based application designed to automate and streamline attendance tracking using facial recognition technology. Built with an intuitive graphical user interface (GUI), the system leverages computer vision and a folder-based database structure to provide a secure, scalable, and user-friendly solution for educational institutions, offices, and events.

Key Features:

Facial Recognition: Accurately identifies students using the face_recognition library for real-time attendance marking.

GUI Interface: Built with Tkinter, offering easy navigation for students and teachers.

Student Management: Supports registration, image capture, and attendance tracking, with teacher controls for viewing records and managing access.

Security Features: Includes camera access blocking/unblocking to prevent malpractice.

Scalable Database: Uses a folder-based structure for storing student images and attendance records, ensuring flexibility and ease of management.

Real-Time Processing: Captures and processes facial data instantly for efficient attendance monitoring.

The system enhances accuracy, reduces manual errors, and provides a robust platform for modern attendance management.

## 🛠 Tech Stack

Layer	Tools/Frameworks

Frontend (GUI)	Tkinter

Computer Vision	OpenCV

Facial Recognition	face_recognition

Image Processing	PIL (Pillow)

Database	Folder-based (text files)

## 🏛️ Overall Workflow
Login/Registration: Students register with a username and password, stored in student_database.txt. Teachers access the system with default credentials.

Image Capture: Students capture their facial image, saved in the student_images folder.

Attendance Marking: Students select a course and faculty, capture an image, and the system compares it with the registered image using facial recognition.

Teacher Controls: Teachers can view attendance records, student details, and images, delete students, and block/unblock camera access.

Output: Attendance records are stored in attendance_records.txt, with visual feedback via the GUI.

![Workflow Diagram Placeholder]
(Note: Include a diagram illustrating the login, image capture, recognition, and record storage process if possible.)


## 📦 Libraries Used

Tkinter: For creating the GUI.

OpenCV: For image acquisition and processing.

face_recognition: For facial feature extraction and comparison.

Pillow (PIL): For image handling and display in the GUI.

datetime: For timestamping attendance records.

os: For file and folder management.

## 🏃‍♂️ Getting Started

These instructions will help you set up and run the Attendance System on your local machine for development and testing.

## 📋 Prerequisites

1.Python 3.8 or higher.

2.A webcam for image capture.

3.Git for repository cloning.

## 🧱 Setting Up Your Development Environment

1.Install Git:
Download and install Git from git-scm.com.

2.Clone the Repository:

git clone https://github.com/YOUR-USERNAME/Attendance-System-Face-Recognition.git

3.Install Dependencies: Navigate to the project directory and install the required Python libraries:

pip install opencv-python face_recognition pillow

4.Run the Application: Execute the main script to launch the GUI:

python main.py

5.Default Teacher Credentials:

Username: teacher

Password: teacher@123

## 👀 Application Preview

![image](https://github.com/user-attachments/assets/6a97a710-e774-45f7-afe7-95954f729611)

![image](https://github.com/user-attachments/assets/6b6492df-46e7-4a8a-b9bc-13e4877b3e75)

After get registered student can login with their respective credentials.

![image](https://github.com/user-attachments/assets/a149992d-a620-4600-875b-048ef9f28120)

Teacher may log in using the default credentials, which are teacher@123 and user name:teacher.

![image](https://github.com/user-attachments/assets/d6c39452-a865-4a8c-8212-1ecb9acfc9b9)
![image](https://github.com/user-attachments/assets/f6cb6b80-c663-43ea-b45f-7b4be3bd730a)

Students must take a picture of themselves as soon as they log in to their desks in order for facial detection to be utilized to take attendance.

![image](https://github.com/user-attachments/assets/9c911c4a-b638-4907-b5e0-00833b3945f0)

Teachers are required to block student images once they are taken in order to prevent subsequent students from taking pictures of themselves until the instructor removes the block. This prevents future students from engaging in unethical attendance practices.

![image](https://github.com/user-attachments/assets/02ccb4a2-8cf4-4e0e-b795-23821ee58480)

Following this, students can record their attendance by choosing a subject and faculty member. If the image recognition process matches the picture the student took, they will receive their attendance; if not, it will be denied.

![image](https://github.com/user-attachments/assets/42433b1a-aa1b-490c-aff5-2d73c65aabd0)

![image](https://github.com/user-attachments/assets/83e90eca-7774-4f4c-a38f-13a8dec9d592)

![image](https://github.com/user-attachments/assets/517cb3dc-f1f5-47db-93c2-c6c2afe0c495)

Once students give their attendance teacher can view students attendance in their desk.

![image](https://github.com/user-attachments/assets/a7e16501-4403-4e40-92b3-681aacd4f85d)

## 📝 Why This Project?

Manual attendance systems are prone to errors, time-consuming, and vulnerable to proxy attendance. The Attendance System with Face Recognition addresses these issues by:

1.Enhancing Accuracy: Uses facial recognition to ensure only authorized individuals are marked present.

2.Improving Efficiency: Automates attendance tracking, saving time for educators and administrators.

3.Ensuring Security: Features like camera access blocking prevent misuse.

4.User-Friendly Design: The Tkinter GUI is accessible to users with minimal technical expertise.

5.Scalability: The folder-based database supports dynamic organizational needs.

6.This project showcases the integration of computer vision and GUI design to solve real-world problems in attendance management.

## 🏃‍♂️ How We Came to Solve This Problem?

The project was developed to address the limitations of traditional attendance systems:

1.Automation: Replaces manual roll-calls with real-time facial recognition.

2.Security: Prevents proxy attendance through image-based verification and access controls.

3.Accessibility: Provides an intuitive GUI for students and teachers, regardless of technical background.

4.Flexibility: Supports diverse environments like classrooms, offices, or events.

5.Future Potential: Can be enhanced with real-time notifications, cloud storage, or advanced recognition algorithms.

## 🎓 Resources

New to Python or computer vision? Start here:

1.https://docs.opencv.org/4.x/index.html

2.https://pypi.org/project/face-recognition/

3.https://docs.python.org/3/library/tkinter.html

4.https://pillow.readthedocs.io/en/stable/

## ✨ Team

Thanks to these contributors:

Venkata Satya (CB.EN.U4AIE22005)

Kolla Lokesh (CB.EN.U4AIE22027)

Goli Surya Teja (CB.EN.U4AIE22069)

Rama Krishna Prasad (CB.EN.U4AIE22070)

Project Guide: Ms. Sreelakshmi K

## 🙌 Contributing
We welcome contributions! Please read our Contributing Guidelines and submit pull requests to enhance features or fix issues.

Built with 💻 by Group-12, Batch A, at Amrita School of Artificial Intelligence, Amrita Vishwa Vidyapeetham.

## 🧠 Remember
The project relies on a webcam for image capture and requires sufficient lighting for accurate facial recognition. Ensure all dependencies are installed correctly, as the face_recognition library may require additional setup on some systems (e.g., dlib installation).











































































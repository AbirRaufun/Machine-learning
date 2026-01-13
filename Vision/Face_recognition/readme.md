# 🔍 Face Recognition using FaceNet and Transfer Learning

This project demonstrates a real-time face recognition system using **FaceNet** (for generating face embeddings), **MTCNN** (for detecting faces), and **KNN** (for classifying known vs unknown faces). It was developed as a team project by Abir, Shakil, and Amit.

## 📌 Project Overview

We built a deep learning-based face recognition pipeline with the following key steps:

1. **Video to Face Dataset**
   - Input: 2-minute videos of each person.
   - Output: ~200 cropped face images per person using **MTCNN**.

2. **Face Embedding Generation**
   - We used a pre-trained **FaceNet** model (`keras-facenet`) to convert face images into 128-dimensional embeddings.

3. **Classification with KNN**
   - The generated embeddings were used to train a **K-Nearest Neighbors (KNN)** classifier.
   - During recognition, embeddings of detected faces are compared and labeled.

4. **Real-Time Recognition**
   - Integrated with a webcam using **OpenCV**.
   - Draws bounding boxes and names over detected faces.
   - If a face doesn't match closely enough, it's labeled as **"Unknown"**.

## 🧠 Key Features

- ✅ Transfer learning with FaceNet (no training from scratch)
- ✅ Face detection using MTCNN
- ✅ Embedding comparison with KNN
- ✅ Live webcam-based recognition using OpenCV
- ✅ Unknown face detection using a distance threshold

## 🗃️ Folder Structure
FaceNet_Project/
├── Abir_faces/
├── Shakil_faces/
├── Amit_faces/
├── embeddings.npy
├── labels.npy
└── realtime_face_recognition.py

## 📦 Technologies Used

- Python
- FaceNet (`keras-facenet`)
- MTCNN
- OpenCV
- NumPy
- scikit-learn (KNN classifier)

## ⚙️ How to Run Locally

1. **Install dependencies:**

1.bash
pip install keras-facenet mtcnn opencv-python scikit-learn 
2.Run the real-time recognition script:
python realtime_face_recognition.py
Press q to exit the webcam window.

🎯 Future Improvements
Add more robust classifier like SVM or a deep classifier

Train with more faces and images

Improve unknown face detection logic

Add GUI for easier testing and dataset creation

🤝 Team Members
Abir

Shakil

Amit


---

Let me know if you want the `.md` file directly or want to include demo images/GIFs in the GitHub repo too!



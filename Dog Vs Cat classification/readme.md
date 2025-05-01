# 🐶🐱 Dogs vs Cats Image Classification

This project focuses on binary image classification: **distinguishing between images of dogs and cats** using deep learning techniques. It demonstrates both **custom CNN modeling** and **transfer learning using MobileNetV2**, showing comparisons between the two.

---

## 📌 Project Overview

- Dataset: [Kaggle Dogs vs Cats Dataset](https://www.kaggle.com/c/dogs-vs-cats)
- Number of images used: **3,000** (from the original 25,000)
- Image Preprocessing: Resized to **224x224**
- Labels:
  - Dog → `1`
  - Cat → `0`

---

## ✅ Tasks Completed

### 🔽 1. Data Acquisition and Preprocessing
- Downloaded dataset using **Kaggle API**
- Unzipped and extracted `train.zip`
- Counted number of cat and dog images
- Displayed sample images
- Created a directory to store resized images (224x224)
- Converted and saved 3,000 images in RGB format

### 🏷️ 2. Label Creation
- Assigned binary labels based on file names (`dog.` or `cat.`)

### 📊 3. Dataset Conversion
- Converted image data to NumPy arrays using OpenCV
- Split into train and test sets (80:20)
- Scaled pixel values to [0,1]

### 🧠 4. Model 1: Custom CNN
- Built a CNN from scratch using Keras
- Layers: Conv2D → MaxPooling → Flatten → Dense
- Output: 2 neurons with `softmax` for binary classification

### 🤖 5. Model 2: Transfer Learning with MobileNetV2
- Used **TensorFlow Hub** MobileNetV2 as a frozen feature extractor
- Added custom Dense layers on top
- Compiled and trained the model using `sparse_categorical_crossentropy`

### 📈 6. Model Training & Comparison
- Trained both models for 10 epochs
- Plotted:
  - Accuracy (Train vs Val)
  - Loss (Train vs Val)

### 📉 7. Evaluation Metrics
Calculated performance on the test set for both models:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

### 🔍 8. Predictive System
- Accepts image path as input
- Predicts using both CNN and Transfer Learning model
- Displays:
  - Prediction
  - Confidence
  - Warning if confidence < 70%
  - Shows image using OpenCV

---

## 📊 Results

| Metric      | Custom CNN | MobileNet (Transfer Learning) |
|-------------|------------|-------------------------------|
| Accuracy    | ✅ X.XX     | ✅ Y.YY                       |
| Precision   | ✅ X.XX     | ✅ Y.YY                       |
| Recall      | ✅ X.XX     | ✅ Y.YY                       |
| F1 Score    | ✅ X.XX     | ✅ Y.YY                       |

*(Replace X.XX and Y.YY with actual results)*

---

## ⚖️ Advantages & Disadvantages

### ✅ Transfer Learning (MobileNetV2)
**Advantages:**
- High accuracy with fewer training epochs
- Efficient use of pre-trained weights
- Reduces need for large datasets

**Disadvantages:**
- Less flexible/customizable
- Larger model size if not carefully optimized
- Can be a black box if not understood well

---

### ✅ Custom CNN
**Advantages:**
- Full control over architecture
- Simpler and easier to understand/debug
- Good for learning and experimentation

**Disadvantages:**
- Lower performance on small datasets
- Requires more tuning and training time
- Prone to underfitting/overfitting

---

## 🔧 Tools & Libraries

- Python
- TensorFlow & TensorFlow Hub
- Keras
- NumPy, OpenCV, PIL
- Matplotlib
- Scikit-learn

---

## 🚀 Future Improvements

- Use full dataset (25,000 images)
- Try other transfer learning models (Inception, ResNet)
- Add real-time prediction via webcam
- Deploy using Streamlit or Flask
- Implement model quantization for mobile

---

## 👨‍💻 Author

**Sheikh Abir Islam**  
📧 abirraufun1234@gmail.com

---

## 🏁 Conclusion

This project is a practical demonstration of deep learning for binary image classification using both traditional CNN and modern transfer learning. It highlights the **trade-offs between simplicity and performance**, and serves as a strong foundation for computer vision learning.



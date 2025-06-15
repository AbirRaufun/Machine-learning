# 🍱 Food Image Segmentation using U-Net (TensorFlow)

This project performs semantic segmentation on Bangladeshi meal plate images using a custom-trained U-Net model in TensorFlow. It identifies and segments multiple food items like Rice, Meat, Fish, Egg, Salad, and more from an image. Ideal for smart cafeteria, food logging, or health-related applications.

---

## 🔍 Project Overview

- **Task**: Multi-class Image Segmentation (pixel-wise classification)
- **Model**: U-Net (customized) implemented in TensorFlow/Keras
- **Input Shape**: 256x256 RGB Images
- **Output**: Segmentation masks with 12 classes
- **Tools**: Python, TensorFlow, NumPy, Matplotlib, Google Colab, Roboflow

---

## 📁 Dataset

- **Source**: Annotated using Roboflow (image + mask pairs)
- **Classes (11)**:
  - 0: Background
  - 1: Chicken Curry
  - 2: Egg
  - 3: Egg Slice
  - 4: Fish
  - 5: Khichuri
  - 6: Meat
  - 7: Others
  - 8: Rice
  - 9: Salad
  - 10: Vegetables

Each image has a corresponding segmentation mask with pixel values mapped to class indices.

---

## 🧠 Model Summary

- U-Net style encoder-decoder
- Uses Conv2D, MaxPooling, BatchNormalization, and UpSampling layers
- Final layer uses `Softmax` with 12 channels (one per class)
- Loss: `SparseCategoricalCrossentropy`
- Optimizer: `Adam`
- Metrics: `Accuracy`

---

## 🏋️ Training Details

- Epochs: 20
- Input Size: 256x256
- Batch Size: 10
- Achieved val_accuracy: ~80%
- Loss dropped steadily (checked using accuracy/loss plots)

---

## 🎯 Results

- Ground truth masks vs predicted masks were visualized using `jet` colormap
- Custom RGB mapping for classes is available for better color-coded visualization
- Predicted masks show strong segmentation in food-rich areas

---

## 🧪 Inference

- You can run predictions on test images
- Output: side-by-side visualization of:
  - Input image
  - Ground truth mask
  - Predicted mask

---

## 👨‍💻 Team Members

- Abir
- Shakil
- Amit

---

## 📦 Folder Structure
/project_root
│
├── dataset/ # train/valid/test images and masks
├── notebooks/ # Colab notebooks used for training
├── model/ # Trained model (.h5)
├── visualize/ # Output plots and prediction samples
└── README.md # This file

---

## 📌 To Run

- Upload `dataset/` to Google Drive or local
- Run training or testing notebooks
- Model checkpoints are saved for reuse

---

## ✅ Future Plans

- Convert to .exe or web app for demo
- Add nutrition estimation based on segmented regions
- Deploy model on edge device or Flask API

---

Thanks for checking out our project! 🌟
---

## 👤 Author

**Abir Islam**  
📧 abirraufun369@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sheikhabirislam369) | [GitHub](https://github.com/AbirRaufun)


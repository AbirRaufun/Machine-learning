# 🌾 Crop Classification Using Neural Networks 🌾

## 📋 Project Overview

This project aims to classify crop types based on two key features: **Rainfall (mm)** and **Temperature (°C)**. The goal is to predict crop types such as **Wheat**, **Rice**, **Maize**, **Barley**, and **Sugarcane** using a **Neural Network** model. A synthetic dataset is generated using `make_blobs`, and the neural network is trained to categorize the crops based on these features.

## ⚙️ Model Details

### Model Used: **Fully Connected Neural Network (FCNN)**

We chose a **Fully Connected Neural Network** because:

- 🌐 **Neural Networks** excel at handling complex patterns and relationships, making them ideal for classification tasks like this one.
- 🔄 **Backpropagation** and the **ReLU activation function** allow the model to efficiently learn and optimize the weights to improve classification accuracy.
- 🔢 **Softmax** is used in the output layer to handle multi-class classification and to calculate the probability of each class.

#### Architecture:
- **Input Layer**: 2 nodes (representing Rainfall and Temperature).
- **Hidden Layers**: 3 hidden layers, each with 500 neurons, using ReLU activation.
- **Output Layer**: 5 nodes (one for each crop type) using the softmax function.

### Why This Model?

The FCNN was selected due to:
- Its ability to **learn complex, nonlinear relationships** between features (Rainfall and Temperature) and crop types.
- Its flexibility in handling **multi-class classification** problems like this one.

## 📊 Features

### Input Features:
- 🌧️ **Rainfall (mm)**
- 🌡️ **Temperature (°C)**

### Output Classes (Predicted Crop Type):
1. 🌾 **Wheat**
2. 🌾 **Rice**
3. 🌽 **Maize**
4. 🌾 **Barley**
5. 🍬 **Sugarcane**

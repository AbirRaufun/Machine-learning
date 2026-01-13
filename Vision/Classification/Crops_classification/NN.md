# 🌾 **Crop Classification Neural Network** 🌾

## Overview
The **Crop Classification Neural Network** project leverages **environmental data** to predict the most suitable crop for a given region. By analyzing key environmental factors like **Rainfall (mm)** and **Temperature (°C)**, the model helps farmers make informed decisions about crop selection based on prevailing climatic conditions.

Using a **Multi-Layer Perceptron (MLP)** neural network, the system is trained to map **Rainfall** and **Temperature** data to one of five crop types: **Wheat**, **Rice**, **Maize**, **Barley**, and **Sugarcane**. The model utilizes **ReLU activation** for hidden layers and **Softmax** for multi-class classification, ensuring accurate predictions.

---

## Features 🌱
- **🌧 Rainfall (mm)**: Represents the amount of rainfall in a specific area. This determines how much water is available for crop growth.
- **🌡 Temperature (°C)**: Indicates the average temperature in the area, which influences which crops thrive in the given climate.

These two essential features are the **inputs** for the neural network, and the **output** is the predicted crop type, making it easier to choose the right crop for cultivation based on local environmental conditions.

---

## Key Concepts 🔑

### How Do **Rainfall (mm)** and **Temperature (°C)** Help Identify the Right Crop? 🤔

- **Rainfall (mm)**: 
  - The **amount of rainfall** in an area directly impacts the **water availability** for crops. 
  - Some crops need **higher rainfall** (e.g., **Rice**), while others thrive with **moderate** or **low rainfall** (e.g., **Wheat**, **Maize**).

- **Temperature (°C)**: 
  - The **average temperature** of the area influences crop growth and development. 
  - Crops like **Sugarcane** and **Rice** prefer **warmer temperatures**, while others like **Barley** and **Wheat** perform better in **cooler climates**.

By analyzing both **Rainfall** and **Temperature**, the neural network can accurately predict which crop is best suited for the given environment.

---

### Example Scenarios 🌾🌤:
- **Scenario 1**: If **Rainfall** is **high** and the **Temperature** is **warm**, crops such as **Rice** or **Sugarcane** are ideal.
- **Scenario 2**: If **Rainfall** is **moderate** and the **Temperature** is **cool**, **Wheat** or **Barley** would be better suited.

This intelligent prediction allows farmers to maximize yield based on local weather conditions.

---

### How the Model Works 🔍
1. **Input Layer**: The model receives **2 features**: **Rainfall (mm)** and **Temperature (°C)**.
2. **Hidden Layers**: 
   - These inputs are passed through **3 hidden layers**, each with **500 neurons**, and processed using the **ReLU activation** function.
3. **Output Layer**: 
   - The model predicts the probability of each crop class (Wheat, Rice, Maize, Barley, Sugarcane) using the **Softmax activation** function.
4. **Prediction**: The class with the **highest probability** is selected as the **predicted crop**.

---

## Model Architecture 🧠
- **Input Layer**: Takes in **2 features**: **Rainfall (mm)** and **Temperature (°C)**.
- **Hidden Layers**: Consists of **3 layers**, each with **500 neurons**.
- **Output Layer**: Contains **5 neurons**, each corresponding to one of the crop classes (Wheat, Rice, Maize, Barley, Sugarcane).

### Activation Functions 🔄
- **ReLU (Rectified Linear Unit)**: 
  - Introduces **non-linearity** in the hidden layers, enabling the model to capture complex patterns.
- **Softmax**: 
  - Applied in the output layer to predict the **probability distribution** over multiple classes.

### Loss Function ⚖️
- **Cross-entropy loss** is used to calculate the difference between the **predicted probabilities** and the **actual class labels**. This helps optimize the model during training.

---

## Performance Metrics 📊
The neural network’s performance is evaluated using key metrics:
- **Confusion Matrix**: Visualizes the model's classification results, showing the accuracy of the predictions for each class.
- **ROC Curve**: Helps assess the model's ability to discriminate between classes.
- **Classification Report**: Provides detailed performance metrics such as **precision**, **recall**, and **F1-score**.

These metrics give insights into how well the model is performing and allow for improvements to be made.

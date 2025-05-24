# 🐶🐱 Dog vs Cat Classifier

This project is a deep learning-based binary image classifier that distinguishes between dogs and cats. It uses **ResNet50** with **transfer learning**, **data augmentation**, and **hyperparameter optimization** via **Optuna**. The trained model is deployed using a lightweight **Flask web application**.

---

## 📦 Features

- ✅ Pretrained **ResNet50** with fine-tuning
- ✅ Advanced **data augmentation** using Keras
- ✅ Hyperparameter tuning with **Optuna**
- ✅ Saved in `.keras` format for portability
- ✅ Simple **Flask** app for browser-based prediction

---

## 📁 Dataset

- **Source**: [Kaggle - Dogs vs Cats](https://www.kaggle.com/datasets/salader/dogs-vs-cats)
- Downloaded and extracted automatically using Kaggle CLI.

---

## 🛠️ Training Pipeline

1. **Data Augmentation**:
   - Rotation, zoom, shifts, flips
   - Preprocessing with `ResNet50.preprocess_input`

2. **Transfer Learning**:
   - Base: ResNet50 (ImageNet weights)
   - Custom top layers with dense, dropout, batchnorm

3. **Hyperparameter Tuning**:
   - Dense units, dropout, learning rate, unfreeze layers, L2 regularization
   - 10 Optuna trials to find the best model

4. **Model Saving**:
   - Final model saved as `my_model.keras`

---

## 🚀 Deployment

### Flask App

A minimal Flask web server allows users to upload images and get predictions.

- Accepts image uploads via HTML form
- Preprocesses images and runs predictions
- Displays result and uploaded image in browser

---

## ▶️ How to Run

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/dog-vs-cat-classifier.git
cd dog-vs-cat-classifier

# Task 2 – Spam Classification Using Machine Learning

This directory contains **Task 2** of the **Syntexhub Internship Program**.  
The task focuses on building a **Spam Message Classification system** using Machine Learning techniques in Python.

The project demonstrates an end-to-end workflow starting from raw text data to a trained and saved classification model.

---

## 📌 Problem Statement

The objective of Task 2 is to classify text messages into:
- **Spam**
- **Ham (Not Spam)**

by applying text preprocessing, feature extraction, and machine learning classification techniques.

---

## 📊 Dataset Description

- **File Name:** `spam.csv`
- **Description:**  
  The dataset contains labeled SMS messages where each message is classified as either:
  - `spam`
  - `ham`

This dataset is used to train and evaluate the spam classification model.

---

## 📓 Notebook Overview

- **Notebook Name:** `spam_classifier.ipynb`

The notebook includes the following steps:

1. Importing required Python libraries  
2. Loading and inspecting the dataset  
3. Text preprocessing and cleaning  
4. Feature extraction using vectorization  
5. Training a machine learning classifier  
6. Evaluating the model performance  
7. Saving the trained model and vectorizer  

---

## 🧠 Machine Learning Workflow

### 🔹 Text Preprocessing
- Removal of unnecessary characters
- Text normalization
- Preparation of clean input for vectorization

### 🔹 Feature Extraction
- Text messages are converted into numerical form using a vectorizer

### 🔹 Model Training
- A classification algorithm is trained on the processed data
- The trained model learns to distinguish between spam and non-spam messages

---

## 💾 Saved Files

- **`model.pkl`**  
  Contains the trained machine learning model.

- **`vectorizer.pkl`**  
  Contains the fitted vectorizer used to transform text data.

These files can be reused for prediction without retraining the model.

---

## 🛠️ Tools & Technologies Used

- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  

---

## ▶️ How to Run Task 2

1. Navigate to the task folder:
   ```bash
   cd task2

 
```markdown
2. Open the notebook:

    ```bash
    jupyter notebook spam_classifier.ipynb
    ```

3. Run all cells sequentially to:
   - Train the model
   - Generate `model.pkl` and `vectorizer.pkl`


Saved Files

model.pkl – Trained spam classification model

vectorizer.pkl – Fitted text vectorizer

These files can be reused for prediction without retraining.



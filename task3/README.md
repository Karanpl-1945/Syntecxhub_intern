# Fraud Detection using Machine Learning

## Project Overview

This project focuses on detecting fraudulent credit card transactions using machine learning techniques.
Credit card fraud datasets are highly imbalanced, where fraudulent transactions represent only a very small portion of the data.

The goal of this project is to build models that can effectively identify fraudulent transactions while handling class imbalance using resampling techniques.

---

## Dataset

The dataset used in this project is the **Credit Card Fraud Detection dataset**.

It contains transactions made by credit cards where:

* **Class = 0 → Normal transaction**
* **Class = 1 → Fraud transaction**

Because the dataset is large (~143 MB), it is not included in this repository.

Dataset source:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

---

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

The dataset was explored to understand:

* Distribution of fraudulent vs non-fraudulent transactions
* Feature distributions
* Presence of outliers
* Data imbalance

Visualizations were created using:

* Matplotlib
* Seaborn
* Plotly

---

### 2. Data Preprocessing

Key preprocessing steps included:

* Handling class imbalance
* Feature scaling
* Train-test split
* Outlier analysis

---

### 3. Handling Class Imbalance

Since fraud cases are extremely rare, resampling techniques were used:

#### SMOTE (Synthetic Minority Oversampling Technique)

Creates synthetic examples of the minority class to balance the dataset.

#### Random Under Sampling

Reduces the number of majority class samples to balance the dataset.

---

### 4. Machine Learning Models

The following models were trained and evaluated:

1. Random Forest
2. XGBoost

Each model was trained using different sampling techniques.

---

### 5. Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* Confusion Matrix

Recall is particularly important in fraud detection because missing fraudulent transactions is costly.

---

## Project Structure

```
Syntecxhub_intern
│
└── task3
    │
    ├── task3.ipynb
    ├── README.md
```

Dataset file is excluded due to GitHub size limitations.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* XGBoost
* Imbalanced-learn

---

## Key Learnings

* Handling highly imbalanced datasets
* Applying resampling techniques
* Comparing multiple machine learning models
* Evaluating fraud detection systems using recall-focused metrics

---


Syntecxhub Internship Project


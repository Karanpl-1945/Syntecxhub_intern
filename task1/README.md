# House Price Prediction using Linear Regression and Model Selection

This project builds a **house price prediction model** using **linear regression (OLS)** in Python.  
The analysis focuses on **data preprocessing, log-transformation, feature engineering, interaction terms, and model selection using AIC and BIC**, followed by prediction and evaluation on test data.

---


## 📊 Dataset Description

The dataset consists of housing characteristics and amenities used to predict house prices.

### Target Variable
- **Price** – selling price of the house

### Key Features
- **Structural**: area, bedrooms, bathrooms, stories, parking  
- **Amenities**: air conditioning, basement, guest room, hot water heating  
- **Location**: main road access, preferred area  
- **Furnishing status**: furnished / semi-furnished / unfurnished  

---

##  Methodology

### 1️⃣ Data Preprocessing
- Categorical variables converted into dummy variables
- Continuous variables inspected for skewness
- Log transformations applied:
  - `log(price)`
  - `log(area)`
- Constant term added for regression intercept

---

### 2️⃣ Feature Engineering
The model includes:
- Core housing attributes
- Binary indicators for amenities
- Furnishing status indicators

Additionally, **interaction terms** are created to capture nonlinear relationships:
- `log(area) × preferred area`
- `log(area) × air conditioning`
- `bathrooms × bedrooms`

---

### 3️⃣ Model Estimation
Models are estimated using **Ordinary Least Squares (OLS)** via `statsmodels`.

Two models are compared:
- **Base Model** – main effects only
- **Interaction Model** – includes interaction terms

---

### 4️⃣ Model Selection (AIC & BIC)
- **AIC (Akaike Information Criterion)**
- **BIC (Bayesian Information Criterion)**

Lower values indicate better trade-off between fit and complexity.  
The **final model is chosen based on minimum AIC**.

---

### 5️⃣ Prediction Pipeline
- Test data is processed using the **same transformations as training data**
- No data leakage or re-fitting on test data
- Predictions are generated on the **log scale**
- Predictions are transformed back using `exp()`
- **Bias-corrected predictions** are also computed

---

### 6️⃣ Model Evaluation
Performance is evaluated using:
- **RMSE (Root Mean Squared Error)**
- **R² score**

Results are compared between:
- Naive back-transformation
- Bias-corrected predictions

---

## 📈 Key Results & Insights

- Log transformation improves model stability
- Interaction terms significantly improve model fit
- AIC/BIC provide principled model comparison
- Bias correction improves prediction accuracy on the original scale
- The final selected model generalizes well to test data

---

## 🛠️ Libraries & Tools Used

- Python 3
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scikit-learn`
- Jupyter Notebook

---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/USERNAME/REPO_NAME.git

# Credit-Risk-Modeling

This repository contains the source code and documentation for a **Credit Risk Modeling** system. The project aims to reliably detect and forecast loan repayment defaulters using machine learning and deep learning techniques. It provides a scorecard system and a user interface to predict whether an applicant is likely to repay a loan.

## 📌 Project Overview

The primary goal of this project is to help financial institutions minimize risk by identifying potential defaulters early in the verification process. We evaluate multiple algorithms to determine the most effective model for predicting credit default based on historical data.

### 🚀 Key Features

* **Exploratory Data Analysis (EDA):** Data cleaning (handling null values) and visualization to understand feature significance.
* **Machine Learning & Deep Learning Models:** Implementation of various algorithms including Logistic Regression, Random Forest, and LSTM.
* **GUI Interface:** A user-friendly interface built with **Tkinter** that allows users to input applicant details and get instant repayment predictions.
* **Scorecard Development:** Systematic calculation of risk to indicate loan repayment probability.

## 🛠️ Technical Stack

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy 
* **Machine Learning:** Scikit-Learn 
* **Deep Learning:** Keras, TensorFlow 
* **Visualization:** Matplotlib, Seaborn 
* **GUI:** Tkinter 


## 📊 Dataset

The project utilizes the **"Give Me Some Credit"** dataset.
**Key data fields include:**

* `RevolvingUtilizationOfUnsecuredLines`
* `Age`
* `DebtRatio`
* `MonthlyIncome`
* `NumberOfOpenCreditLinesAndLoans`
* `NumberOfTimes90DaysLate`
* `NumberOfDependents`.



## 📈 Results and Performance

We evaluated several models based on their accuracy in predicting defaulters:

| Model | Accuracy |
| --- | --- |
| **LSTM (Long Short-Term Memory)** | **93.4%** |
| **MLP (Multi-Layer Perceptron)** | **93.2%** |
| **Gradient Boosting** | **92.9%** |
| **Random Forest** | **92.7%** |
| **Logistic Regression** | **92.5%** |
| **K-Neighbors Classification** | **92.0%** |

The **LSTM** algorithm achieved the highest accuracy of approximately **93.5%**.

## 💻 Installation and Usage

1. **Clone the repository:**
```bash
git clone https://github.com/deekshitha-k/credit-risk-modeling.git

```


2. **Install dependencies:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn keras tensorflow

```


3. **Run the Analysis:**
Open and execute the `ML_Project.ipynb` notebook to see data preprocessing and model training.
4. **Launch the GUI:**
Run the project script (e.g., `python main.py`) to open the Tkinter interface for real-time predictions.



## 👥 Contributors

* **Revu Mythili** (20WH1A0556) 
* **Kashetty Deekshitha** (20WH1A0557) 
* **Katta Komali** (20WH1A0558) 
* **Bukka Godishela Sahithi** (20WH1A0559) 
* **Sai Laxmi Rishita Alluri** (20WH1A0560) 
* **Project Guide:** Ms. S. Vidyullatha (Assistant Professor, BVRIT HYDERABAD) 



## 📜 Acknowledgments

Developed at **BVRIT HYDERABAD College of Engineering for Women** as part of the Bachelor of Technology in Computer Science & Engineering (2023-2024).

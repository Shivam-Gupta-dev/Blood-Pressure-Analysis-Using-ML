# 🩺 Hypertension Prediction System

## 📌 Overview

The **Hypertension Prediction System** is a machine learning–based healthcare project designed to **predict and classify different stages of hypertension (high blood pressure)** using patient clinical data and lifestyle factors.

The system analyzes health parameters such as blood pressure readings, age, symptoms, medical history, and lifestyle habits to determine the **risk level and stage of hypertension**. It also provides **basic lifestyle recommendations** to help users monitor and manage their health.

This project demonstrates the use of **supervised machine learning algorithms, data preprocessing, feature selection, model evaluation, and prediction pipelines** to build a practical healthcare decision-support tool.

⚠️ **Disclaimer:**  
This system is intended **only for educational and decision-support purposes** and should **not be used as a substitute for professional medical diagnosis.**

---

# 🎯 Project Objectives

The main objectives of this project are:

- Predict the **stage of hypertension** using patient health data
- Apply **machine learning classification algorithms**
- Perform **data preprocessing and feature selection**
- Evaluate model performance using standard metrics
- Provide **risk predictions and recommendations**
- Build a **user-friendly interface** for prediction

---

# 🧠 Machine Learning Workflow

The system follows a standard **machine learning pipeline**:

### 1. Data Collection

Hypertension dataset containing:

- Blood pressure readings
- Age
- Symptoms
- Medication status
- Lifestyle habits
- Medical history

### 2. Data Preprocessing

- Handling missing values
- Encoding categorical variables
- Feature normalization
- Data cleaning

### 3. Exploratory Data Analysis (EDA)

- Distribution analysis
- Correlation analysis
- Pattern identification related to hypertension

### 4. Feature Selection

Selecting the most relevant features that contribute to hypertension prediction.

### 5. Dataset Splitting

- Training dataset
- Testing dataset

### 6. Model Training

Supervised machine learning models used:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### 7. Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### 8. Model Selection

The best-performing model is selected based on evaluation results.

### 9. Prediction Pipeline

The pipeline accepts **new patient input data** and returns:

- Hypertension stage classification
- Risk score

### 10. Recommendation Module

Provides **basic health and lifestyle recommendations** based on prediction results.

---

# ⚙️ Tech Stack

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

### Tools

- Jupyter Notebook / Python Scripts
- Git & GitHub

### Interface

- Simple user interface for patient data input and prediction results

---

# 📂 Project Structure

\`\`\`text
Blood-Pressure-Analysis-Using-ML/
│
├── Milestone 1 - Data*Collection*&\_Preparation/
│ ├── patient_data.csv
│ └── categorical-encoding.ipynb
│
├── Milestone 2 - EDA/
│ └── visual-analysis.ipynb
│
├── Milestone 3 - Model_Building/
│ └── models.ipynb
│
├── model/
│ └── hypertension_model.pkl # Trained ML model
│
├── static/
│ └── style.css # Frontend styling
│
├── templates/
│ ├── index.html # Input form
│ └── result.html # Prediction output
│
├── app.py # Main Flask application
└── README.md
\`\`\`

---

# 🚀 Installation & Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/hypertension-prediction.git
cd hypertension-prediction
\`\`\`

### 2. Create and Activate a Virtual Environment

**Windows:**
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`
**Linux / Mac:**
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install Dependencies

Ensure you have the required Python libraries installed:
\`\`\`bash
pip install Flask joblib numpy pandas scikit-learn matplotlib seaborn
\`\`\`

---

# ▶️ Running the Project

### 1. (Optional) Re-train the Model

If you need to re-train the model or generate a new `.pkl` file, open `Milestone 3 - Model_Building/models.ipynb` in Jupyter or VS Code, run all cells, and ensure the save script at the bottom executes successfully.

### 2. Start the Web Server

Run the Flask application from the root directory:
\`\`\`bash
python app.py
\`\`\`

### 3. View the App

Open your web browser and navigate to:
**http://127.0.0.1:5000**

Enter the patient details in the interface to receive the Hypertension stage prediction!

---

# 🤝 Contributors

Project developed by:

- Shivam Gupta
- Shourya Panchariya
- Shlok Shinde
- Shivam Vishwakarma

---

# 📜 License

This project is open-source and available under the **MIT License**.

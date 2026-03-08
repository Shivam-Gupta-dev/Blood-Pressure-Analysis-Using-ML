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

```
Hypertension-Prediction/
│
├── data/
│   └── hypertension_dataset.csv
│
├── notebooks/
│   └── EDA_analysis.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── prediction_pipeline.py
│   └── recommendation_system.py
│
├── ui/
│   └── app_interface.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hypertension-prediction.git
cd hypertension-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Train the Model

```bash
python train_model.py
```

### Run Prediction System

```bash
python app_interface.py
```

Enter patient details in the interface to receive:

- Hypertension stage prediction  
- Risk score  
- Health recommendations  

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

These metrics help determine the most reliable model for hypertension stage classification.

---

# 🧪 Use Cases

This system can be used in:

- Preventive health screening  
- Hypertension risk monitoring  
- Clinical decision support systems  
- Patient awareness tools  
- Healthcare data analysis  

---

# 🔮 Future Improvements

Possible enhancements include:

- Deep learning models for improved accuracy  
- Integration with wearable health devices  
- Real-time patient monitoring  
- Mobile application interface  
- Cloud deployment  
- Integration with hospital systems  

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

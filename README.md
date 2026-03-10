<div align="center">

# 🩺 Hypertension Prediction System using Machine Learning

**An end-to-end AI healthcare tool that predicts and classifies hypertension stages based on clinical data and lifestyle factors.**

</div>

---

# 📌 Project Overview

The **Hypertension Prediction System** is a machine learning-based healthcare application designed to evaluate patient health parameters and predict their risk of high blood pressure.

By analyzing a combination of **vital signs, medical history, and lifestyle factors**, the system categorizes the patient's condition into specific stages:

* Normal
* Hypertension Stage-1
* Hypertension Stage-2
* Hypertensive Crisis

The project demonstrates a **complete machine learning pipeline** including:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Model training and evaluation
* Deployment using Flask

⚠️ **Disclaimer:** This project is built for **educational and clinical decision-support purposes only**. It is not a substitute for professional medical diagnosis.

---

# 📊 Dataset & Features

The dataset contains multiple **clinical and lifestyle attributes** used to predict hypertension.

### Core Features

**Vital Signs**

* Systolic Blood Pressure
* Diastolic Blood Pressure

**Demographics**

* Age Group
* Gender

**Medical History**

* Past medical history
* Patient status
* Medication usage

**Symptoms**

* Severity of condition
* Shortness of breath
* Visual changes
* Nosebleeds

**Lifestyle**

* Diet control
* Duration since initial diagnosis

---

# 🧠 Methodology & Machine Learning Pipeline

The project development was divided into three milestones.

---

## Milestone 1: Data Collection & Preparation

The raw dataset (`patient_data.csv`) contained categorical and numerical data requiring preprocessing.

Steps performed:

* Handling missing values
* Data normalization
* Encoding categorical features

Categorical variables such as **Yes/No values and symptom severity** were converted into machine-readable numerical formats.

Final processed dataset:

```
encoded.csv
```

---

## Milestone 2: Exploratory Data Analysis (EDA)

EDA was conducted to uncover patterns and relationships between features.

Using **Matplotlib and Seaborn**, we analyzed:

* Feature distributions
* Correlations between symptoms and blood pressure
* Impact of lifestyle factors on hypertension risk

This helped identify the **most influential predictors**.

---

## Milestone 3: Model Building & Evaluation

Multiple supervised machine learning models were trained using an **80/20 train-test split**.

### Model Performance

| Model                  | Accuracy |
| ---------------------- | -------- |
| Random Forest          | 100%     |
| Support Vector Machine | 100%     |
| Decision Tree          | 100%     |
| K-Nearest Neighbors    | 98.1%    |
| Logistic Regression    | 95.1%    |
| Ridge Classifier       | 90.0%    |
| Naive Bayes            | 84.4%    |

The **Random Forest model** was selected for deployment because it:

* Handles non-linear data well
* Reduces overfitting
* Provides strong predictive performance

The trained model was serialized as:

```
hypertension_model.pkl
```

---

# 💻 Web Deployment (Flask)

The application is deployed using a **Flask web framework**.

Workflow:

1. User enters health parameters via a web form.
2. The backend preprocesses the inputs.
3. Data is passed to the trained ML model.
4. The model predicts the hypertension stage.
5. The result is displayed on the result page.

This allows **real-time predictions through a simple web interface**.

---

# ⚙️ Tech Stack

**Programming Language**

* Python

**Machine Learning & Data Science**

* Scikit-learn
* Pandas
* NumPy

**Data Visualization**

* Matplotlib
* Seaborn

**Backend**

* Flask

**Frontend**

* HTML5
* CSS3

**Development Tools**

* Jupyter Notebook
* Git
* VS Code

---

# 🚀 Installation & Setup Guide

Follow these steps to run the project locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/shivam-gupta-dev/blood-pressure-analysis-using-ml.git
cd blood-pressure-analysis-using-ml
```

---

## 2️⃣ Create a Virtual Environment

It is recommended to isolate project dependencies.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install Flask joblib numpy pandas scikit-learn matplotlib seaborn
```

---

# ▶️ Running the Application

After completing the setup:

Ensure you are inside the project directory.

Run the Flask application:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

Fill in the clinical details and click **Predict** to get the hypertension stage classification.

---

# 📂 Project Structure

```
Blood-Pressure-Analysis-Using-ML/
│
├── Milestone 1 - Data_Collection_&_Preparation/
│   ├── patient_data.csv
│   ├── encoded.csv
│   └── categorical-encoding.ipynb
│
├── Milestone 2 - EDA/
│   └── visual-analysis.ipynb
│
├── Milestone 3 - Model_Building/
│   └── models.ipynb
│
├── model/
│   └── hypertension_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
└── README.md
```

---

# 🤝 Contributors

* Shivam Gupta
* Shourya Panchariya
* Shlok Shinde
* Shivam Vishwakarma

---

# 📜 License

This project is open-source and available under the **MIT License**.

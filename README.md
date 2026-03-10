<div align="center">
  <h1>🩺 Hypertension Prediction System using Machine Learning</h1>
  <p><b>An end-to-end AI healthcare tool that predicts and classifies hypertension stages based on clinical data and lifestyle factors.</b></p>
</div>

---

## 📌 Project Overview
The **Hypertension Prediction System** is a machine learning-based healthcare application designed to evaluate patient health parameters and predict their risk of high blood pressure. By analyzing a combination of vital signs, medical history, and physical symptoms, the system categorizes the patient's condition into specific stages (Normal, Hypertension Stage-1, Hypertension Stage-2, or Hypertensive Crisis).

The project features a full data science pipeline, from exploratory visual analysis to algorithm training, capped off with a user-friendly Flask web interface for real-time predictions.

> ⚠️ **Disclaimer:** This system is built for **educational and clinical decision-support purposes only**. It is not a substitute for professional medical diagnosis or treatment.

---

## 📊 Dataset & Features
The model is trained on clinical data encompassing various physiological and lifestyle factors. The core features evaluated by the system include:
* **Vital Signs:** Systolic and Diastolic Blood Pressure.
* **Demographics:** Age group and Gender.
* **Medical History:** Past medical history, current patient status, and medication usage.
* **Symptoms:** Severity of condition, shortness of breath, visual changes, and nosebleeds.
* **Lifestyle:** Diet control and duration since initial diagnosis.

---

## 🧠 Methodology & Machine Learning Pipeline

The project development was structured into three major milestones:

### Milestone 1: Data Collection & Preparation
The raw dataset (`patient_data.csv`) contained categorical and numerical data that required extensive cleaning. We handled missing values, normalized the data, and performed categorical encoding to convert textual data (like "Yes"/"No" and symptom severity) into machine-readable numeric formats, resulting in our finalized `encoded.csv` dataset.

### Milestone 2: Exploratory Data Analysis (EDA)
Extensive visual analysis was conducted to uncover hidden patterns within the patient data. Using libraries like Seaborn and Matplotlib, we mapped out feature distributions, identified correlations between specific symptoms (like shortness of breath) and blood pressure spikes, and determined which features heavily influenced the target variable.

### Milestone 3: Model Building & Evaluation
We trained and evaluated multiple supervised machine learning algorithms using an 80/20 train-test split. The performance metrics (Accuracy) are as follows:
* **Random Forest Classifier:** 100% 
* **Support Vector Machine (SVM):** 100%
* **Decision Tree:** 100%
* **K-Nearest Neighbors (KNN):** 98.1%
* **Logistic Regression:** 95.1%
* **Ridge Classifier:** 90.0%
* **Naive Bayes:** 84.4%

Because of its robust capability to handle non-linear data and prevent overfitting, the **Random Forest** model was serialized (`hypertension_model.pkl`) and selected for the final deployment.

---

## 💻 Web Deployment (Flask)
The user interface is powered by a Flask backend (`app.py`). When a user submits their details via the HTML form, the backend dynamically scales and encodes the inputs to match the exact format the Random Forest model expects. It then feeds the data to the `.pkl` model and renders the predicted hypertension stage back to the user on a dedicated results page.

---

## ⚙️ Tech Stack
* **Programming Language:** Python
* **Machine Learning & Data Science:** Scikit-learn, Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3
* **Tools:** Jupyter Notebook, Git, VS Code

---

## 🚀 Installation & Setup Guide

Follow these instructions to clone the repository and run the application on your local machine.

### 1. Clone the Repository
Open your terminal and run:
```bash
git clone [https://github.com/shivam-gupta-dev/blood-pressure-analysis-using-ml.git](https://github.com/shivam-gupta-dev/blood-pressure-analysis-using-ml.git)
cd blood-pressure-analysis-using-ml

2. Create a Virtual Environment
It is highly recommended to isolate your project dependencies.

For Windows:

Bash
python -m venv venv
venv\Scripts\activate
For macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all the required Python libraries using pip:

Bash
pip install Flask joblib numpy pandas scikit-learn matplotlib seaborn
▶️ Running the Application
Once the setup is complete, you can launch the prediction system.

Ensure you are in the root directory (blood-pressure-analysis-using-ml).

Start the Flask server by running:

Bash
python app.py
Open your web browser and navigate to:
👉 http://127.0.0.1:5000

Enter the required clinical details in the form and click "Predict" to receive the hypertension stage classification!

📂 Project Structure
Plaintext
Blood-Pressure-Analysis-Using-ML/
│
├── Milestone 1 - Data_Collection_&_Preparation/
│   ├── patient_data.csv               # Raw dataset
│   ├── encoded.csv                    # Cleaned & encoded dataset
│   └── categorical-encoding.ipynb     # Preprocessing scripts
│
├── Milestone 2 - EDA/
│   └── visual-analysis.ipynb          # Exploratory Data Analysis & charts
│
├── Milestone 3 - Model_Building/
│   └── models.ipynb                   # Algorithm training & evaluation
│
├── model/
│   └── hypertension_model.pkl         # Serialized Random Forest model
│
├── static/
│   └── style.css                      # UI styling
│
├── templates/
│   ├── index.html                     # Input form page
│   └── result.html                    # Output prediction page
│
├── app.py                             # Main Flask application
└── README.md
🤝 Contributors
Shivam Gupta

Shourya Panchariya

Shlok Shinde

Shivam Vishwakarma

📜 License
This project is open-source and available under the MIT License.
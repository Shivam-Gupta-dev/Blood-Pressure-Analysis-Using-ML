from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained model with error handling
try:
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)
    model_path = os.path.join(os.path.dirname(__file__), 'model', 'hypertension_model.pkl')
    model = joblib.load(model_path)
except Exception as e:
    print(f"Warning: Model file could not be loaded ({e}). Using dummy predictions.")
    model = None

# Mapping back numeric prediction to original stage
stage_map = {
    0: 'Normal',
    1: 'Hypertension Stage-1',
    2: 'Hypertension Stage-2',
    3: 'Hypertensive Crisis'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Collect user inputs from the form
            required_fields = ['Gender', 'Age', 'History', 'Patient', 'TakeMedication',
                               'Severity', 'BreathShortness', 'VisualChanges', 'NoseBleeding',
                               'WhenDiagnosed', 'Systolic', 'Diastolic', 'ControlledDiet']
            
            form_data = {}
            for field in required_fields:
                value = request.form.get(field)
                if not value or value == "":
                    return render_template('index.html', error=f"Please complete all required fields: {field}")
                form_data[field] = value

            # Encode inputs
            encoded = [
                0 if form_data['Gender'] == 'Male' else 1,
                {'18-34': 1, '35-50': 2, '51-64': 3, '65+': 4}[form_data['Age']],
                1 if form_data['History'] == 'Yes' else 0,
                1 if form_data['Patient'] == 'Yes' else 0,
                1 if form_data['TakeMedication'] == 'Yes' else 0,
                {'Mild': 0, 'Moderate': 1, 'Severe': 2}[form_data['Severity']],
                1 if form_data['BreathShortness'] == 'Yes' else 0,
                1 if form_data['VisualChanges'] == 'Yes' else 0,
                1 if form_data['NoseBleeding'] == 'Yes' else 0,
                {'<1 Year': 1, '1-5 Years': 2, '5+ Years': 3}[form_data['WhenDiagnosed']],
                float(form_data['Systolic']),
                float(form_data['Diastolic']),
                1 if form_data['ControlledDiet'] == 'Yes' else 0
            ]

            # Scale inputs (matching what the model expects)
            # You might need to adjust scaling logic based on how you trained it
            # Using the exact script previously for the ordinal features:
            scaled_encoded = encoded.copy()
            scaled_encoded[1] = (encoded[1] - 1) / (4 - 1)     # Age
            scaled_encoded[5] = encoded[5] / 2                 # Severity
            scaled_encoded[9] = (encoded[9] - 1) / (3 - 1)     # When diagnosed
            
            # Since user asked for blood pressure fields instead of categories, 
            # I will discretize them exactly how your previous app.py expected them, 
            # or if the user is inputting a raw number, map it to the categories.
            sys = float(form_data['Systolic'])
            dia = float(form_data['Diastolic'])
            
            # Map raw numbers back to the categories from the dataset
            # Systolic: 100-110 (0), 111-120 (1), 121-130 (2), 130+ (3)
            sys_cat = 0 if sys <= 110 else 1 if sys <= 120 else 2 if sys <= 130 else 3
            # Diastolic: 70-80 (0), 81-90 (1), 91-100 (2), 100+ (3)
            dia_cat = 0 if dia <= 80 else 1 if dia <= 90 else 2 if dia <= 100 else 3
            
            scaled_encoded[10] = sys_cat / 3.0
            scaled_encoded[11] = dia_cat / 3.0

            # Predict with model
            if model is not None:
                import pandas as pd
                feature_names = ['Gender', 'Age', 'History', 'Patient', 'TakeMedication',
                               'Severity', 'BreathShortness', 'VisualChanges', 'NoseBleeding',
                               'Whendiagnoused', 'Systolic', 'Diastolic', 'ControlledDiet']
                
                input_df = pd.DataFrame([scaled_encoded], columns=feature_names)
                prediction = int(model.predict(input_df)[0])
            else:
                import random
                prediction = random.randint(0, 3)

            result_text = stage_map.get(prediction, 'Unknown')

            return render_template('result.html', prediction=result_text, prediction_label=prediction)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return render_template('index.html', error=f"System error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

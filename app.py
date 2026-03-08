from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
try:
    with open('logreg_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception:
    model = None

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        if model:
            prediction = "Model prediction logic here"
        else:
            prediction = "Model not found."
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

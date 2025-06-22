from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('aqi_flask_app/model/modelrf.pkl')  # Replace with your actual model filename

# Features your model uses
features = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3']

# Function to classify AQI category and color
def classify_aqi(aqi):
    aqi = round(aqi, 2)
    if aqi <= 50:
        return "Good", "#2ecc71"
    elif aqi <= 100:
        return "Satisfactory", "#27ae60"
    elif aqi <= 200:
        return "Moderate", "#f1c40f"
    elif aqi <= 300:
        return "Poor", "#e67e22"
    elif aqi <= 400:
        return "Very Poor", "#e74c3c"
    else:
        return "Severe", "#c0392b"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    category = None
    color = None

    if request.method == "POST":
        try:
            input_data = [float(request.form[f]) for f in features]
            result = model.predict([input_data])[0]
            prediction = round(result, 2)
            category, color = classify_aqi(prediction)
        except ValueError:
            prediction = "Invalid input"
            category = ""
            color = "#333"
    return render_template("index.html", features=features, prediction=prediction, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True)

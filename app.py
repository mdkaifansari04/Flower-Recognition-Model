from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd
app = Flask(__name__)

# Load trained model
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

model = joblib.load("iris_model.pkl")
encoder = LabelEncoder()
encoder.fit(df['species'])
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Get input data
    features = np.array(data["features"]).reshape(1, -1)
    print("feature : ", features)# Convert to NumPy array
    
    prediction = model.predict(features)
    return jsonify({"prediction": encoder.inverse_transform(prediction)[0]})


@app.route('/')
def method_name():
    return jsonify({"message": "Server is up and running "})

if __name__ == "__main__":
    app.run(debug=True)

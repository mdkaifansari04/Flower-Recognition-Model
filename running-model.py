import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

encoder = LabelEncoder()
encoder.fit(df['species']) 

loaded_model = joblib.load("iris_model.pkl")

# Making a new prediction
new_data = [[5.5, 2.5, 1.9, 1.2]]
prediction = loaded_model.predict(new_data)

print(f"Predicted class: {encoder.inverse_transform(prediction)[0]}")
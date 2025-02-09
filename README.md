# Flask API - Model Prediction Service

This is a Flask-based API that serves a machine learning model for making predictions. It includes sample Python scripts for learning purposes.

## 📌 Features

- **Predict API**: Send input features and get predictions.
- **Pre-trained Model**: Uses a machine learning model for classification.
- **RESTful API**: Built with Flask and supports JSON requests.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```sh
git clone git@github.com:mdkaifansari04/Flower-Recognition-Model.git
cd Flower-Recognition-Model
```

### 2️⃣ Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```sh
python app.py
```

The server will start at: `http://127.0.0.1:5000/`

---

## 📡 API Endpoints

### 🔹 Health Check

**URL:** `GET /`

```sh
curl http://127.0.0.1:5000/
```

📌 **Response:**

```json
{ "message": "Server is up and running" }
```

### 🔹 Prediction API

**URL:** `POST /predict`

#### Request Format:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

#### Sample Request (cURL):

```sh
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

#### Sample Response:

```json
{ "prediction": "Iris-setosa" }
```

---

## 📤 Deployment

To deploy the Flask API, use any cloud provider like **Render, Heroku, AWS, or DigitalOcean**.

For example, deploying on **Render**:

1. Push the code to GitHub.
2. Connect GitHub to Render.
3. Select **Flask** as the runtime.
4. Add **Start Command:** `python app.py`.

---

## 🛠 Troubleshooting

- If the model is missing, make sure `iris_model.pkl` is in the root directory.
- If dependencies fail, run: `pip install -r requirements.txt --no-cache-dir`
- If port conflicts occur, change the port in `app.py`.

---

## 👨‍💻 Author

Developed by **Md Kaif Ansari** 🚀

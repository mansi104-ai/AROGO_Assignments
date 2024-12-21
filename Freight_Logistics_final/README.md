# Freight Logistics - Predicting Shipment Delays

Predicting shipment delays in freight logistics is crucial for maintaining supply chain efficiency. This project builds an AI model to forecast delays based on historical data and deploys the model via an API for practical use.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Dataset Overview](#dataset-overview)
- [Project Structure](#project-structure)
- [Project Workflow](#project-workflow)
- [Technologies Used](#technologies-used)
- [How to Run the Project](#how-to-run-the-project)
  - [Setup Instructions](#setup-instructions)
  - [Using the API](#using-the-api)
- [Example API Request and Response](#example-api-request-and-response)
- [Project Structure](#project-structure)

---

## Problem Statement

Freight logistics often suffer from delays due to unpredictable factors like traffic, weather, and operational inefficiencies.  
**Objective:** Build a machine learning model that predicts whether a shipment will be delayed or delivered on time.

---

## Dataset Overview

The dataset contains the following features:

- **Shipment ID**: Unique identifier for each shipment.
- **Origin and Destination**: Indian cities where the shipment starts and ends.
- **Shipment Date**: The date the shipment was dispatched.
- **Vehicle Type**: Type of vehicle used (Truck, Lorry, Container, Trailer).
- **Distance (km)**: Distance between origin and destination.
- **Weather Conditions**: Weather at the time of shipment (Clear, Rain, Fog).
- **Traffic Conditions**: Traffic level during shipment (Light, Moderate, Heavy).
- **Delay**: The target variable indicating delay (Yes/No).

---

## Project Structure

Freight_Logistics/ </br>
│</br>
├── api/  </br>
│ ├── app.py  # FastAPI application  </br>
│ ├── predict.html   # Frontend HTML file  </br>
│ ├── styles.css   # Frontend styling  </br>
│  </br>
├── data/ </br>
│ ├── raw/   # Contains raw dataset  </br>
│ ├── processed/   # Contains processed dataset</br>
│</br>
├── models/</br>
│ ├── model.pkl   # Saved best-performing ML model</br>
│ ├── scaler.pkl   # Scaler for preprocessing</br>
│</br>
├── notebooks/</br>
│ ├── eda.ipynb   # EDA and feature selection </br>
│ ├── preprocessing.ipynb   # Data preprocessing notebook</br>
│ ├── model.ipynb   # Model training and evaluation</br>
│</br>
├── results/</br>
│ └── *.png   # EDA and result visualizations</br>
│</br>
├── .gitignore</br>
├── README.md   # Project documentation</br>
└── requirements.txt   # Python dependencies</br>

## Project Workflow

### 1. **Data Preparation**
   - Clean and preprocess the raw dataset.
   - Encode categorical variables.
   - Handle missing values and outliers.

### 2. **Exploratory Data Analysis (EDA)**
   - Identify trends and correlations using visualizations.
   - Select features contributing to shipment delays.

### 3. **Model Development**
   - Train and evaluate multiple machine learning models:
     - Logistic Regression
     - Decision Tree
     - Random Forest
   - Select the best model based on evaluation metrics.

### 4. **Deployment**
   - Save the best model as `model.pkl`.
   - Build an API using FastAPI to accept shipment data and return predictions.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn, FastAPI
- **Deployment**: FastAPI for API development and Uvicorn for server hosting

---

## How to Run the Project

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/freight-logistics.git
   cd freight-logistics
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv freight_env
   source freight_env/bin/activate  
   ### On Windows: freight_env\Scripts\activate
   ```

3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Data**

-1. Place the raw dataset in `data/raw/`.
-2. Run `notebooks/preprocessing.ipynb` to process and save the dataset in `data/processed/`.

5. **Train the Model**

Run `notebooks/model.ipynb` to train the model and save the best-performing model as `model.pkl`.

6. **Start the API**
   ```bash
   uvicorn api.app:app --reload

   ```

7. **Test the API**

Open a browser and visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

## Using the API

Access the API at [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict).

## Use the following JSON payload for predictions:

{
"distance_km": 120.5,
"planned_delivery_days": 5,
"actual_delivery_days": 7,
"weather_conditions": 1,
"traffic_conditions": 2,
"is_long_distance": 1,
"is_bad_weather": 0,
"is_heavy_traffic": 1
}


The API returns a prediction as:

{
"prediction": "Delayed"
}


## Example API Request and Response

**Endpoint:** `/predict`

### Request

{</br>
"distance_km": 450,</br>
"planned_delivery_days": 5,</br>
"actual_delivery_days": 6,</br>
"weather_conditions": 0,</br>
"traffic_conditions": 2,</br>
"is_long_distance": 1,</br>
"is_bad_weather": 0,</br>
"is_heavy_traffic": 1</br>
}</br>


### Response

{</br>
"prediction": "On-Time"</br>
}</br>



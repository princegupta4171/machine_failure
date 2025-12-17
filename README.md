# Machine Failure Prediction

A Streamlit web application that predicts machine failure using sensor data.

## Features

- Real-time machine health prediction
- Interactive UI with animated gradient background
- Input validation for sensor readings
- Visual alerts for failure predictions

## Installation

```bash
pip install streamlit numpy
```

## Usage

```bash
streamlit run app.py
```

## Input Parameters

- Temperature (°C)
- Vibration
- Pressure
- RPM

## Model

The application uses a pre-trained machine learning model (`machinefailure.pkl`) to predict machine failure based on sensor inputs.

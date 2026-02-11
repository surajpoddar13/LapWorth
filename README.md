# LapWorth – Laptop Price Prediction
Live: https://lapworth.streamlit.app

## Overview

LapWorth is a machine learning application that predicts laptop prices based on hardware specifications and product attributes. The project demonstrates an end-to-end workflow including data preprocessing, feature engineering, model training, and deployment through an interactive Streamlit interface.

## Features

* End-to-end scikit-learn pipeline
* Feature engineering with categorical encoding
* Linear Regression model for price estimation
* Interactive web interface using Streamlit
* Cloud deployment ready

## Tech Stack

* Python
* scikit-learn
* pandas
* NumPy
* Streamlit

## Project Structure

```
LapWorth/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Traning.ipynb
└── README.md
```

## Installation

```
git clone https://github.com/surajpoddar13/LapWorth.git
cd LapWorth
pip install -r requirements.txt
```

## Run Locally

```
streamlit run app.py
```

## Deployment

The application is deployed using Streamlit Community Cloud and can be adapted for Hugging Face Spaces or other cloud platforms.

## Author

Suraj Poddar

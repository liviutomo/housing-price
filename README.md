# Housing Price Prediction
This repository contains code and resources for predicting housing prices using machine learning techniques.

## Overview
The goal of this project is to develop a machine learning model that can accurately predict housing prices based on various features such as square footage, number of bedrooms, location, etc. We explore different machine learning algorithms and techniques to build and evaluate predictive models.

## Dataset
The dataset used in this project is available in the data directory. It includes features such as square footage, number of bedrooms, number of bathrooms, and the target variable, sale price.

## Files
data/: Contains the dataset files - already split in train and test 
models/: Saved trained models.
Python scripts: Scripts for data preprocessing, model training, and evaluation.
requirements.txt: Python dependencies required to run the code.

## Usage

Clone the repository:
cmd: 'git clone https://github.com/liviutomo/housing-price.git'

Install the required dependencies:

'pip install -r requirements.txt'

For local execution, set the tracking URI from run.py to 'http://127.0.0.1:5000/' and run the following command in bash 'mlflow server --host 127.0.0.1 --port 5000'

The current state of the project is not very generic - you will have to adapt it with your AWS credentials and parameters.

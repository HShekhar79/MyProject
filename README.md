AI Threat Hunter
What This Project Does
AI Threat Hunter is a machine learning tool that detects network attacks and anomalies using advanced data science. It automatically preprocesses large, real-world network data, trains a predictive model, and evaluates new network flows to identify threats in real-time.

Supports CIC-IDS2017 attack dataset

Batch and single network flow predictions

Automated feature engineering and model training

Performance reporting with visualizations

Setup Instructions
Install Python (3.8 or higher).

Clone/download this project folder to your machine.

Install dependencies (run in terminal from project root):

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" -m pip install pandas scikit-learn matplotlib seaborn joblib
Organize the files:

Raw network data in data/raw/

Processed and cleaned files will be auto-saved in data/processed/

Model and result files will be auto-saved in models/ and data/

How To Run Each Script (with Example Commands)
Preprocess Raw Data

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" data/preprocess.py
Clean and Engineer Features

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" data/clean_and_engineer.py
Train The Model

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" src/train_model.py
Single Flow Prediction

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" src/predict.py
Batch Prediction (use your data/new_network_flows.csv as input)

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" src/batch_predict.py
Performance Report

powershell
& "C:/Users/Himanshu Shekhar/AppData/Local/Python/pythoncore-3.14-64/python.exe" src/performance_report.py
Screenshots of Results and Plots
Confusion Matrix Example
Batch Prediction Example
Flow Duration	Total Fwd Packets	Total Backward Packets	...	Predicted_Label
1000	50	50	...	BENIGN
900	40	45	...	BENIGN
Add more screenshots of your CLI output or plots here for variety!
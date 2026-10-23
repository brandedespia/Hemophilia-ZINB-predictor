# Hemophilia-ZINB-predictor
## Overview
A interactive Streamlit web application based on the Zero-Inflated Negative Binomial(ZINB) model that predict the mortality risk for Hemophilia.

## Work Contribution
The ZINB model is built by my final year project group
- **Group Contribution** : Data preprocessing, R-based models training, statistical analysis (see `Code_Finalized.R`).
- **My Individual Contribution** : Rewrite the ZINB model prediction logic by Python to remove the dependency on R environment, and built the interaction Streamlit app for the model.

## Features
-Input HIV status, dose of blood clotting preparation, age and the year number of all patients from a age group in that year in the study.
-Real time prediction of death count.

## Tech Stack
- **Language**: Python
- **Web Framework**: Streamlit
- **Statistical Model**: ZINB
- **Libraries**: NumPy, Pandas, Streamlit

## How to run
.\venv\Scripts\python.exe -m streamlit run stappbypy.py

## Model Detail
- **Count Model**: `death ~ hiv + factor + age + offset(log(py))`
- **Zero-inflation Model**: `death ~ hiv + age + offset(log(py))`

## Original Project
The original group project can be found in https://github.com/yfc0307/Hemophilia-Count-Data-Modelling

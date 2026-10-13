import streamlit as st
import numpy as np
import pandas as pd

#input the variable
beta = {
    "Intercept" : -5.63127239,
    "hivpositive" : 1.92239417,
    "factorlow" : -0.37241511,
    "factormoderate" : -0.44727617,
    "factornone" : -0.33258605,
    "factorunknown" : -0.67625664,
    "age" : 0.03307299
}

gamma = {
    "Intercept" : 1.59802180,
    "hivpositive" : -3.45426592,
    "age" : -0.09549393
}

def pred_zinb(hiv_input, factor_input, age_input, py):

    #hiv_negative and factor_high will be the dummy value
    hiv_pos = 1.0 if hiv_input == "positive" else 0.0
    factor_moderate = 1.0 if factor_input == "moderate" else 0.0
    factor_low = 1.0 if factor_input == "low" else 0.0
    factor_unknown = 1.0 if factor_input == "unknown" else 0.0
    factor_none = 1.0 if factor_input == "none" else 0.0

    #calculation
    count_part = (
        beta["Intercept"] +
        beta["hivpositive"] * hiv_pos +
        beta["factormoderate"] * factor_moderate +
        beta["factorlow"] * factor_low +
        beta["factorunknown"] * factor_unknown +
        beta["factornone"] * factor_none * factor_none +
        beta["age"] * age_input +
        np.log(py)
    )
    mu = np.exp(count_part)

    ZI_part = (
        gamma["Intercept"] +
        gamma["hivpositive"] * hiv_pos +
        gamma["age"] * age_input +
        np.log(py) 
    )
    pi = np.exp(ZI_part)/(1 + np.exp(ZI_part))

    predicted = (1 - pi) * mu
    return predicted

st.title("Hemophilia analysis: ZINB model visualizer")

#Section 1: The problem of dataset
st.header("The problem in the hemophilia dataset: Zero inflaction and overdispersion")
st.image("data_shape.png")

#Section 2: Model Evaluaion
st.header("Model Comparison")
st.image("model_comparison.png")

#Section 3: ZINB model interaction
st.header("Predictor")

#set the interaction object
st.text("The zinb model use 3 independent variable and 1 offset to predict the death count, the variable of zinb is model_zinb_1 <- zeroinfl(death ~ hiv + factor + age + offset(log(py)) | hiv + age + offset(log(py)), data = data)")
hiv = st.radio("Select:", ["negative","positive"])
factor = st.selectbox("The dose of blood clotting preparation:", ["high", "moderate", "low", "unknown", "none"])
age = st.slider("Enter the age", min_value=0, max_value=120)
py = st.slider("The total number of years of all patients from a particular group ", min_value=1, max_value=100)


if st.button("Predict"):
    pred_death_count = pred_zinb(hiv, factor, age, py)
    st.metric(label="Predicted death count:", value=f"{pred_death_count:4f}")
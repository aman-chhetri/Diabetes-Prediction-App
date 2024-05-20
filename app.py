import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('model/trained_model.pkl','rb'))


st.sidebar.markdown("<h1 style='text-align: center;'>Diabetes Prediction App ❤️‍🩹 </h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.sidebar.columns([1, 2, 2, 1])
with col2:
    st.image('assets/image_2.png', width=90)
with col3:
    st.image('assets/image_1.jpg', width=90)

st.sidebar.caption(
    '**A machine learning web application built using Streamlit that predicts whether or `not` a patient has `diabetes` considering multiple health parameters.**')

st.sidebar.caption(
    '**Parameters included: `Blood Pressure`, `Insulin & Glucose Level`, `BMI`, `Age`**')

st.sidebar.markdown('---') 

st.markdown("<h1 style='text-align: center; color: violet;'> Diabetes Prediction App 🧑‍⚕️</h1>", unsafe_allow_html=True)

st.write('The Diabetes Prediction App is a tool that predicts the probability of a patient having diabetes based on diagnostic measurements. This tool is intended for females above the age of 21 years, of Pima Indian Heritage, and uses a dataset from the National Institute of Diabetes and Digestive and Kidney Diseases.')

with st.expander('Click on the dropdown to see - How it works?'):
    st.subheader('Steps to Predict:')
    st.markdown(
        '1. Enter the required information in the input fields.')
    st.markdown(
        '2. Click the `Diabetes Test Result` button to generate the prediction.')
    st.markdown('')


st.sidebar.title('ML Model Details :')

st.sidebar.caption(
    '**Algorithm used:** **`SVM - Support Vector Classifier`**')
st.sidebar.caption(
    '**Dataset used:** **`Pima Indians Diabetes Database`**')
st.sidebar.caption(
    '**Accuracy:** **`78%`**')  


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Pregnancies (Number of times)','6')
    
with col2:
    Glucose = st.text_input('Glucose Level','148')

with col3:
    BloodPressure = st.text_input('Blood Pressure value (mm Hg)','72')

with col1:
    SkinThickness = st.text_input('Skin Thickness value (mm)','35')

with col2:
    Insulin = st.text_input('Insulin Level (mu U/ml)','0')

with col3:
    BMI = st.text_input('BMI value (weight-kg/(height-m)^2)','33.6')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value','0.627')

with col2:
    Age = st.text_input('Age of the Person (years)','50')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result 🔍'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0] == 1):
        diab_diagnosis = 'Ooppss! 😲 The Patient is highly likely to have Diabetes.'
        st.error(diab_diagnosis)

    else:
        diab_diagnosis = 'Relaaxxx! 😊 The Patient is likely Diabetes-Free.'
        st.success(diab_diagnosis)

st.markdown(
    "<footer style='text-align: center; position: fixed; bottom: 0; width: 45%; padding: 10px;'>Made with ❤️ by Aman</footer>",
    unsafe_allow_html=True
)

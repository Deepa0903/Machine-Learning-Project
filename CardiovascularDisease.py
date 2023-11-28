
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
Cardiovascular_Disease_model = pickle.load(open('C:/Users/HP/Desktop/Cardio/heart disease_model3.sav','rb'))


#sidebar for navigate
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                           ['Cardiovascular Disease Prediction'],
                           icons = ['heart'],
                           default_index=0)
    
if (selected == 'Cardiovascular Disease Prediction'):
    st.title("Cardiovascular Disease Prediction System")
    
    age = st.text_input('Age')
    gender = st.text_input('Sex')
    height = st.text_input('Height')
    weight = st.text_input('Weight')
    ap_hi = st.text_input('ap_hi mmHg [Blood pressure (ap_hi / ap_lo)]')
    ap_lo = st.text_input('ap_lo mmHg [Blood pressure (ap_hi / ap_lo)]')
    cholesterol = st.text_input('cholesterol [1: normal(Less than 200 mg/dL), 2: above normal(200-239 mg/dL), 3: well above normal(240 mg/dL and above)]')
    gluc = st.text_input('Glucose [1: normal(70 to 100 (mg/dL)), 2: above normal(100 to 125 mg/dL), 3: well above normal(126 mg/dL or higher)]')
    smoke = st.text_input('Smokeing [0:No Smoke, 1:smoke]')
    alco = st.text_input('Alcohol Intake [0:Do not Drink, 1:Drink]')
    active = st.text_input('Physical Activity [0:No, 1:Yes]')
        
   
        
     
     
   # ... (your existing code)

# code for Prediction
heart_diagnosis = ''

# creating a button for Prediction
if st.button('Cardiovascular Disease Test Result'):
    if any(val == '' for val in [age, gender, height, weight, ap_hi, ap_lo, cholesterol , gluc, smoke, alco, active]):
        st.error("Please fill in all the fields.")
    else:
        try:
            heart_prediction =Cardiovascular_Disease_model.predict([[float(age), float(gender), float(height), float(weight), float(ap_hi), float(ap_lo), float(cholesterol), float(gluc), float(smoke), float(alco), float(active)]])
            prediction_value = int(heart_prediction[0])
            if prediction_value == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Error: Invalid input. Please enter numeric values.'

    st.success(heart_diagnosis)

        
    

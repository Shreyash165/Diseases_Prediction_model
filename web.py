import os
import pickle   # For loading the trained model
import streamlit as st      # Web app
from streamlit_option_menu import option_menu # Custom option menu

st.set_page_config(page_title="Prediction of Heart Disease",
                   layout="wide",
                   page_icon="🏥")

# Load models
diabetes_model = pickle.load(open(r"C:\Users\manes\OneDrive\Desktop\Prediction\Traning_models\diabetes_model.sav", 'rb'))
Heart_model = pickle.load(open(r"C:\Users\manes\OneDrive\Desktop\Prediction\Traning_models\Heart_model.sav", 'rb'))
parkinson_model = pickle.load(open(r"C:\Users\manes\OneDrive\Desktop\Prediction\Traning_models\Parkinson_model.sav", 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Prediction System",
                           ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson Prediction"],
                           menu_icon='hospital-fill',
                           icons=["activity", 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction ML App")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("No of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI of the Patient")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the Patient")

    diab_diagnosis = ''

    # Predict Button
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float correctly
            user_input = [
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
                
            ]

            # Reshape input for the model
            user_input = [user_input]  # Convert to 2D list

            # Make prediction
            diab_prediction = diabetes_model.predict(user_input)

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetes Positive'
            else:
                diab_diagnosis = 'The person is Diabetes Negative'

            # Show result
            st.success(diab_diagnosis)

        except ValueError:
            st.error("Please enter valid numerical values.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
            
            # Heart Disease Prediction
elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction ML App")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("sex")
    with col3:
        cp = st.text_input("cp")
    with col1:
        trestbps = st.text_input("trestbps")
    with col2:
        chol = st.text_input("chol")
    with col3:
        fbs = st.text_input("fbs")
    with col1:  
        restecg = st.text_input("restecg")
    with col2:
        thalach = st.text_input("thalach")
    with col3:
        exang = st.text_input("exang")
    with col1:
        oldpeak = st.text_input("oldpeak")
    with col2:
        slope = st.text_input("slope")
    with col3:
        ca = st.text_input("ca")
    with col1:
        thal = st.text_input("thal")
    diab_diagnosis = ''

    # Predict Button
    if st.button('Heart Test Result'):
        try:
            # Convert inputs to float correctly
            user_input = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]

            # Reshape input for the model
            user_input = [user_input]  # Convert to 2D list

            # Make prediction
            heart_prediction = Heart_model.predict(user_input)

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having Heart Disease'
            else:
                heart_diagnosis = 'The person is not having Heart Disease'

            # Show result
            st.success(heart_diagnosis)

        except ValueError:
            st.error("Please enter valid numerical values.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
        # parkinson Detection
elif selected == "Parkinson Prediction":
    st.title("Parkinson Prediction ML App")

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input("MDVP_Fo(Hz)")
    with col2:
        MDVP_Fhi = st.text_input("MDVP_Fhi(Hz)")
    with col3:
        MDVP_Flo = st.text_input("MDVP_Flo(Hz)")
    with col1:
        MDVP_Jitter_percent = st.text_input("MDVP_Jitter(%)")
    with col2:
        MDVP_Jitter_abs = st.text_input("MDVP_Jitter(Abs)")
    with col3:
        MDVP_RAP = st.text_input("MDVP_RAP")
    with col1:
        MDVP_PPQ = st.text_input("MDVP_PPQ")
    with col2:
        Jitter_DDP= st.text_input("Jitter_DDP")
    with col3:
        MDVP_Shimmer = st.text_input("MDVP_Shimmer")
    with col1:
        MDVP_Shimmer_dB = st.text_input("MDVP_Shimmer_dB")
    with col2:
        Shimmer_APQ3 = st.text_input("Shimmer_APQ3")
    with col3:
        Shimmer_APQ5 = st.text_input("Shimmer_APQ5")
    with col1:
        MDVP_APQ = st.text_input("MDVP_APQ")
    with col2:
        Shimmer_DDA = st.text_input("Shimmer_DDA")
    with col3:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col1:
        spread1 = st.text_input("spread1")
    with col2:
        spread2 = st.text_input("spread2")
    with col3:
        D2 = st.text_input("D2")
    with col1:
        PPE = st.text_input("PPE")
    diab_diagnosis = ''

    # Predict Button
    if st.button('Parkinson Test Result'):
        try:
            # Convert inputs to float correctly
            user_input = [
                float(MDVP_Fo),
                float(MDVP_Fhi),
                float(MDVP_Flo),
                float(MDVP_Jitter_percent),
                float(MDVP_Jitter_abs),
                float(MDVP_Shimmer),
                float(HNR),
                float(RPDE),
                float(DFA),
                float(spread1),
                float(spread2),
                float(D2),
                float(PPE)
            ]

            # Reshape input for the model
            user_input = [user_input]  # Convert to 2D list

            # Make prediction
            parkinson_prediction = parkinson_model.predict(user_input)

            if parkinson_prediction[0] == 1:
                parkinson_diagnosis = 'The person is having Parkinson Disease'
            else:
                parkinson_diagnosis = 'The person is not having Parkinson Disease'

            # Show result
            st.success(parkinson_diagnosis)

        except ValueError:
            st.error("Please enter valid numerical values.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
            
    
            
        

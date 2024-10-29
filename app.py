import streamlit as st
from datetime import datetime

# Placeholder functions for risk algorithms
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    return "High" if risk_score > 15 else "Moderate" if risk_score > 10 else "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 15 else "Low"

def calculate_copd_risk(smoking_years, age, fev1):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1)
    return "High" if risk_score > 25 else "Moderate" if risk_score > 15 else "Low"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1):
    risk_score = (frequency_of_symptoms * 2) + (nighttime_symptoms * 3) + (inhaler_use * 1.5) - (fev1 * 0.1)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 10 else "Low"

# Function for AI Assistant responses
def ai_assistant_response(query):
    if "follow-up" in query.lower():
        return "For follow-ups, coordinate with your healthcare provider to determine frequency based on your conditions and risk levels."
    elif "monitoring" in query.lower():
        return "Monitoring includes tracking key parameters specific to each condition, such as blood pressure, glucose, and lung function."
    elif "self-management" in query.lower():
        return "Self-management involves lifestyle changes, adherence to medications, and regular monitoring of your conditions."
    else:
        return "I'm here to assist with questions on risk assessment, monitoring, self-management, and follow-up plans for chronic conditions."

# Streamlit App Layout
st.title("Comprehensive Multi-Condition Risk Stratification, Care Plan, and AI Assistant")
st.write("This app assesses risk for chronic conditions, provides a unified care plan for multiple conditions, and includes an AI assistant for personalized queries.")

# Define tabs for each condition and the AI Assistant
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan", "AI Assistant"])

# Dictionary to store risk levels for each condition
results = {}

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)
    smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker"])

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        results["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        results["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1_copd = st.number_input("FEV1 (%) - COPD", min_value=20, max_value=100, value=80)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1_copd)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        results["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Asthma Symptoms (days per week)", 0, 7, 3)
    nighttime_symptoms = st.slider("Nighttime Symptoms (days per week)", 0, 7, 1)
    inhaler_use = st.slider("Inhaler Use (days per week)", 0, 7, 2)
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        results["Asthma"] = asthma_risk

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan for Multi-Condition Management")

    high_risk_conditions = [condition for condition, risk in results.items() if risk == "High"]
    moderate_risk_conditions = [condition for condition, risk in results.items() if risk == "Moderate"]
    
    # Display combined risk levels
    if high_risk_conditions:
        st.write("### High-Risk Conditions:")
        for condition in high_risk_conditions:
            st.write(f"- **{condition}**")

    if moderate_risk_conditions:
        st.write("### Moderate-Risk Conditions:")
        for condition in moderate_risk_conditions:
            st.write(f"- **{condition}**")

    # Unified care recommendations based on multiple conditions
    if high_risk_conditions or moderate_risk_conditions:
        st.subheader("Personalized Care Recommendations")
        st.write("- **Self-Management Support**: Integrate lifestyle changes such as diet, physical activity, and medication adherence for all high and moderate-risk conditions.")
        
        # Monitoring Plan
        st.subheader("Monitoring Plan")
        if "Cardiovascular" in high_risk_conditions or "Diabetes" in high_risk_conditions:
            st.write("- **Daily**: Blood pressure and/or blood glucose tracking at home.")
        if "COPD" in high_risk_conditions or "Asthma" in high_risk_conditions:
            st.write("- **Daily**: Peak flow and FEV1 tracking.")
        st.write("- **Weekly**: Symptoms diary to monitor condition management and adjust if necessary.")

        # Follow-Up Plan
        st.subheader("Follow-Up Plan")
        if high_risk_conditions:
            st.write("- **Frequency**: Monthly follow-ups for high-risk conditions.")
        if moderate_risk_conditions:
            st.write("- **Frequency**: 3-6 months for moderate-risk conditions.")
        st.write("- **Coordination**: Single follow-up sessions to discuss all conditions with healthcare provider.")

        # Outcome Evaluation Plan
        st.subheader("Outcome Evaluation Plan")
        st.write("- **Quarterly Assessments**: Evaluate improvement or adjustment needs across all conditions.")
        st.write("- **Biannual Review**: Comprehensive check to adjust long-term management plan if necessary.")

    else:
        st.success("No high-risk or moderate-risk conditions identified. Continue regular preventive care.")

# AI Assistant Tab
with tab6:
    st.header("AI Health Assistant")

    # User input for AI Assistant
    user_query = st.text_input("Ask the AI Assistant about your health conditions, care plans, monitoring, or follow-up.", "")
    
    # Button to submit query
    if st.button("Submit Query"):
        if user_query:
            # Generate AI response
            response = ai_assistant_response(user_query)
            
            # Display conversation history
            st.write("**You**: ", user_query)
            st.write("**AI Assistant**: ", response)

# Display assessment date and time
st.write("### Date and Time of Assessment")
st.write("Assessment Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

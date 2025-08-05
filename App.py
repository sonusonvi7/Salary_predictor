import streamlit as st
import joblib
import numpy as np
import plotly.express as px
import pandas as pd
import os

# Page configuration
st.set_page_config(
    page_title="Salary Estimation App",
    page_icon=":money_with_wings:",
    layout='wide',
    initial_sidebar_state="expanded"
)

# Sidebar branding and info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135789.png", width=80)
    st.title("Salary Estimation App")
    st.markdown("Welcome! :wave:")
    st.caption("🏢 Predict your expected salary using Machine Learning.")
    st.markdown("---")
    st.info("Enter your details to see your salary estimate instantly!\n\nMade with ❤️")

# Main title and subtitle
st.markdown("""
    <div style='text-align: center; padding-bottom: 0.5rem'>
        <h1 style='color:#1864ab;'>💸 Salary Estimation App</h1>
        <p style='font-size: 1.2rem; color:#555;'>Predict your expected salary based on company experience!</p>
    </div>
""", unsafe_allow_html=True)

# Columns for layout symmetry
col_blank1, col_main, col_blank2 = st.columns([1,2,1])
with col_main:
    st.image(
        "https://www.pexels.com/photo/person-holding-debit-card-50987/",
        caption="It's time to know your worth! 💰",
        use_column_width=True
    )

st.markdown("---")

# Inputs in a card style
st.markdown("#### 📝 Fill out the details:")

card = st.container()
with card:
    col1, col2, col3 = st.columns(3)
    with col1:
        years_at_company = st.slider("Years at company", 0, 40, 3)
    with col2:
        satisfaction_level = st.slider("Satisfaction level", 0.0, 1.0, 0.7, 0.01)
    with col3:
        average_monthly_hours = st.slider("Avg Monthly Hours", 80, 320, 160)

    st.progress(int((satisfaction_level)*100), text="Satisfaction Level Progress")
    st.markdown(" ")


# Prediction logic
base_path = os.path.dirname(__file__)
scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))
model = joblib.load(os.path.join(base_path, "model.pkl"))

X = [years_at_company, satisfaction_level, average_monthly_hours]
X_array = scaler.transform([np.array(X)])  # scale input

predict_button = st.button("✨ Predict Salary", use_container_width=True)

if predict_button:
    st.balloons()
    prediction = model.predict(X_array)
    st.success(f"### 🎉 Predicted Salary: **₹{prediction[0]:,.2f}**", icon="💰")
    st.divider()

    # Visual feedback of input
    user_profile = pd.DataFrame({
        "Feature": ["Years at Company", "Satisfaction Level", "Monthly Hours"],
        "Value": X
    })
    fig = px.bar(
        user_profile, 
        x="Feature", y="Value", color="Feature", 
        title="Your Work Profile", 
        color_discrete_sequence=px.colors.sequential.Blues,
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

    # Fun/Extra: Feedback based on satisfaction
    if satisfaction_level < 0.4:
        st.warning("Your satisfaction level is quite low. Consider discussing this with your manager for possible improvements! 🚀")
    elif satisfaction_level > 0.85:
        st.info("You seem very satisfied in your role! 🌟")
else:
    st.info("Please enter your details and click **Predict Salary** to see the estimated amount.", icon="💡")

st.markdown("---")
st.caption("© 2024 Salary Estimation App | Powered by Sonvi Assis Noronha with Streamlit & Machine Learning 🚀")


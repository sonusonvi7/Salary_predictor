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
    st.info("Enter your details to see your salary estimate instantly!\n\nMade with ❤️ using Streamlit.")

# --- ADD THIS BLOCK FOR VIDEO BACKGROUND ---
st.markdown("""
    <style>
    .video-background {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
        opacity: 0.3;
        object-fit: cover;
    }
    </style>
    <video autoplay muted loop playsinline class='video-background'>
        <source src='https://cdn.pixabay.com/vimeo/457436623/money-21670.mp4?width=640&hash=1f88920752cef71aa019fb710178ad33ed786883' type='video/mp4'>
    </video>
""", unsafe_allow_html=True)

# Main title and subtitle (leave as is)
st.markdown("""
    <div style='text-align: center; padding-bottom: 0.5rem'>
        <h1 style='color:#1864ab;'>💸 Salary Estimation App</h1>
        <p style='font-size: 1.2rem; color:#555;'>Predict your expected salary based on company experience!</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# REMOVE the previous col_blank1, col_main, col_blank2 block and the st.image() in it

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

# (The rest of your app logic remains unchanged.)

import streamlit as st
import numpy as np
import random

# Set up dark mode
st.set_page_config(page_title="Finance Calculator", page_icon="📈", layout="wide")

# Custom CSS for better layout and readability
st.markdown(
    """
    <style>
        .stApp {
            background-color: #121212;
            color: white;
        }
        .css-1d391kg p, .st-bf, .st-cq, .st-dj, label {
            color: white !important;
        }
        .stSlider, .stNumberInput {
            width: 100% !important;
        }
    </style>
    """, unsafe_allow_html=True
)

# Finance trivia section
finance_trivia = [
    "The Rule of 72 is a simple way to estimate how long an investment will take to double given a fixed annual return.",
    "Warren Buffett bought his first stock at age 11.",
    "The New York Stock Exchange was founded in 1792.",
    "The highest stock market return in a single year was 50.3% (1954, S&P 500).",
    "Compound interest was called the 'eighth wonder of the world' by Albert Einstein.",
    "The largest single-day stock market drop in history occurred on Black Monday, October 19, 1987.",
    "Bitcoin was first introduced in 2009 by an anonymous person or group using the name Satoshi Nakamoto.",
    "The first publicly traded company was the Dutch East India Company in 1602.",
    "The US dollar is the most widely used reserve currency in the world.",
    "Index funds often outperform actively managed funds over the long term.",
]

# Functions for calculations
def calculate_sip(amount, rate, years):
    if rate == 0:
        return amount * years * 12  # Simple addition for 0% interest
    rate = rate / 100 / 12
    months = years * 12
    return amount * ((1 + rate) ** months - 1) / rate * (1 + rate)

def calculate_lumpsum(amount, rate, years):
    return amount * (1 + rate / 100) ** years

def calculate_fd(amount, rate, years):
    return amount * (1 + rate / 100) ** years

# UI Components
st.title("📊 Finance Calculator")

# Tabs for SIP and Lump Sum calculations
tab1, tab2 = st.tabs(["📈 Monthly SIP", "💰 Lump Sum Investment"])

with tab1:
    st.subheader("📈 Monthly SIP Calculator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("### Investment Inputs")
    
    with col2:
        sip_amount = st.number_input("Enter Monthly SIP Amount (₹):", min_value=0, value=10000, step=1000, key="sip_amount")
        sip_years = st.number_input("Enter Investment Duration (years):", min_value=1, value=10, step=1, key="sip_years")
        sip_rate = st.slider("Select Expected Annual Return (%):", 1, 100, 10, key="sip_rate")  # Min set to 1%
    
    sip_result = calculate_sip(sip_amount, sip_rate, sip_years)
    fd_result = calculate_fd(sip_amount, 5, sip_years)  # Assume 5% for FD
    
    st.subheader("📊 SIP Returns")
    st.write(f"**Final SIP Corpus:** ₹{sip_result:,.2f}")
    st.write(f"**Fixed Deposit Returns (5% rate):** ₹{fd_result:,.2f}")

with tab2:
    st.subheader("💰 Lump Sum Investment Calculator")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write("### Investment Inputs")
    
    with col2:
        lumpsum_amount = st.number_input("Enter Lump Sum Amount (₹):", min_value=0, value=100000, step=5000, key="lumpsum_amount")
        lumpsum_years = st.number_input("Enter Investment Duration (years):", min_value=1, value=10, step=1, key="lumpsum_years")
        lumpsum_rate = st.slider("Select Expected Annual Return (%):", 1, 100, 10, key="lumpsum_rate")  # Min set to 1%
    
    lumpsum_result = calculate_lumpsum(lumpsum_amount, lumpsum_rate, lumpsum_years)
    fd_lumpsum_result = calculate_fd(lumpsum_amount, 5, lumpsum_years)  # Assume 5% for FD
    
    st.subheader("📊 Lump Sum Returns")
    st.write(f"**Final Lump Sum Corpus:** ₹{lumpsum_result:,.2f}")
    st.write(f"**Fixed Deposit Returns (5% rate):** ₹{fd_lumpsum_result:,.2f}")
    st.write(f"**Total Interest Earned:** ₹{lumpsum_result - lumpsum_amount:,.2f}")
    st.write(f"**Total FD Interest Earned:** ₹{fd_lumpsum_result - lumpsum_amount:,.2f}")

# Trivia Section
st.subheader("💡 Finance Trivia")
st.write(random.choice(finance_trivia))

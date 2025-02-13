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
        .css-1d391kg p, .st-bf, .st-cq, .st-dj, label, .stButton > button {
            color: white !important;
        }
        .stSlider, .stNumberInput, .stTextInput {
            width: 100% !important;
            background-color: #333 !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True
)

# Finance trivia section with India-based trivia
finance_trivia = [
    "The Rule of 72 is a simple way to estimate how long an investment will take to double given a fixed annual return.",
    "Warren Buffett bought his first stock at age 11.",
    "The New York Stock Exchange was founded in 1792.",
    "The highest stock market return in a single year was 50.3% (1954, S&P 500).",
    "Compound interest was called the 'eighth wonder of the world' by Albert Einstein.",
    "The Bombay Stock Exchange (BSE) is Asia's oldest stock exchange, established in 1875.",
    "The Reserve Bank of India (RBI) was established in 1935 to regulate India's financial system.",
    "India's mutual fund industry started in 1963 with the establishment of Unit Trust of India (UTI).",
    "The National Stock Exchange (NSE) was founded in 1992 and is the largest stock exchange in India.",
    "The Indian rupee symbol (₹) was officially adopted in 2010.",
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

# UI Components
st.title("📊 Finance Calculator")

# Tabs for SIP and Lump Sum calculations
tab1, tab2 = st.tabs(["📈 Monthly SIP", "💰 Lump Sum Investment"])

with tab1:
    st.subheader("📈 Monthly SIP Calculator")
    sip_amount = st.number_input("Enter Monthly SIP Amount (₹):", min_value=0, value=10000, step=1000, key="sip_amount")
    sip_years = st.number_input("Enter Investment Duration (years):", min_value=1, value=10, step=1, key="sip_years")
    sip_rate = st.slider("Select Expected Annual Return (%):", 1, 100, 10, key="sip_rate")  # Min set to 1%
    
    sip_result = calculate_sip(sip_amount, sip_rate, sip_years)
    total_invested_sip = sip_amount * sip_years * 12
    total_profit_sip = sip_result - total_invested_sip
    total_profit_percent_sip = (total_profit_sip / total_invested_sip) * 100
    
    st.subheader("📊 SIP Returns")
    st.write(f"**Total Invested:** ₹{total_invested_sip:,.2f}")
    st.write(f"**Final SIP Corpus:** ₹{sip_result:,.2f}")
    st.write(f"**Total Profit Earned:** ₹{total_profit_sip:,.2f}")
    st.write(f"**Total Profit Percentage:** {total_profit_percent_sip:.2f}%")

with tab2:
    st.subheader("💰 Lump Sum Investment Calculator")
    lumpsum_amount = st.number_input("Enter Lump Sum Amount (₹):", min_value=0, value=100000, step=5000, key="lumpsum_amount")
    lumpsum_years = st.number_input("Enter Investment Duration (years):", min_value=1, value=10, step=1, key="lumpsum_years")
    lumpsum_rate = st.slider("Select Expected Annual Return (%):", 1, 100, 10, key="lumpsum_rate")  # Min set to 1%
    
    lumpsum_result = calculate_lumpsum(lumpsum_amount, lumpsum_rate, lumpsum_years)
    total_profit_lumpsum = lumpsum_result - lumpsum_amount
    total_profit_percent_lumpsum = (total_profit_lumpsum / lumpsum_amount) * 100
    
    st.subheader("📊 Lump Sum Returns")
    st.write(f"**Total Invested:** ₹{lumpsum_amount:,.2f}")
    st.write(f"**Final Lump Sum Corpus:** ₹{lumpsum_result:,.2f}")
    st.write(f"**Total Profit Earned:** ₹{total_profit_lumpsum:,.2f}")
    st.write(f"**Total Profit Percentage:** {total_profit_percent_lumpsum:.2f}%")

# Trivia Section with refresh button
st.subheader("💡 Finance Trivia")
trivia_placeholder = st.empty()
if st.button("🔄 Refresh Trivia", key="refresh_trivia"):
    trivia_placeholder.write(random.choice(finance_trivia))
else:
    trivia_placeholder.write(random.choice(finance_trivia))

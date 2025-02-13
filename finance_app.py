import streamlit as st
import numpy as np
import random

# Set up dark mode
st.set_page_config(page_title="Finance Calculator", page_icon="📈", layout="centered")

# Custom CSS for dark mode
st.markdown(
    """
    <style>
        .stApp {
            background-color: #121212;
            color: white;
        }
        .css-1d391kg p {
            color: white;
        }
        .st-bf {
            color: white;
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
    "The longest bull market in history lasted from 2009 to 2020.",
    "Gold has been used as a form of currency for over 3,000 years.",
    "The world's first credit card was introduced by Diners Club in 1950.",
    "The Roth IRA was introduced in 1997 as a tax-advantaged retirement account.",
    "A diversified portfolio helps reduce investment risk.",
    "The Great Depression lasted from 1929 to 1939.",
    "A bond's yield and price move in opposite directions.",
    "Inflation reduces the purchasing power of money over time.",
    "The largest bank in the world by assets is the Industrial and Commercial Bank of China (ICBC).",
    "The first modern stock exchange was established in Amsterdam in 1602.",
    "Stock market corrections are common and usually happen every 1-2 years.",
    "The S&P 500 has historically averaged around 8-10% annual returns.",
    "Credit scores range from 300 to 850.",
    "A bear market is defined as a 20% drop in stock prices from recent highs.",
    "Investing early allows more time for compound interest to work.",
    "Stock splits increase the number of shares but not the total value of the investment.",
    "The term 'blue-chip stocks' refers to financially stable and well-established companies.",
    "FDs in India are considered one of the safest investments but offer lower returns compared to equities.",
    "The Nasdaq stock exchange is known for being tech-focused.",
    "Hedge funds use high-risk investment strategies to maximize returns.",
    "Cryptocurrencies are decentralized digital assets.",
    "Real estate is considered an alternative investment class.",
    "Market capitalization is the total value of a company's outstanding shares.",
    "A mutual fund pools money from multiple investors to invest in stocks, bonds, or other assets.",
    "Inflation in the long run reduces the purchasing power of savings.",
    "The bond market is larger than the stock market in total value.",
    "Gold and silver are considered safe-haven investments during economic downturns.",
    "The PE ratio measures a company's stock price relative to its earnings.",
    "An emergency fund should cover 3-6 months of expenses.",
    "401(k) retirement plans in the US offer tax advantages to savers.",
    "Dollar-cost averaging helps reduce the impact of market volatility.",
    "Credit cards can improve or damage your credit score depending on usage.",
    "The Federal Reserve controls monetary policy in the US.",
    "Market bubbles occur when asset prices rise far above their intrinsic value.",
    "Diversification reduces overall investment risk.",
    "Warren Buffett's company, Berkshire Hathaway, has averaged over 20% annual returns for decades.",
    "The S&P 500 index includes 500 of the largest US companies.",
    "A stock buyback reduces the number of shares available in the market.",
    "Central banks control interest rates to manage inflation and economic growth.",
]

# Functions for calculations
def calculate_sip(amount, rate, years):
    rate = rate / 100 / 12
    months = years * 12
    return amount * ((1 + rate) ** months - 1) / rate * (1 + rate)

def calculate_lumpsum(amount, rate, years):
    return amount * (1 + rate / 100) ** years

def calculate_fd(amount, rate, years):
    return amount * (1 + rate / 100) ** years

# UI Components
st.title("📊 Finance Calculator")
amount = st.number_input("Enter the amount (₹):", min_value=0, value=10000, step=1000)
years = st.number_input("Enter time horizon (years):", min_value=1, value=10, step=1)
rate = st.slider("Select Interest Rate (% per annum):", 0, 100, 10)

# Calculations
sip_result = calculate_sip(amount, rate, years)
lumpsum_result = calculate_lumpsum(amount, rate, years)
fd_result = calculate_fd(amount, 5, years)  # Assume 5% for FD

# Display Results
st.subheader("📈 Investment Returns")
st.write(f"**SIP Returns:** ₹{sip_result:,.2f}")
st.write(f"**Lump Sum Returns:** ₹{lumpsum_result:,.2f}")
st.write(f"**Fixed Deposit Returns (5% rate):** ₹{fd_result:,.2f}")

# Trivia Section
st.subheader("💡 Finance Trivia")
st.write(random.choice(finance_trivia))

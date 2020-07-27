import streamlit as st

initial_investment: float = st.sidebar.number_input('Initial investment')
years: int = st.sidebar.slider('Years', min_value=1, max_value=50)
return_rate: float = st.sidebar.number_input('Return rate')

# additioan_contribution: float = 100.00

accrued_amount = initial_investment * (1 + return_rate/100)**years

st.write(accrued_amount)

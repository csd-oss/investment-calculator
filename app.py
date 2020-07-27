import streamlit as st

initial_investment: float = 20000.00
years: int = 10
return_rate: float = 6.00

# additioan_contribution: float = 100.00

accrued_amount = initial_investment * (1 + return_rate/100)**years

st.write(accrued_amount)

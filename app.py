import streamlit as st

initial_investment: float = st.sidebar.number_input(
    'Initial investment',
    value=10000.00)
years: int = st.sidebar.slider('Years', min_value=1, max_value=50, value=10)
return_rate: float = st.sidebar.number_input('Return rate', value=6.00)

accrued_amount = initial_investment * (1 + return_rate/100)**years

st.write(f'''If you invest {initial_investment} for {years} years with
return rate of {return_rate} at the end of that period
you will get {accrued_amount}''')

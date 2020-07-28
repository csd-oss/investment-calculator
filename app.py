import streamlit as st

initial_investment: float = st.sidebar.number_input(
    'Initial investment',
    value=10000.00)
years: int = st.sidebar.slider('Years', min_value=1, max_value=50, value=10)
return_rate: float = st.sidebar.number_input('Return rate', value=6.00)
compound_per_year: int = st.sidebar.slider(
    'Compound per year', min_value=1, max_value=12, value=1)
r = (return_rate/100)
accrued_amount = initial_investment * (
    1 + r/compound_per_year)**(years*compound_per_year)

st.write(f'''If you invest {round(initial_investment, 2)} for
{round(years, 2)} years with return rate of {round(return_rate, 2)}
at the end of that period you will get **{round(accrued_amount, 2)}**.''')

if st.sidebar.checkbox('I WILL ADD MONEY TO IT'):
    addition_value = st.sidebar.number_input('Addition value', value=100.00)

    addition_future_value = accrued_amount + addition_value*((
        ((1+r)**(years))-1)/r)

    st.write(round(addition_future_value, 2))

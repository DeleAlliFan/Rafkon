import streamlit as st
import pandas as pd

st.title("Economics")

cap_comm_other = pd.DataFrame(
    {
        "Capititalism": ["Good at producing goods", "Lots of taxes","Trading between all countries", "","","","",""],
        "Marx's Version of Commnunism": ["No social classes", "Free Healthcare","","","","","",""],
        "Other": ["When the price of food goes up minimum wage goes up", "Taxes never go up", "5% of yearly income to taxes for people who make 0-10000 dollars", "15% of yearly income to taxes for people who make 10001-40000 dollars", "20% of yearly income to taxes for people who make 40001-50000 dollars", "30% of yearly income to taxes for people who make 50001-70000 dollars", "45% of yearly income to taxes for people who make 70001 and over", "Country has no religious background"],
    },
)
st.table(cap_comm_other) 

st.write("In a communist society selling goods is not something they are good at so the capitalist will run that part. The reason why there are a lot of taxes is to allow free healthcare to happen. The idea of having no social classes means that there are no differences between people. The reason why the yearly tax rate changes based on money made is to make sure that no one is taxed too much, even though there is a lot of taxes. The best way to be impartial is to trade with all countries. Also having no religious background means that anyone can live there without feeling unsafe because of his religion.")

st.image("https://gbhspanthertales.com/wp-content/uploads/2022/05/health-care.jpg")
st.image("https://resourcesforhistoryteachers.pbworks.com/f/1554064321/Screen%20Shot%202019-03-31%20at%204.31.35%20PM.png")
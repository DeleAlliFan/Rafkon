import streamlit as st
import pandas as pd
import time
st.subheader("National Sport")
lt= pd.read_csv("league_table.csv")
pd.set_option("display.max_columns", None)

st.write("The National Sport is Football")
st.write("The league is the Rarkonian Premier League")


@st.dialog("Sign up for a Weekly Newsletter", width="small",dismissible=False)
def email_form():
    name = st.text_input("Legal Name", placeholder="John Doe")
    email = st.text_input("Email Adress", placeholder="example@example.com")
    phone_number= st.text_input("Phone Number", placeholder="XXX-XXX-XXXX")
    st.write("P.S. If you do not fill out all parts of the form you will not get your newsletter.")
    if st.button("Sign Up"):
        st.rerun()


if st.button("Sign up for a Weekly Newsletter on the Latest Football News"):
    email_form()




st.write("Below is the final table of the season that just finished")

st.dataframe(lt,hide_index=True)

st.markdown("#")

st.subheader("FA")
st.write("The national team has the nickname “Exercitus Telepathicus” meaning The Telepathic Army")
st.write("The head of the RFA, Rafkonian FA, is…")
st.write("REEEEEEECCCCCEEEE JJJJJJJJJJAAAAAMMMMEEEESSSS!")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_a_XlTEskKE1RxCroswmcBQ8M0D0ZX5WN3w&s")
st.markdown('If you have any issues about the system you Can give Recce a call at <a href="tel:+12127879534"> +1 (212) 787-9534.', unsafe_allow_html=True)

st.markdown("#")

st.subheader("National Team")
st.write("National Team Crest:")
st.image("Crest.jpg")
st.write("National Team Jersey:")
st.image("jersey.jpg")
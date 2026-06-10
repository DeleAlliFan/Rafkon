import streamlit as st
import pandas as pd

st.title("Governance")


order = pd.DataFrame(
    {
        "Line of official order 1": ["President", "Vice-President","Speaker-of-the-House", "Senator","Governor","State Attorney General","State Senate","Mayor", "District Attorney"],
        "Line of official order 2": ["President", "Vice-President","Speaker-of-the-House", "Senator","Governor","State Attorney General","State Senate","Mayor", "District Attorney"],
    },
)
st.table(order)

st.image("https://blog.littletoncoin.com/wp-content/uploads/3presidents.jpg")
st.image("https://i.ebayimg.com/images/g/ySQAAOSwRQ5lGgxP/s-l400.jpg")

st.write("")
st.write("By having more than one president it means that before a law is made or changed both of the presidents must agree on it. If they can’t, the decisions go to the vice presidents.")
st.write("The Presidents lead the country. Vice Presidents are the presidents underlings. The speakers of the houses are 3rd in line to the presidency. The senators are part of the senates. The representatives are lower than the senators in the houses of representatives. The Governors run the states with the help of the state senates. The State attorney generals are the chief legal officers in the states. The state senators give ideas to the governors Mayors are the head of the cities. The District attorneys are the representatives of each district. No political parties just right or left.")
st.write("")
st.write("Every four years everyone is up for election and the voters must vote their top two choices in every category. The fact that every position in office changes at the same thime means that everyone will vote for every single category since the biggest issue is getting people to vote for some positions and not others.")
st.write("The motto of the government is “No freedom without choice”.")

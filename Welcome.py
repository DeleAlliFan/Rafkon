import streamlit as st

st.title("Welcome to Rafkon")
toggle = st.toggle("Dark Mode")
if toggle:
    st.write("Never Gonna Give You Up. Never Gonna Let You Down.")
    st.rerun()

st.write("")
st.write("The Rafkonian National Anthem is Life is a Highway by the Rascal Flatts")

st.video("Rascal Flatts - Life Is a Highway (From _Cars__Official Video).mp4")

st.write("Below is the flag of Rafkon:")

st.image("0-1.jpg")

st.markdown("#")

st.subheader("The current presidents are Eric Adams and Ted Cruz")
st.write("Eric Adams:")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTEuBJWBky89p3oenwZDb_ERb7UhHF_5gsGu_gB2J7sN7lFpPnruh49pfIDcPQEXNsgABDgbFetMtRD4b562OWEkw029xifYwLok4kSg&s=10")
st.write("Ted Cruz:")
st.image("https://s3.amazonaws.com/ballotpedia-api4/files/thumbs/200/300/Ted_Cruz.jpg")
st.write("")
st.subheader("The current Vice presidents are Kathy Hochul and Chuck Schumer")
st.write("Kathy Hochul:")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVmZvKyYYfjoNALxLreUfCrZ8Fl4HcRHQbNIw_KjJ6sCjpyIAEzDe3kWr48diT-oHj8hs072dI6rWn7Vt-qV5qHOv183CIexO-QxiJHvM&s=10")
st.write("Chuck Schumer:")
st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcTYs6xI8-B6h2kRqIYzJw985T-rLbdH6lUH7WOeVHlo1MLl_aIcemiKY3eFJMyd7-zwTvGn1WDsQZdiwck")
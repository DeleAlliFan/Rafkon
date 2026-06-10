import streamlit as st


Welcome = st.Page(
    page="Welcome.py",
    title="Welcome",
    default=True,
)

Governance = st.Page(
    page="Governance.py",
    title="Governance",
)

Economics = st.Page(
    page="Economics.py",
    title="Ecomonics",
)

Society = st.Page(
    page="Society.py",
    title="Society & Culture",
)

Football = st.Page(
    page="Football.py",
    title="Football",
)

nav_menu = st.navigation(
    {
        "Welcome": [Welcome],
        "Project": [Governance, Economics, Society,Football],
    },
    position="top"
)

st.logo("0-1.jpg")

nav_menu.run()
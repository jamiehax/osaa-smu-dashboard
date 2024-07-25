import streamlit as st

st.title("OSAA SMU's Data App")
st.markdown("Welcome to the Office of the Speical Advisor to Africa's Strategic Management Unit's Data App. Use the sidebar to the left or the page links below to navigate between the data products. ")

st.markdown("<hr>", unsafe_allow_html=True)
st.write("")

st.subheader("Dashboard")
col1, col2 = st.columns(2)
with col1:
    st.markdown("The SMU's Data Dashboard allows for quick access to summary statistics about a dataset, as well as a detailed report on the dataset with *YData Profiling*.")
with col2:
    st.page_link("dashboard.py", label="Dashboard", icon=":material/analytics:")

st.subheader("Data Sheet")
col1, col2 = st.columns(2)
with col1:
    st.markdown("The SMU's Data Sheet allows for the automation of excel sheet processes and analysis with *Mitosheet*.")
with col2:
    st.page_link("datasheet.py", label="Data Sheet", icon=":material/table_chart:")
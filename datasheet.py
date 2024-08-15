import streamlit as st
from helper_functions import get_dataset_names, get_df
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd


# title and introduction
st.title("OSAA SMU's Data Sheet")

st.markdown("The SMU's Data Sheet allows for the automation of excel sheet processes and analysis with *Mitosheet*.")

# find and choose a dataset
st.subheader("Select a Dataset")
st.write("Either search through existing datasets or upload your own dataset as a CSV or Excel file.")


st.markdown("##### Search Datasets")
dataset_names = get_dataset_names(st.session_state.db_path)
df_name = st.selectbox("find a dataset", dataset_names, index=None, placeholder="search datasets...", label_visibility="collapsed")

if df_name is not None:
    df = get_df(st.session_state.db_path, df_name)
else:
    df = None
    st.session_state.report = None


st.markdown("##### Upload a Dataset (CSV or excel)")
uploaded_df = st.file_uploader("Choose a file", type=["csv", "xlsx"], label_visibility="collapsed")

if uploaded_df is not None:
    df_name = uploaded_df.name
    if uploaded_df.name.endswith('.csv'):
        df = pd.read_csv(uploaded_df)
    elif uploaded_df.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_df)


st.success(f"Selected Dataset: {df_name}") 
st.markdown("<hr>", unsafe_allow_html=True)
st.write("")


st.subheader("Mitosheet")
if df is not None:
    new_dfs, code = spreadsheet(df)
else:
    st.write("no dataset selected")
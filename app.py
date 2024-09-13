import streamlit as st
from helper_functions import setup_db
import hmac


# check password
def check_password():
    """
    Returns `True` if the user had the correct password.
    """

    def password_entered():
        """
        Checks whether a password entered by the user is correct.
        """

        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # remove the password
        else:
            st.session_state["password_correct"] = False

    # return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # show input for password.
    col1, col2 = st.columns(2)
    with col1:
        st.image("content/OSAA-Data-logo.svg")


    st.title("SMU's Data App")
    st.markdown("Welcome to the Office of the Speical Advisor to Africa's Strategic Management Unit's Data App. Please enter the app password to access the data app.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("")

    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )

    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()


# create test database
db_path = setup_db()

if 'db_path' not in st.session_state:
    st.session_state.db_path = db_path

# create app pages
home_page = st.Page("home.py", title="Home", icon=":material/home:")
dashboard_page = st.Page("dashboard.py", title="Data Dashboard", icon=":material/analytics:")
wb_dashboard_page = st.Page("wb_dashboard.py", title="WorldBank Data Dashboard", icon=":material/bar_chart:")
sdg_dashboard_page = st.Page("sdg_dashboard.py", title="SDG Data Dashboard", icon=":material/show_chart:")
contradictory_analysis_page = st.Page("check_analysis.py", title="Contradictory Analysis Tool", icon=":material/check:")


# mitosheet_page = st.Page("datasheet.py", title="Data Sheet", icon=":material/table_chart:")
# visualizations_page = st.Page("visualizations.py", title="Data Visualization Tool", icon=":material/insert_chart:")


pg = st.navigation([home_page, dashboard_page, wb_dashboard_page, sdg_dashboard_page, contradictory_analysis_page])
st.set_page_config(page_title="SMU Data App", page_icon=":material/home:", layout="wide")
pg.run()
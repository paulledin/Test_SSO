import streamlit as st
from st_snowauth import snowauth_session

st.markdown("## This (and above) is always seen")
session = snowauth_session()
st.markdown("## This (and below) is only seen after authentication")

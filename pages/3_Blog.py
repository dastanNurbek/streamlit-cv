import streamlit as st

st.set_page_config(
    page_title="Researcher",
    page_icon="🗺",
    layout="wide"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.subheader('Blog')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('./images/photo1714053678.jpeg')
    st.image('./images/photo1714053679.jpeg')
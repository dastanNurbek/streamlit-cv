import streamlit as st

st.set_page_config(
    page_title="Researcher",
    page_icon="🗺",
    layout="wide"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.subheader('Publications')

st.markdown("""
<style>
.big-font {
    font-size:1.5rem !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<a class="big-font" href="https://bulletin-phmath.kaznpu.kz/index.php/ped/article/view/1720">Modeling The Change of Water Volume in Alakol Lake Through Polynomial Regression</a>', unsafe_allow_html=True)

st.write("Published in _Bulletin of the Abai KazNPU, the series of Physical and Mathematical Sciences, 2023_")

st.write("")

st.write("""Water level and water volume monitoring can help identify possible changes of water flow, 
         as well as water volume changes, which can suggest alteration of waterway flow and potential 
         surface level flooding. Satellite altimetry and optical remote sensing are used to obtain water 
         level and water area data of Lake Alakol. The Normalized Difference Water Index is used to calculate 
         water area from Sentinel-2 data series. Hydroweb provides water level data and estimates water area 
         using polynomial regression model.  Heron's formula are used to calculate water volume changes. After 
         results analysis,  seasonal variations of water level and water volume were observed. Water level data 
         from Sentinel-2 and interpolated water level data series from Hydroweb were showed strong relationship 
         with correlation coefficient of 0.78.""")

st.write("")

st.write("""Recommended citation: Нурбекулы, Д., Бейсембекова, М., Маемерова, Г. and Ракишева, З. 2023. 
         MODELING THE CHANGE OF WATER VOLUME IN ALAKOL LAKE THROUGH POLYNOMIAL REGRESSION. 
         Bulletin of the Abai KazNPU, the series of "Physical and Mathematical Sciences". 
         84, 4 (Dec. 2023), 101–108. DOI:https://doi.org/10.51889/2959-5894.2023.84.4.010.""")

st.write("")

st.subheader('Conferences')

st.write("**FARABI ALEMI**, Al-Farabi Kazakh National University")
st.write('Thesis on "Observing long-term NOx trends in Almaty city using satellite retrievals" was published and awarded a third place.')
st.caption("Almaty, 2023")

st.write("")

st.write("**AIAC AUES**, Almaty University of Power Engineering and Telecommunications")
st.write('Participated as a speaker.')
st.caption("Almaty, 2023")

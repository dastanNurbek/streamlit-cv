import streamlit as st

st.set_page_config(
    page_title="Researcher",
    page_icon="🗺",
    layout="wide"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.subheader('Projects')

st.markdown("""
<style>
.big-font {
    font-size:1.5rem !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<a class="big-font" href="https://orbit-explorer.streamlit.app/">Orbit Explorer</a>', unsafe_allow_html=True)

st.write("This application provides user interactivity to explore satellite orbital parameters and visualize its orbit and ground track.")
st.write("")

st.image('./images/project1.png')
st.write("")

st.write("""The orbit is displayed on a 3D sphere representing the Earth using the [pyvista](https://pyvista.org/) library.

The project also includes functionality to display the satellite's ground track on a map using the 
         [matplotlib](https://matplotlib.org/) library and the 
         [cartopy](https://scitools.org.uk/cartopy/docs/latest/) module. 
         The satellite is represented as a red dot on the map, 
         which represents its location over time.""")

st.write("")
st.write("[GitHub](https://github.com/dastanNurbek/orbit-explorer)")
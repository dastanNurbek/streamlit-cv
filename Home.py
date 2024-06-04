import streamlit as st

st.set_page_config(
    page_title="Researcher",
    page_icon="🗺",
    layout="wide"
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

col1, col2 = st.columns([3,8])

with col1:
    st.image('./images/headshot.png', width=120)
    st.write('**Dastan Nurbekuly**')
    st.write('_Earth Observation Researcher_')
    st.write('📍 Almaty, Kazakhstan')
    st.write('🎓 Al-Farabi Kazakh National University')
    st.write('📧 [Email](mailto:dastan.nurbek22@gmail.com)')
    st.write('💼 [LinkedIn](https://www.linkedin.com/in/dastan-nurbekuly-1758362b3/)')

with col2:

    with st.container():
        st.subheader("👋 Hi, I'm Dastan!")

        subcol1, subcol2 = st.columns([2,1])
        with subcol1:
            st.write("👨‍💻 I'm a scholar of Copernicus Master in Digital Earth, in GeoData Science study track.")
            st.write("")
            st.write("🔭 My research interests are Satellite Data applications in Oceanography and Climate Change.")
            st.write("")
            st.write("🌊 I'm currently working on a paper about Wave Climate of Lake Alakol.")
            st.write("")
            st.write("🎮 I'm also interested in making video games in Unity Engine.")
        with subcol2:
            st.image('./images/usgs.jpg')
    st.write("")

    with st.container():
        st.subheader("Experience")

        st.write("🔬 **Junior Researcher**, Al-Farabi Kazakh National University")
        st.write("I got hands-on experience working in research projects. I mostly did data analysis and I also published an article; currently in process of publishing another one.")
        st.caption("Jan 2024 - Present")
        st.caption("Almaty, Kazakhstan")
        st.write("")

        st.write("🖥️ **CS Teacher**, Tamos Education")
        st.write("I taught students Python and C# programming languages, as well as Game Development. We participated in coding competitions and project olympiads.")
        st.caption("Sep 2023 - June 2024")
        st.caption("Almaty, Kazakhstan")
    st.write("")
    
    with st.container():
        st.subheader("Education")

        st.write("🛰️ **Bachelor of Technics and Technologies**, Space Engineering and Technologies")
        st.write("""I learned fundamentals of mathematics, physics and mechanics; 
                 basics of rocket science; concepts and principles of space systems; programming languages; 
                 3d modelling and simulation; processing and analyzing satellite imagery and scientific data; 
                 applying numerical and theoretical research methods to solving scientific and applied problems.""")
        st.caption("Al-Farabi Kazakh National University")
        st.caption("Sep 2019 - June 2023")
        st.write("")

        st.write("🌍 **Master of Science**, GeoData Science")
        st.write("""Haven't yet started""")
        st.caption("Paris Lodron University of Salzburg, Southern Brittany University")
        st.caption("Sep 2024")

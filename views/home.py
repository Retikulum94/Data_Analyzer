import streamlit as st

st.markdown("""
<h1 style='text-align: center; margin-bottom:0; font-size: 3.5rem;'>
Passing-Bablok Analyzer
</h1>
<h4 style='text-align: center; color: gray; margin-top:0; font-size: 2rem;'>
Methodenvergleich im Labor
</h4>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("###")

st.container()

st.info("Bitte wählen Sie eine Funktion:")
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<style>
div.stButton > button,
div.stLinkButton a {
    height: 70px;
    font-size: 24px;
    font-weight: 600;
    border-radius: 12px;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 !important;
}
</style>

""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📊 Passing-Bablok", use_container_width=True):
        st.switch_page("views/passing_bablok2.py")

with col2:
    if st.button("📊 Bland-Altman", use_container_width=True):
        st.switch_page("views/bland_altman2.py")

with col3:
    st.link_button("📁 Verlauf", url="https://drive.switch.ch/index.php/s/9UOKqhPaeV4UsVN", use_container_width=True)

with col4:
    if st.button("❓ Hilfe", use_container_width=True):
        st.switch_page("views/Benutzeranleitung_1.py")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.caption("Einfach. Schnell. Verständlich.")

st.markdown("##### Entwickelt von")

st.markdown ("""
- Dennis Bailer (baileden@students.zhaw.ch)
- David Brunner (brunndav@students.zhaw.ch)
- Frochaux Noémie (frochnoe@students.zhaw.ch)
- Vagias Dimitrios (vagiadim@students.zhaw.ch)
             
im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW.
""")
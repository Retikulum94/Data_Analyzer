import streamlit as st

st.markdown("""
<h1 style='text-align: center; margin-bottom:0;'>
Passing-Bablok Analyzer
</h1>
<h4 style='text-align: center; color: gray; margin-top:0;'>
Methodenvergleich im Labor
</h4>
""", unsafe_allow_html=True)

st.markdown("###")

st.container()

st.info("Bitte wählen Sie eine Funktion:")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("📊 Neue Analyse", use_container_width=True)

with col2:
    st.button("📁 Verlauf", use_container_width=True)

with col3:
    st.button("❓ Hilfe", use_container_width=True)

st.markdown("---")
st.caption("Einfach. Schnell. Verständlich.")

st.markdown ("Diese App wurde von " \
"Dennis Bailer (Baileden@students.zhaw.ch)" \
"- David Brunner (brunndav@students.zhaw.ch)" \
"- Frochaux Noémie (frochnoe@students.zhaw.ch)" \
"- Vagias Dimitrios (vagiadim@students.zhaw.ch)" \
"im Rahmen des Moduls 'BMLD Informatik 2' an der ZHAW entwickelt .")
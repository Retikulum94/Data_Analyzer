import streamlit as st

st.markdown("""

<style>

    .block-box {

        background: #f8f9fa;

        border: 1px solid #e0e0e0;

        border-radius: 14px;

        padding: 20px 24px;

        margin-bottom: 18px;

    }

    .block-box h4 {

        margin: 0 0 10px 0;

        font-size: 1.3rem;

        font-weight: 600;

        color: #111827;

    }

    .block-box p {

        margin: 0;

        font-size: 1.05rem;

        color: #4b5563;

        line-height: 1.8;

    }

</style>

""", unsafe_allow_html=True)

st.markdown("""

<h1 style='text-align: center; margin-bottom: 0; font-size: 3.5rem;'>
Passing-Bablok-Verfahren

</h1>

<h3 style='text-align: center; color: #6c757d; margin-top: 0;'>

Methodenvergleich in der Labordiagnostik

</h3>

""", unsafe_allow_html=True)
st.markdown("""

Das Passing-Bablok-Verfahren ist eine **nicht-parametrische Regressionsmethode**,
die verwendet wird, um zwei Messmethoden miteinander zu vergleichen, zum Beispiel
eine neue Labormethode mit einer etablierten Referenzmethode.

""")

st.divider()

st.subheader("Grundidee:")

st.markdown("""
<div class="block-box">
    <h4>Was wird verglichen?</h4>
    <p>Dieselbe Probe wird mit zwei verschiedenen Methoden gemessen. Die Ergebnisse werden 
    gegenübergestellt, um zu prüfen, ob die Methoden austauschbar sind also ob sie 
    systematisch oder proportional voneinander abweichen.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="block-box">
    <h4>Kein Messfehler wird ignoriert</h4>
    <p>Anders als bei der gewöhnlichen linearen Regression geht das Passing-Bablok-Verfahren 
    davon aus, dass <em>beide</em> Methoden Messfehler haben. Keine Methode gilt als 
    „perfekte Referenz".</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="block-box">
    <h4>Nicht-parametrisch</h4>
    <p>Die Methode macht keine Annahmen über die Normalverteilung der Daten und ist damit 
    robust gegenüber Ausreissern und nicht-normalverteilten Messwerten.</p>
</div>
""", unsafe_allow_html=True)

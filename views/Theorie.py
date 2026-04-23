import streamlit as st

st.markdown("""
    <style>
        .block-box {
            background: #f8f9fa;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 16px 20px;
            margin-bottom: 12px;
        }
        .block-box h4 {
            margin: 0 0 6px 0;
            font-size: 15px;
            color: #111;
        }
        .block-box p {
            margin: 0;
            font-size: 14px;
            color: #555;
            line-height: 1.7;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Passing-Bablok-Verfahren")
st.caption("Methodenvergleich in der Labordiagnostik")

st.markdown("""
Das Passing-Bablok-Verfahren ist eine **nicht-parametrische Regressionsmethode**, 
die verwendet wird, um zwei Messmethoden miteinander zu vergleichen, zum Beispiel 
eine neue Labormethode mit einer etablierten Referenzmethode.
""")

st.divider()

st.subheader("Grundidee")

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

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



st.markdown("""
<h1 style='text-align: center; margin-bottom: 0; font-size: 3.5rem;'>
Bland-Altman-Analyse
</h1>
<h3 style='text-align: center; color: #6c757d; margin-top: 0;'>
Übereinstimmung zweier Messmethoden grafisch beurteilen
</h3>
""", unsafe_allow_html=True)

st.markdown("""
Die Bland-Altman-Analyse ist eine **grafische Methode zur Beurteilung der Übereinstimmung**
zwischen zwei Messmethoden. Statt eine Korrelation zu berechnen, werden die
**Differenzen** der Messwertepaare gegen ihre **Mittelwerte** aufgetragen.
""")

st.divider()

st.subheader("Grundidee:")

st.markdown("""
<div class="block-box">
    <h4>Was wird dargestellt?</h4>
    <p>Für jedes Messpaar wird die Differenz (Methode A − Methode B) gegen den Mittelwert
    beider Messungen geplottet. So wird sichtbar, ob und wie stark die Methoden voneinander
    abweichen – über den gesamten Messbereich hinweg.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="block-box">
    <h4>Limits of Agreement</h4>
    <p>Das Verfahren berechnet den <em>Bias</em> (mittlere Differenz) sowie die
    <em>Limits of Agreement</em> (Bias ± 1,96 SD). Diese Grenzen zeigen, in welchem
    Bereich 95 % der Differenzen liegen – entscheidend für die klinische Beurteilung.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="block-box">
    <h4>Grafik statt Korrelation</h4>
    <p>Eine hohe Korrelation bedeutet nicht zwingend gute Übereinstimmung. Die
    Bland-Altman-Methode macht systematische und zufällige Abweichungen direkt
    sichtbar – und vermeidet so einen häufigen Interpretationsfehler.</p>
</div>
""", unsafe_allow_html=True)


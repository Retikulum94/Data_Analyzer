import streamlit as st

st.set_page_config(page_title="Benutzeranleitung - Passing-Bablok Analyzer", layout="wide")

# Custom CSS für bessere Lesbarkeit
st.markdown("""
    <style>
    .guide-section {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #1f77b4;
    }
    .step-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid #2ca02c;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid #ff9800;
    }
    .example-box {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-family: monospace;
        overflow-x: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Titel
st.title("📚 Benutzeranleitung: Passing-Bablok Analyzer")
st.markdown("---")

# Inhaltsverzeichnis
st.sidebar.title("📑 Inhaltsverzeichnis")
page = st.sidebar.radio("Wähle einen Bereich:", [
    "Übersicht",
    "CSV vorbereiten",
    "Datei hochladen",
    "Einstellungen",
    "Ergebnisse interpretieren",
    "Häufig gestellte Fragen"
])

# ==================== ÜBERSICHT ====================
if page == "Übersicht":
    st.header("🎯 Was ist der Passing-Bablok Analyzer?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        Der **Passing-Bablok Analyzer** ist ein statistisches Werkzeug, das zwei verschiedene 
        Methoden zur linearen Regressionsanalyse vergleicht:
        
        ### 📊 Die zwei Methoden
        
        **1. Least-Squares Methode**
        - Klassische lineare Regression
        - Minimiert die Fehlerquadrate
        - Kann durch Ausreißer verzerrt werden
        
        **2. Passing-Bablok Methode**
        - Robuste Alternative zur Least-Squares
        - Symmetrisch (keine Unterscheidung zwischen x und y)
        - Weniger empfindlich gegenüber Ausreißern
        - Ideal für Vergleiche zwischen Messmethoden
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Anwendungsbeispiele
        
        - Vergleich von zwei Messinstrumenten
        - Validierung neuer Messmethoden
        - Medizinische Laboranalysen
        - Qualitätskontrolle
        - Kalibrationsvergleiche
        
        ### 📈 Was erhalte ich?
        
        - Vergleich beider Regressionsmethoden
        - Steigungskoeffizient (Slope)
        - Achsenabschnitt (Intercept)
        - Konfidenzintervalle
        - Visualisierung als Grafik
        - Korrelationskoeffizient
        """)
    
    st.markdown("---")
    st.markdown("""
    <div class="guide-section">
    <h3>✨ Kurzzusammenfassung der Schritte</h3>
    <ol>
        <li><strong>CSV vorbereiten:</strong> Datei aus Excel exportieren</li>
        <li><strong>Datei hochladen:</strong> CSV in die App laden</li>
        <li><strong>Spalten wählen:</strong> X- und Y-Achse definieren</li>
        <li><strong>Ergebnisse ansehen:</strong> Grafiken und Statistiken interpretieren</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# ==================== CSV VORBEREITEN ====================
elif page == "CSV vorbereiten":
    st.header("📋 Schritt 1: CSV-Datei korrekt vorbereiten")
    
    st.markdown("""
    Eine korrekt formatierte CSV-Datei ist essentiell für die Analyse. 
    Folge diesen Schritten, um deine Daten richtig zu exportieren.
    """)
    
    st.subheader("🔄 Von Excel zu CSV")
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 1: Excel-Datei öffnen</h4>
    <p>Öffne deine Excel-Datei mit den Messdaten. Die Datei sollte zwei numerische 
    Spalten enthalten: eine Referenzmessung und eine Testmessung.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 2: Daten kontrollieren</h4>
    <p>Überprüfe folgende Punkte:</p>
    <ul>
        <li>✅ Erste Zeile enthält Spaltenüberschriften</li>
        <li>✅ Mindestens zwei numerische Spalten vorhanden</li>
        <li>✅ Keine leeren Zeilen oder Spalten am Anfang</li>
        <li>✅ Keine Texte in Zahlenspalten (außer in der Kopfzeile)</li>
        <li>✅ Dezimaltrennzeichen ist Punkt (.) statt Komma (,)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 3: Speichern als CSV</h4>
    <ol>
        <li>Klicke auf <strong>Datei → Speichern unter...</strong></li>
        <li>Wähle den Speicherort</li>
        <li>Gib einen aussagekräftigen Namen ein (z.B. "Messvergleich_2024")</li>
        <li>Ändere das Dateiformat zu <strong>CSV UTF-8 (.csv)</strong></li>
        <li>Klicke auf <strong>Speichern</strong></li>
    </ol>
    <p><em>Hinweis: Wähle "CSV UTF-8", nicht "CSV" oder "CSV (Alt)"</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📊 Datenformat-Anforderungen")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### ✅ Korrektes Format")
        st.markdown("""
        ```
        Referenz,Test
        10.5,10.2
        12.3,12.1
        15.7,15.9
        18.2,18.0
        20.5,20.7
        ```
        """)
    
    with col2:
        st.markdown("#### ❌ Fehler vermeiden")
        st.markdown("""
        ```
        Referenz, Test
        10,5    | 10,2   (Komma statt Punkt)
        
        12.3    | 12.1
        Text    | 15.9   (Text statt Zahl)
        
        20.5    | 20.7
        ```
        """)
    
    st.markdown("""
    <div class="warning-box">
    <h4>⚠️ Häufige Fehler</h4>
    <ul>
        <li><strong>Dezimaltrennzeichen:</strong> Verwende einen Punkt (.) statt Komma (,)</li>
        <li><strong>Leerzeichen:</strong> Keine Leerzeichen nach Spaltennamen</li>
        <li><strong>Leere Zellen:</strong> Alle Messungen sollten beide Werte haben</li>
        <li><strong>Tausendertrennzeichen:</strong> Entferne alle Punkte als Tausendertrennzeichen</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔍 Beispiel: Schritt-für-Schritt")
    
    with st.expander("📸 Detailliertes Beispiel mit Screenshots-Text"):
        st.markdown("""
        **Ausgangssituation:** Du hast eine Excel-Datei mit Messwerten von zwei Geräten.
        
        **Excel-Inhalt:**
        | Gerät A | Gerät B |
        |---------|---------|
        | 10.5    | 10.2    |
        | 12.3    | 12.1    |
        | 15.7    | 15.9    |
        
        **So speicherst du richtig:**
        1. Klicke: Datei → Speichern unter
        2. Wähle: Format = "CSV UTF-8 (.csv)"
        3. Dateiname: "Messvergleich.csv"
        4. Speichern klicken
        
        **Fertig!** Die CSV-Datei ist jetzt bereit zum Hochladen.
        """)

# ==================== DATEI HOCHLADEN ====================
elif page == "Datei hochladen":
    st.header("📤 Schritt 2: CSV-Datei hochladen")
    
    st.markdown("""
    Hier erfährst du, wie du deine vorbereitete CSV-Datei in den Analyzer hochlädst.
    """)
    
    st.subheader("🚀 Upload-Anleitung")
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 1: Zur Analyzer-Seite gehen</h4>
    <p>Navigiere zur Seite "📊 Analyzer" in der linken Menüleiste.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 2: CSV-Datei hochladen</h4>
    <p>Du siehst oben auf der Seite die Upload-Box mit der Aufschrift 
    <strong>"CSV-Datei hochladen"</strong>.</p>
    <ol>
        <li>Klicke auf die Upload-Box oder auf "Browse files"</li>
        <li>Wähle deine vorbereitete CSV-Datei</li>
        <li>Warte, bis die Datei verarbeitet wurde</li>
        <li>Du siehst eine grüne Meldung "✅ Datei geladen! (X Zeilen)"</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 3: Daten-Vorschau ansehen</h4>
    <p>Nach dem Upload wird automatisch eine Vorschau der ersten 10 Zeilen angezeigt.
    Überprüfe hier, ob die Daten korrekt geladen wurden:</p>
    <ul>
        <li>✅ Spaltenüberschriften sind korrekt</li>
        <li>✅ Zahlenwerte sind numerisch und nicht als Text</li>
        <li>✅ Die Anzahl der Zeilen ist korrekt</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✅ Upload erfolgreich - Was kommt danach?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Nach erfolgreichem Upload:**
        
        1. ✅ Datei wird verarbeitet
        2. ✅ Alle numerischen Spalten werden erkannt
        3. ✅ Vorschau wird angezeigt
        4. ✅ Du kannst Spalten auswählen
        """)
    
    with col2:
        st.markdown("""
        **Danach gehts weiter mit:**
        
        1. 👉 Wähle X-Achse (Referenz)
        2. 👉 Wähle Y-Achse (Test)
        3. 👉 Ergebnisse anschauen
        4. 👉 Statistiken interpretieren
        """)
    
    st.markdown("""
    <div class="warning-box">
    <h4>⚠️ Häufige Upload-Fehler</h4>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("❌ Fehler: 'Mindestens 2 numerische Spalten erforderlich'"):
        st.markdown("""
        **Problem:** Die App findet zu wenige Zahlenspalten.
        
        **Lösungen:**
        - CSV-Datei nochmal kontrollieren: Enthält sie zwei Zahlenspalten?
        - Sind alle Werte wirklich Zahlen? (keine Anführungszeichen, keine Buchstaben)
        - Dezimaltrennzeichen: Nutze Punkt (.) statt Komma (,)
        - Datei neu speichern und erneut hochladen
        """)
    
    with st.expander("❌ Fehler: 'Fehler beim Einlesen der Datei'"):
        st.markdown("""
        **Problem:** Das Dateiformat ist falsch oder beschädigt.
        
        **Lösungen:**
        - Stelle sicher, dass du "CSV UTF-8" speicherst, nicht "CSV" oder andere Formate
        - Öffne die CSV-Datei im Editor und prüfe das Format
        - Speichere die Datei nochmals als CSV
        - Probiere einen anderen Dateinamen ohne Sonderzeichen
        """)
    
    with st.expander("❌ Fehler: 'Nicht genug Datenpunkte nach Entfernung von NaN-Werten'"):
        st.markdown("""
        **Problem:** Die Datei hat zu viele leere Zellen.
        
        **Lösungen:**
        - Überprüfe die Vorschau der Daten
        - Stelle sicher, dass beide Messwerte für jede Zeile vorhanden sind
        - Entferne leere Zeilen in Excel vor dem Export
        - Du brauchst mindestens 2 gültige Datenpunkte
        """)

# ==================== EINSTELLUNGEN ====================
elif page == "Einstellungen":
    st.header("⚙️ Schritt 3: Einstellungen und Spaltenauswahl")
    
    st.markdown("""
    Nach dem Upload wählst du deine Messwertespalten aus. Hier erklären wir, 
    wie das funktioniert und was die Optionen bedeuten.
    """)
    
    st.subheader("📊 Spaltenauswahl")
    
    st.markdown("""
    <div class="step-box">
    <h4>X-Achse auswählen (Referenzmessung)</h4>
    <p>Dies ist normalerweise dein Referenzmessgerät oder die etablierte Messmethode.</p>
    <ul>
        <li>Die "sichere" oder anerkannte Messmethode</li>
        <li>Oft auch als "Gold Standard" bekannt</li>
        <li>Beispiel: Laborgerät, älteres bewährtes Instrument</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Y-Achse auswählen (Testmessung)</h4>
    <p>Dies ist normalerweise die neue oder zu validierende Messmethode.</p>
    <ul>
        <li>Die Methode, die du validieren möchtest</li>
        <li>Ein neues Messgerät</li>
        <li>Beispiel: Neues Messgerät, alternative Methode</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⚠️ Wichtig: X und Y müssen unterschiedlich sein")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ✅ Korrekt
        - X-Achse: "Gerät A"
        - Y-Achse: "Gerät B"
        
        Jetzt wird der Vergleich durchgeführt.
        """)
    
    with col2:
        st.markdown("""
        #### ❌ Falsch
        - X-Achse: "Gerät A"
        - Y-Achse: "Gerät A"
        
        Du wirst eine Warnung sehen:
        ⚠️ "Wähle zwei unterschiedliche Spalten!"
        """)
    
    st.subheader("🔧 Automatische Datenbereinigung")
    
    st.markdown("""
    Die App führt automatisch folgende Schritte durch:
    
    1. **NaN-Werte entfernen:** Leere Zellen oder ungültige Werte werden ignoriert
    2. **Formatkonvertierung:** Alle Werte werden in Dezimalzahlen konvertiert
    3. **Validierung:** Es wird überprüft, dass mindestens 2 gültige Datenpunkte vorhanden sind
    
    Du musst dich darum nicht selbst kümmern - alles läuft automatisch ab!
    """)
    
    st.subheader("📝 Beispiel: Schritt-für-Schritt")
    
    st.markdown("""
    **Szenario:** Du möchtest ein neues Blutzuckermessgerät validieren.
    
    **Deine Daten:**
    | Referenzgerät | Neues Gerät |
    |---------------|------------|
    | 120           | 118        |
    | 145           | 147        |
    | 98            | 100        |
    
    **Deine Auswahl:**
    - X-Achse: "Referenzgerät" (etablierte Messung)
    - Y-Achse: "Neues Gerät" (zu validieren)
    
    **Ergebnis:** Der Analyzer vergleicht automatisch beide Methoden!
    """)

# ==================== ERGEBNISSE INTERPRETIEREN ====================
elif page == "Ergebnisse interpretieren":
    st.header("📊 Schritt 4: Ergebnisse verstehen und interpretieren")
    
    st.markdown("""
    Nach der Analyse siehst du Grafiken und Statistiken. 
    Hier erklären wir, was sie bedeuten.
    """)
    
    st.subheader("📈 Die Vergleichsgrafik")
    
    st.markdown("""
    Die Grafik zeigt zwei Regressionsllinien in einem Scatterplot:
    
    - **Rote Linie:** Least-Squares Regression
    - **Blaue Linie:** Passing-Bablok Regression
    - **Punkte:** Deine Messwerte
    
    **Was bedeutet das?**
    - Wenn beide Linien sehr ähnlich sind: Beide Methoden funktionieren gut
    - Wenn sie stark abweichen: Passing-Bablok ist robuster (bei Ausreißern)
    """)
    
    st.subheader("📊 Die wichtigsten Statistiken")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### Anzahl Datenpunkte
        **Was ist das?** Die Anzahl der gültigen Messungen
        
        **Was ist gut?**
        - Je mehr Datenpunkte, desto zuverlässiger
        - Mindestens 20-30 Punkte empfohlen
        - Mindestens 2 erforderlich
        """)
    
    with col2:
        st.markdown("""
        #### Korrelation
        **Was ist das?** Misst, wie gut die Werte zusammenhängen
        
        **Was ist gut?**
        - Wert zwischen -1 und +1
        - 1 = perfekte positive Korrelation
        - > 0.95 = sehr gut
        - > 0.90 = gut
        - < 0.80 = fragwürdig
        """)
    
    st.subheader("🔍 Regressionskoeffizienten")
    
    st.markdown("""
    <div class="guide-section">
    <h4>Slope (Steigung)</h4>
    <p><strong>Bedeutung:</strong> Der Proportionalitätsfaktor zwischen den beiden Messungen</p>
    <ul>
        <li><strong>Ideal:</strong> Slope ≈ 1.0 (beide Methoden sind proportional)</li>
        <li><strong>Beispiel Slope = 1.05:</strong> Neue Methode ist 5% höher</li>
        <li><strong>Beispiel Slope = 0.95:</strong> Neue Methode ist 5% niedriger</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="guide-section">
    <h4>Intercept (Achsenabschnitt)</h4>
    <p><strong>Bedeutung:</strong> Der systematische Versatz zwischen den Methoden</p>
    <ul>
        <li><strong>Ideal:</strong> Intercept ≈ 0.0 (keine Verschiebung)</li>
        <li><strong>Beispiel Intercept = 5:</strong> Neue Methode ist systematisch 5 Einheiten höher</li>
        <li><strong>Beispiel Intercept = -2:</strong> Neue Methode ist systematisch 2 Einheiten niedriger</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="guide-section">
    <h4>Konfidenzintervalle (95% CI)</h4>
    <p><strong>Bedeutung:</strong> Der Bereich, in dem der wahre Wert mit 95% Sicherheit liegt</p>
    <ul>
        <li>Gibt die Genauigkeit der Schätzung an</li>
        <li>Schmale Intervalle = Präzise Schätzung</li>
        <li>Breite Intervalle = Weniger genaue Schätzung</li>
        <li>Wenn beide Methoden ähnliche Intervalle haben: Gut!</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✅ Was bedeutet ein gutes Ergebnis?")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **Ausgezeichnet:**
        - ✅ Korrelation > 0.95
        - ✅ Slope 0.98 - 1.02
        - ✅ Intercept sehr nah bei 0
        - ✅ Beide Linien fast identisch
        """)
    
    with col2:
        st.markdown("""
        **Prüfwert:**
        - ⚠️ Korrelation 0.90 - 0.95
        - ⚠️ Slope 0.95 - 1.05
        - ⚠️ Linien unterscheiden sich
        - ⚠️ Ausreißer sichtbar
        """)
    
    st.subheader("🔴 Was bedeutet ein schlechtes Ergebnis?")
    
    st.markdown("""
    <div class="warning-box">
    <h4>Probleme erkennen:</h4>
    <ul>
        <li><strong>Korrelation < 0.80:</strong> Die Methoden messen Unterschiedliches</li>
        <li><strong>Slope >> 1 oder << 1:</strong> Systematischer Unterschied</li>
        <li><strong>Linien stark unterschiedlich:</strong> Ausreißer beeinflussen LS-Methode stark</li>
        <li><strong>Viele Punkte weit entfernt:</strong> Möglicherweise Messfehler</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Beispiel: Interpretation")
    
    with st.expander("📊 Szenario: Blutdruckmessgeräte"):
        st.markdown("""
        **Daten:** Vergleich eines neuen digitalen mit einem analogen Blutdruckmessgerät
        
        **Ergebnisse:**
        - Korrelation: 0.97 ✅
        - Least-Squares Slope: 1.02
        - Passing-Bablok Slope: 1.00
        - Intercept: 0.5 mmHg
        
        **Interpretation:**
        - Sehr gute Korrelation → Methoden messen das Gleiche
        - Sehr ähnliche Slopes → Beide gut
        - Minimaler Intercept → Kein systematischer Fehler
        - **Fazit:** Neue Methode validiert! ✅
        """)
    
    with st.expander("📊 Szenario: Glucosemessgeräte (Problematisch)"):
        st.markdown("""
        **Daten:** Vergleich von zwei Glucosemessgeräten
        
        **Ergebnisse:**
        - Korrelation: 0.82 ⚠️
        - Least-Squares Slope: 1.15
        - Passing-Bablok Slope: 1.08
        - Intercept: 15 mg/dL
        
        **Interpretation:**
        - Akzeptable aber nicht ideale Korrelation
        - Unterschiedliche Slopes → Systematischer Fehler
        - Großer Intercept → Neue Methode misst ~15 mg/dL höher
        - **Fazit:** Geräte stimmen nicht überein, Kalibrierung nötig! ⚠️
        """)

# ==================== FAQ ====================
else:  # "Häufig gestellte Fragen"
    st.header("❓ Häufig gestellte Fragen (FAQ)")
    
    st.subheader("Allgemeine Fragen")
    
    with st.expander("Wann sollte ich Passing-Bablok nutzen statt Least-Squares?"):
        st.markdown("""
        **Passing-Bablok ist besser, wenn:**
        - Du zwei verschiedene Messmethoden vergleichst
        - Ausreißer in den Daten vorhanden sind
        - Beide Variablen Messfehler haben (nicht nur eine)
        - Du Geräte validieren möchtest
        
        **Least-Squares ist besser, wenn:**
        - Du eine Variable vorhersagen möchtest (z.B. Preis aus Größe)
        - Es klare Abhängigkeiten gibt
        - Nur eine Variable fehlerhaft ist
        """)
    
    with st.expander("Wie viele Datenpunkte brauche ich?"):
        st.markdown("""
        **Minimum:** 2 Datenpunkte (App-Anforderung)
        
        **Empfohlen:**
        - 20-30 Punkte für grundlegende Analysen
        - 50+ Punkte für robuste Ergebnisse
        - 100+ Punkte für hochwertige Validierungen
        
        **Je mehr Daten, desto besser die Ergebnisse!**
        """)
    
    with st.expander("Was sind NaN-Werte und warum werden sie entfernt?"):
        st.markdown("""
        **NaN = "Not a Number" (Keine Zahl)**
        
        Beispiele für NaN-Werte:
        - Leere Zellen
        - Fehlerhafte Messungen
        - Nicht-numerische Werte (z.B. "ERROR", "N/A")
        
        **Warum werden sie entfernt?**
        - Regressionsmethoden können nicht mit fehlenden Werten rechnen
        - Es ist korrekt, nur vollständige Datenpunkte zu nutzen
        - Ein Datenpunkt ist nur gültig, wenn beide Messwerte vorhanden sind
        """)
    
    st.subheader("Technische Fragen")
    
    with st.expander("Was ist UTF-8 und warum sollte ich das wählen?"):
        st.markdown("""
        **UTF-8** ist eine Zeichenkodierung, die alle Symbole richtig darstellt.
        
        **Warum UTF-8?**
        - Funktioniert auf allen Computern
        - Unterstützt Sonderzeichen und Umlaute (ä, ö, ü, etc.)
        - Das App bevorzugt dieses Format
        
        **Andere Formate:**
        - "CSV (Alt)" oder nur "CSV" können zu Problemen führen
        - Sonderzeichen werden falsch angezeigt
        - Dezimaltrennzeichen können falsch sein
        """)
    
    with st.expander("Punkt oder Komma als Dezimaltrennzeichen?"):
        st.markdown("""
        **Nutze immer Punkt (.)**
        
        Korrekt: 12.5, 23.45, 100.1
        Falsch: 12,5, 23,45, 100,1
        
        **In Excel auf Deutsch:**
        1. Gehe in Einstellungen
        2. Region: Wähle "English (USA)"
        3. Speichern als CSV - jetzt wird Punkt verwendet
        
        Oder nutze "Finden & Ersetzen":
        - Finde: ,
        - Ersetze: .
        """)
    
    with st.expander("Kann ich mehrere Dateien analysieren?"):
        st.markdown("""
        **Ja!** Es gibt zwei Optionen:
        
        **Option 1: Nacheinander**
        - Lade eine Datei, analysiere sie
        - Lade dann eine neue Datei hoch
        
        **Option 2: Alle zusammenfassen**
        - Kombiniere mehrere Excel-Dateien in einer Datei
        - Alle Messungen müssen die gleichen Spalten haben
        - Dann als eine CSV exportieren
        """)
    
    st.subheader("Interpretationsfragen")
    
    with st.expander("Warum unterscheiden sich die beiden Linien?"):
        st.markdown("""
        **Die Linien unterscheiden sich, wenn:**
        
        1. **Ausreißer vorhanden:** Least-Squares wird davon beeinflusst
           - Passing-Bablok ist robuster
        
        2. **Unterschiedliche Fehlerstrukturen:** Wenn eine Methode fehleranfällig ist
           - Passing-Bablok behandelt dies symmetrisch
        
        3. **Kleine Stichprobe:** Bei wenigen Datenpunkten größere Unterschiede
        
        **Große Unterschiede sind OK** - das zeigt, dass Passing-Bablok robuster ist!
        """)
    
    with st.expander("Meine Korrelation ist 0.92 - ist das gut?"):
        st.markdown("""
        **Kontext ist wichtig!**
        
        **0.92 ist:**
        - ✅ Sehr gut für medizinische Geräte
        - ✅ Sehr gut für Labormessungen
        - ✅ Akzeptabel für Screenings
        - ⚠️ Grenzwert für kritische Messungen
        - ❌ Nicht ausreichend für hochpräzise Kalibrationen
        
        **Branchenstandards:**
        - Klinische Chemie: > 0.95 erwartet
        - Hämatologie: > 0.93 erwartet
        - Kohortenstudien: > 0.85 akzeptabel
        """)
    
    with st.expander("Mein Slope ist 1.25 - was bedeutet das?"):
        st.markdown("""
        **Slope 1.25 bedeutet:**
        
        Die neue Methode misst 25% höher als die Referenz.
        
        **Beispiel mit konkreten Zahlen:**
        - Referenz misst: 100
        - Neue Methode misst: 125
        - Unterschied: 25%
        
        **Ist das ein Problem?**
        - Kommt auf die Anwendung an
        - < 5% Unterschied: Austauschbar
        - 5-10% Unterschied: Systematischer Fehler, aber nutzbar
        - > 10% Unterschied: Möglicherweise Kalibrierung nötig
        """)
    
    st.subheader("Datenvorbereitung - Häufige Fragen")
    
    with st.expander("Kann ich die CSV-Datei in TextEdit/Editor öffnen und bearbeiten?"):
        st.markdown("""
        **Ja, aber sei vorsichtig!**
        
        Wenn du TextEdit/Editor nutzt:
        1. Öffne die CSV-Datei
        2. Bearbeite die Werte
        3. Speichere sie (Format muss CSV bleiben)
        
        **Besser:** Nutze Excel oder Calc
        - Übersichtlicher
        - Weniger Fehler
        - Leichtere Formatierung
        """)
    
    with st.expander("Muss die erste Zeile Spaltennamen haben?"):
        st.markdown("""
        **Ja, die App benötigt Spaltennamen in der ersten Zeile!**
        
        ✅ Korrekt:
        ```
        Methode_A,Methode_B
        10.5,10.2
        12.3,12.1
        ```
        
        ❌ Falsch:
        ```
        10.5,10.2
        12.3,12.1
        ```
        
        **Spaltennamen können sein:**
        - "Gerät A" und "Gerät B"
        - "Referenz" und "Test"
        - "Methode 1" und "Methode 2"
        - Egal was - Hauptsache aussagekräftig
        """)
    
    with st.expander("Kann ich Formeln in Excel vor dem Export verwenden?"):
        st.markdown("""
        **Ja!** Aber mit Vorsicht:
        
        ✅ Okay:
        - Formatierung
        - Berechnungen (z.B. Mittelwerte)
        - Runden (z.B. auf 2 Dezimalstellen)
        - Filterung (nur bestimmte Zeilen)
        
        ⚠️ Problematisch:
        - Abhängige Zellen (können "#REF" zeigen beim Export)
        - Externe Verknüpfungen
        - Bedingte Formatierung
        
        **Tipp:** Nach Berechnung die Werte → Werte einfügen, 
        dann als CSV speichern.
        """)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="guide-section">
    <h3>💡 Noch Fragen?</h3>
    <p>Wenn du auf ein Problem stößt:</p>
    <ol>
        <li>Schaue in dieser Anleitung nach (nutze die Suche)</li>
        <li>Überprüfe deine CSV-Datei nochmal</li>
        <li>Versuche die Schritte in dieser Anleitung zu wiederholen</li>
        <li>Falls weiterhin Probleme: Überprüfe die Fehlermeldung in der App</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 30px;'>
<p><small>📖 Benutzeranleitung für Passing-Bablok Analyzer | Version 1.0</small></p>
<p><small>Zuletzt aktualisiert: 2024</small></p>
</div>
""", unsafe_allow_html=True)

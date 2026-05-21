import streamlit as st

st.markdown("""
    <style>
    .guide-section {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #1f77b4;
        color: #000;
    }
    .step-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid #2ca02c;
        color: #000;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid #ff9800;
        color: #000;
    }
    .example-box {
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-family: monospace;
        overflow-x: auto;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""

<h1 style='text-align: center; margin-bottom: 0; font-size: 3.5rem;'>
Benutzeranleitung

</h1>

<h3 style='text-align: center; color: #6c757d; margin-top: 0;'>

Passing-Bablok & Bland-Altman Analyzer

</h3>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Analyzer-Auswahl in der Sidebar
st.sidebar.title(" Analyzertyp")
analyzer_type = st.sidebar.radio("Wähle den Analyzer:", [
    "Passing-Bablok",
    "Bland-Altman"
])

st.sidebar.markdown("---")
st.sidebar.title(" Inhaltsverzeichnis")
page = st.sidebar.radio("Wähle einen Bereich:", [
    "Übersicht",
    "CSV vorbereiten",
    "Datei hochladen",
    "Einstellungen",
    "Ergebnisse interpretieren",
    "Häufig gestellte Fragen"
])


if page == "Übersicht":
    st.header(" Was ist ein Analyzer?")
    
    col1, col2 = st.columns([1, 1])
    
    if analyzer_type == "Passing-Bablok":
        with col1:
            st.markdown("""
            Der **Passing-Bablok Analyzer** ist ein statistisches Werkzeug, das zwei verschiedene 
            Methoden zur linearen Regressionsanalyse vergleicht:
            
            ###  Die zwei Methoden
            
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
            ###  Anwendungsbeispiele
            
            - Vergleich von zwei Messinstrumenten
            - Validierung neuer Messmethoden
            - Medizinische Laboranalysen
            - Qualitätskontrolle
            - Kalibrationsvergleiche
            
            ###  Was erhalte ich?
            
            - Vergleich beider Regressionsmethoden
            - Steigungskoeffizient (Slope)
            - Achsenabschnitt (Intercept)
            - Konfidenzintervalle
            - Visualisierung als Grafik
            - Korrelationskoeffizient
            """)
    else:  # Bland-Altman
        with col1:
            st.markdown("""
            Der **Bland-Altman Analyzer** ist ein statistisches Werkzeug zur Beurteilung 
            der Übereinstimmung zwischen zwei Messmethoden:
            
            ###  Die Bland-Altman Methode
            
            - Analysiert Unterschiede zwischen zwei Methoden
            - Zeigt systematische Fehler (Bias)
            - Berechnet Grenzen der Übereinstimmung
            - Ideal für Methodenvergleiche in der Klinik
            - Nicht-parametrisch und robust
            
            **Unterschied zur Passing-Bablok:**
            - Nicht auf Regression basiert
            - Fokus auf Unterschiede, nicht auf Korrelation
            - Bessere Visualisierung von Abweichungen
            - Standard in medizinischen Validierungen
            """)
        
        with col2:
            st.markdown("""
            ###  Anwendungsbeispiele
            
            - Validierung von Messinstrumenten
            - Medizinische Methodenvergleiche
            - Klinische Laboranalysen
            - Gerätevalidierung
            - Methodenwechsel in der Klinik
            
            ###  Was erhalte ich?
            
            - Bland-Altman Plot (Differenzen vs. Mittelwerte)
            - Mittlere Differenz (Bias)
            - Grenzen der Übereinstimmung (LoA)
            - Standardabweichung der Differenzen
            - Bias-Prozentsätze
            - Detaillierte statistische Kennzahlen
            """)
    
    st.markdown("---")
    
    st.markdown("---")
    st.markdown("""
    <div class="guide-section">
    <h3> Kurzzusammenfassung der Schritte</h3>
    <ol>
        <li><strong>CSV vorbereiten:</strong> Datei aus Excel exportieren</li>
        <li><strong>Datei hochladen:</strong> CSV in die App laden</li>
        <li><strong>Spalten wählen:</strong> Referenz- und Testmessung definieren</li>
        <li><strong>Ergebnisse ansehen:</strong> Grafiken und Statistiken interpretieren</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif page == "CSV vorbereiten":
    st.header(" Schritt 1: CSV-Datei korrekt vorbereiten")
    
    st.markdown("""
    Eine korrekt formatierte CSV-Datei ist essentiell für die Analyse. 
    Folge diesen Schritten, um deine Daten richtig zu exportieren.
    """)
    
    st.subheader(" Von Excel zu CSV")
    
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
        <li> Erste Zeile enthält Spaltenüberschriften</li>
        <li> Mindestens zwei numerische Spalten vorhanden</li>
        <li> Keine leeren Zeilen oder Spalten am Anfang</li>
        <li> Keine Texte in Zahlenspalten (außer in der Kopfzeile)</li>
        <li> Dezimaltrennzeichen ist Punkt (.) statt Komma (,)</li>
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
    
    st.subheader(" Datenformat-Anforderungen")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("####  Korrektes Format")
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
        st.markdown("####  Fehler vermeiden")
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
    <h4> Häufige Fehler</h4>
    <ul>
        <li><strong>Dezimaltrennzeichen:</strong> Verwende einen Punkt (.) statt Komma (,)</li>
        <li><strong>Leerzeichen:</strong> Keine Leerzeichen nach Spaltennamen</li>
        <li><strong>Leere Zellen:</strong> Alle Messungen sollten beide Werte haben</li>
        <li><strong>Tausendertrennzeichen:</strong> Entferne alle Punkte als Tausendertrennzeichen</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader(" Beispiel: Schritt-für-Schritt")
    
    with st.expander(" Detailliertes Beispiel mit Screenshots-Text"):
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

elif page == "Datei hochladen":
    st.header(" Schritt 2: CSV-Datei hochladen")
    
    st.markdown("""
    Hier erfährst du, wie du deine vorbereitete CSV-Datei in den Analyzer hochlädst.
    """)
    
    st.subheader(" Upload-Anleitung")
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 1: Zur Analyzer-Seite gehen</h4>
    <p>Navigiere zur Seite " Analyzer" in der linken Menüleiste.</p>
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
        <li>Du siehst eine grüne Meldung " Datei geladen! (X Zeilen)"</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-box">
    <h4>Schritt 3: Daten-Vorschau ansehen</h4>
    <p>Nach dem Upload wird automatisch eine Vorschau der ersten 10 Zeilen angezeigt.
    Überprüfe hier, ob die Daten korrekt geladen wurden:</p>
    <ul>
        <li> Spaltenüberschriften sind korrekt</li>
        <li> Zahlenwerte sind numerisch und nicht als Text</li>
        <li> Die Anzahl der Zeilen ist korrekt</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader(" Upload erfolgreich - Was kommt danach?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Nach erfolgreichem Upload:**
        
        1.  Datei wird verarbeitet
        2.  Alle numerischen Spalten werden erkannt
        3.  Vorschau wird angezeigt
        4.  Du kannst Spalten auswählen
        """)
    
    with col2:
        st.markdown("""
        **Danach gehts weiter mit:**
        
        1.  Wähle X-Achse (Referenz)
        2.  Wähle Y-Achse (Test)
        3.  Ergebnisse anschauen
        4.  Statistiken interpretieren
        """)
    
    st.markdown("""
    <div class="warning-box">
    <h4> Häufige Upload-Fehler</h4>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander(" Fehler: 'Mindestens 2 numerische Spalten erforderlich'"):
        st.markdown("""
        **Problem:** Die App findet zu wenige Zahlenspalten.
        
        **Lösungen:**
        - CSV-Datei nochmal kontrollieren: Enthält sie zwei Zahlenspalten?
        - Sind alle Werte wirklich Zahlen? (keine Anführungszeichen, keine Buchstaben)
        - Dezimaltrennzeichen: Nutze Punkt (.) statt Komma (,)
        - Datei neu speichern und erneut hochladen
        """)
    
    with st.expander(" Fehler: 'Fehler beim Einlesen der Datei'"):
        st.markdown("""
        **Problem:** Das Dateiformat ist falsch oder beschädigt.
        
        **Lösungen:**
        - Stelle sicher, dass du "CSV UTF-8" speicherst, nicht "CSV" oder andere Formate
        - Öffne die CSV-Datei im Editor und prüfe das Format
        - Speichere die Datei nochmals als CSV
        - Probiere einen anderen Dateinamen ohne Sonderzeichen
        """)
    
    with st.expander(" Fehler: 'Nicht genug Datenpunkte nach Entfernung von NaN-Werten'"):
        st.markdown("""
        **Problem:** Die Datei hat zu viele leere Zellen.
        
        **Lösungen:**
        - Überprüfe die Vorschau der Daten
        - Stelle sicher, dass beide Messwerte für jede Zeile vorhanden sind
        - Entferne leere Zeilen in Excel vor dem Export
        - Du brauchst mindestens 2 gültige Datenpunkte
        """)

elif page == "Einstellungen":
    st.header(" Schritt 3: Einstellungen und Spaltenauswahl")
    
    st.markdown("""
    Nach dem Upload wählst du deine Messwertespalten aus. Hier erklären wir, 
    wie das funktioniert und was die Optionen bedeuten.
    """)
    
    st.subheader(" Spaltenauswahl")
    
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
    
    st.subheader(" Wichtig: X und Y müssen unterschiedlich sein")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ####  Korrekt
        - X-Achse: "Gerät A"
        - Y-Achse: "Gerät B"
        
        Jetzt wird der Vergleich durchgeführt.
        """)
    
    with col2:
        st.markdown("""
        ####  Falsch
        - X-Achse: "Gerät A"
        - Y-Achse: "Gerät A"
        
        Du wirst eine Warnung sehen:
         "Wähle zwei unterschiedliche Spalten!"
        """)
    
    st.subheader(" Automatische Datenbereinigung")
    
    st.markdown("""
    Die App führt automatisch folgende Schritte durch:
    
    1. **NaN-Werte entfernen:** Leere Zellen oder ungültige Werte werden ignoriert
    2. **Formatkonvertierung:** Alle Werte werden in Dezimalzahlen konvertiert
    3. **Validierung:** Es wird überprüft, dass mindestens 2 gültige Datenpunkte vorhanden sind
    
    Du musst dich darum nicht selbst kümmern - alles läuft automatisch ab!
    """)
    
    st.subheader(" Beispiel: Schritt-für-Schritt")
    
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

elif page == "Ergebnisse interpretieren":
    st.header(" Schritt 4: Ergebnisse verstehen und interpretieren")
    
    st.markdown("""
    Nach der Analyse siehst du Grafiken und Statistiken. 
    Hier erklären wir, was sie bedeuten.
    """)
    
    if analyzer_type == "Passing-Bablok":
        st.subheader(" Die Vergleichsgrafik")
        
        st.markdown("""
        Die Grafik zeigt zwei Regressionsllinien in einem Scatterplot:
        
        - **Rote Linie:** Least-Squares Regression
        - **Blaue Linie:** Passing-Bablok Regression
        - **Punkte:** Deine Messwerte
        
        **Was bedeutet das?**
        - Wenn beide Linien sehr ähnlich sind: Beide Methoden funktionieren gut
        - Wenn sie stark abweichen: Passing-Bablok ist robuster (bei Ausreißern)
        """)
        
        st.subheader(" Die wichtigsten Statistiken")
        
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
        
        st.subheader(" Regressionskoeffizienten")
        
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
        
        st.subheader(" Was bedeutet ein gutes Ergebnis?")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Ausgezeichnet:**
            -  Korrelation > 0.95
            -  Slope 0.98 - 1.02
            -  Intercept sehr nah bei 0
            -  Beide Linien fast identisch
            """)
        
        with col2:
            st.markdown("""
            **Prüfwert:**
            -  Korrelation 0.90 - 0.95
            -  Slope 0.95 - 1.05
            -  Linien unterscheiden sich
            -  Ausreißer sichtbar
            """)
        
        st.subheader(" Was bedeutet ein schlechtes Ergebnis?")
        
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
        
        st.subheader(" Beispiel: Interpretation")
        
        with st.expander(" Szenario: Blutdruckmessgeräte"):
            st.markdown("""
            **Daten:** Vergleich eines neuen digitalen mit einem analogen Blutdruckmessgerät
            
            **Ergebnisse:**
            - Korrelation: 0.97 
            - Least-Squares Slope: 1.02
            - Passing-Bablok Slope: 1.00
            - Intercept: 0.5 mmHg
            
            **Interpretation:**
            - Sehr gute Korrelation → Methoden messen das Gleiche
            - Sehr ähnliche Slopes → Beide gut
            - Minimaler Intercept → Kein systematischer Fehler
            - **Fazit:** Neue Methode validiert! 
            """)
        
        with st.expander(" Szenario: Glucosemessgeräte (Problematisch)"):
            st.markdown("""
            **Daten:** Vergleich von zwei Glucosemessgeräten
            
            **Ergebnisse:**
            - Korrelation: 0.82 
            - Least-Squares Slope: 1.15
            - Passing-Bablok Slope: 1.08
            - Intercept: 15 mg/dL
            
            **Interpretation:**
            - Akzeptable aber nicht ideale Korrelation
            - Unterschiedliche Slopes → Systematischer Fehler
            - Großer Intercept → Neue Methode misst ~15 mg/dL höher
            - **Fazit:** Geräte stimmen nicht überein, Kalibrierung nötig! 
            """)
    
    else:  # Bland-Altman
        st.subheader(" Das Bland-Altman Diagramm")
        
        st.markdown("""
        Das Bland-Altman Diagramm zeigt:
        
        - **X-Achse:** Mittelwert der beiden Messungen ((x+y)/2)
        - **Y-Achse:** Differenz zwischen den Messungen (y-x)
        - **Rote horizontale Linie:** Mittlere Differenz (Bias)
        - **Gestrichelte Linien:** Grenzen der Übereinstimmung (LoA)
        - **Punkte:** Einzelne Messpaare
        
        **Was bedeutet das?**
        - Punkte sollten symmetrisch um die mittlere Differenz liegen
        - 95% der Punkte sollten innerhalb der LoA-Linien liegen
        - Keine Trends oder Muster sind ideal
        """)
        
        st.subheader(" Die wichtigsten Statistiken")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Anzahl Datenpunkte
            **Was ist das?** Die Anzahl der Messpaare
            
            **Was ist gut?**
            - Je mehr Datenpunkte, desto zuverlässiger
            - Mindestens 30-50 Punkte empfohlen
            - Mindestens 2 erforderlich
            """)
        
        with col2:
            st.markdown("""
            #### Bias (mittlere Differenz)
            **Was ist das?** Systematischer Fehler zwischen Methoden
            
            **Was ist gut?**
            - Wert sollte nahe bei 0 liegen
            - Negative Werte: Methode 2 misst niedriger
            - Positive Werte: Methode 2 misst höher
            """)
        
        st.subheader(" Grenzen der Übereinstimmung (LoA)")
        
        st.markdown("""
        <div class="guide-section">
        <h4>Limits of Agreement (LoA)</h4>
        <p><strong>Bedeutung:</strong> Bereich, in dem 95% der Unterschiede liegen</p>
        <ul>
            <li><strong>Formel:</strong> Bias ± 1.96 × SD der Differenzen</li>
            <li><strong>Interpretation:</strong> Die meisten Messungen unterscheiden sich um maximal diesen Betrag</li>
            <li><strong>Schmaler Bereich:</strong> Methoden stimmen gut überein</li>
            <li><strong>Breiter Bereich:</strong> Größere Unterschiede zwischen Methoden</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader(" Was bedeutet ein gutes Ergebnis?")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            **Ausgezeichnet:**
            -  Bias nahe bei 0
            -  Enge LoA
            -  Keine Trends im Plot
            -  Alle Punkte innerhalb LoA
            -  Symmetrische Verteilung
            """)
        
        with col2:
            st.markdown("""
            **Prüfwert:**
            -  Bias < 10% des Messbereichs
            -  Breitere LoA akzeptabel
            -  Leichte Trends sichtbar
            -  Wenige Punkte außerhalb LoA
            """)
        
        st.subheader(" Was bedeutet ein schlechtes Ergebnis?")
        
        st.markdown("""
        <div class="warning-box">
        <h4>Probleme erkennen:</h4>
        <ul>
            <li><strong>Großer Bias:</strong> Systematischer Unterschied zwischen Methoden</li>
            <li><strong>Sehr breite LoA:</strong> Methoden stimmen nicht überein</li>
            <li><strong>Trend (Steigung):</strong> Unterschied hängt von Messgröße ab</li>
            <li><strong>Viele Ausreißer:</strong> Zu viele Punkte außerhalb LoA</li>
            <li><strong>Asymmetrische Verteilung:</strong> Nicht-random Unterschiede</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader(" Beispiele: Interpretation")
        
        with st.expander(" Szenario: Pulsmesser-Validierung"):
            st.markdown("""
            **Daten:** Vergleich eines neuen Smartwatch-Pulsmessers mit ECG-Standard
            
            **Ergebnisse:**
            - Bias: 1.2 bpm
            - LoA: [-4.5, 6.9] bpm
            - Anzahl Punkte: 45
            - Trend: Nein
            
            **Interpretation:**
            - Sehr kleiner systematischer Fehler (1.2 bpm)
            - Akzeptable Grenzen der Übereinstimmung
            - 95% der Messungen unterscheiden sich maximal um 6.9 bpm
            - **Fazit:** Smartwatch ist klinisch akzeptabel!
            """)
        
        with st.expander(" Szenario: Blutdruck-Geräte (Problematisch)"):
            st.markdown("""
            **Daten:** Vergleich zweier Blutdruckmessgeräte
            
            **Ergebnisse:**
            - Bias: 8.5 mmHg
            - LoA: [-15.2, 32.2] mmHg
            - Anzahl Punkte: 50
            - Trend: Ja (Steigung erkennbar)
            
            **Interpretation:**
            - Großer systematischer Fehler (8.5 mmHg höher)
            - Sehr breite LoA → Schlechte Übereinstimmung
            - Trend deutet auf Abhängigkeit vom Messniveau hin
            - **Fazit:** Geräte nicht austauschbar, Kalibrierung nötig!
            """)
        
        with st.expander(" Szenario: Laborwert-Analyzer"):
            st.markdown("""
            **Daten:** Vergleich eines neuen mit etabliertem Analyzer
            
            **Ergebnisse:**
            - Bias: 0.3 mg/dL
            - LoA: [-2.1, 2.7] mg/dL
            - Anzahl Punkte: 120
            - Trend: Nein
            
            **Interpretation:**
            - Minimaler Bias
            - Sehr enge LoA
            - Sehr gute Übereinstimmung
            - **Fazit:** Analyzer kann etabliertes Gerät ersetzen!

else:
    st.header(" Häufig gestellte Fragen (FAQ)")
    
    st.subheader("Allgemeine Fragen")
    
    with st.expander("Wann sollte ich Passing-Bablok vs. Bland-Altman nutzen?"):
        st.markdown("""
        **Passing-Bablok verwenden für:**
        - Vergleich von zwei Messmethoden mit Regressionsanalyse
        - Wenn du die Beziehung zwischen Methoden beschreiben möchtest
        - Wenn Ausreißer möglich sind (robuste Methode)
        - Wenn Slope und Intercept wichtig sind
        
        **Bland-Altman verwenden für:**
        - Beurteilung der Übereinstimmung zwischen Methoden
        - Wenn du Grenzen der Übereinstimmung brauchst
        - In klinischen Validierungsstudien (Standard)
        - Wenn du Bias und Variabilität analysieren möchtest
        
        **Kurz gesagt:**
        - **Passing-Bablok:** "Wie korrelieren die Methoden?"
        - **Bland-Altman:** "Stimmen die Methoden überein?"
        """)
    
    if analyzer_type == "Passing-Bablok":
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
        
        **Speziell für Bland-Altman:** Mindestens 30-50 Punkte empfohlen für zuverlässige LoA
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
    
    if analyzer_type == "Bland-Altman":
        st.subheader("Bland-Altman spezifische Fragen")
        
        with st.expander("Was bedeutet Bias und wann ist er akzeptabel?"):
            st.markdown("""
            **Bias:** Der systematische Unterschied zwischen zwei Methoden
            
            **Bedeutung:**
            - Positive Bias: Methode 2 misst im Durchschnitt höher
            - Negative Bias: Methode 2 misst im Durchschnitt niedriger
            - Bias = 0: Keine systematischen Unterschiede
            
            **Wann ist Bias akzeptabel?**
            - < 5% des Messbereichs: Sehr gut
            - 5-10% des Messbereichs: Akzeptabel
            - > 10% des Messbereichs: Problematisch
            
            **Beispiel:** Blutdruck-Messbereich ist etwa 40-200 mmHg
            - 5% = 8 mmHg → Akzeptabler Bias
            - 20 mmHg Bias → Problematisch
            """)
        
        with st.expander("Was sind Limits of Agreement (LoA)?"):
            st.markdown("""
            **LoA = Grenzen der Übereinstimmung**
            
            **Definition:** Der Bereich, in dem 95% der Unterschiede zwischen Methoden liegen
            
            **Berechnung:** 
            - Mittlere Differenz ± 1.96 × Standardabweichung der Differenzen
            
            **Interpretation:**
            - Schmale LoA → Gute Übereinstimmung
            - Breite LoA → Schlechte Übereinstimmung
            - Sollte für klinische Entscheidungen klinisch relevant sein
            
            **Beispiel:** Wenn LoA = [-5, +5] mmHg
            - 95% der Messungen unterscheiden sich maximal um 5 mmHg
            - Ist das für deine Anwendung akzeptabel?
            """)
        
        with st.expander("Sind meine Punkte weit außerhalb der LoA - ist das ein Problem?"):
            st.markdown("""
            **Normal:** Bis zu 5% der Punkte können außerhalb liegen
            
            **Wenn mehr Punkte außerhalb sind:**
            - Überprüfe Dateneingabe auf Fehler
            - Möglicherweise Ausreißer vorhanden
            - Unterscheiden sich diese Messungen systematisch?
            
            **Was tun?**
            1. Überprüfe die Rohdaten
            2. Wenn Fehler: Entferne fehlerhafte Punkte
            3. Führe Analyse erneut durch
            4. Dokumentiere, was entfernt wurde
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
    
    if analyzer_type == "Passing-Bablok":
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
            -  Sehr gut für medizinische Geräte
            -  Sehr gut für Labormessungen
            -  Akzeptabel für Screenings
            -  Grenzwert für kritische Messungen
            -  Nicht ausreichend für hochpräzise Kalibrationen
            
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
        
         Korrekt:
        ```
        Methode_A,Methode_B
        10.5,10.2
        12.3,12.1
        ```
        
         Falsch:
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
        
         Okay:
        - Formatierung
        - Berechnungen (z.B. Mittelwerte)
        - Runden (z.B. auf 2 Dezimalstellen)
        - Filterung (nur bestimmte Zeilen)
        
         Problematisch:
        - Abhängige Zellen (können "#REF" zeigen beim Export)
        - Externe Verknüpfungen
        - Bedingte Formatierung
        
        **Tipp:** Nach Berechnung die Werte → Werte einfügen, 
        dann als CSV speichern.
        """)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="guide-section">
    <h3> Noch Fragen?</h3>
    <p>Wenn du auf ein Problem stößt:</p>
    <ol>
        <li>Schaue in dieser Anleitung nach (nutze die Suche)</li>
        <li>Überprüfe deine CSV-Datei nochmal</li>
        <li>Versuche die Schritte in dieser Anleitung zu wiederholen</li>
        <li>Falls weiterhin Probleme: Überprüfe die Fehlermeldung in der App</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.caption("Benutzeranleitung für den Passing-Bablok Analyzer")

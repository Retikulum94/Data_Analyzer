# User-Testung für die Streamlit-App „Data_Analyzer"

## Ziel und Testgegenstand
Diese User-Testung bewertet eine Streamlit-App, mit der per CSV-Upload methodenvergleichende Auswertungen mit Passing-Bablok-Regression und Bland-Altman-Darstellung erstellt werden können. Der Fokus liegt auf Verständlichkeit, Bedienbarkeit, Fehlerrobustheit und dem sicheren Interpretieren der erzeugten Analyseergebnisse in einem typischen wissenschaftlichen oder laboranalytischen Nutzungskontext.

## Testziele
Die Testung soll prüfen, ob Nutzerinnen und Nutzer den Analyse-Workflow ohne fremde Hilfe durchführen können und ob die App die zentralen Schritte ausreichend transparent macht. Zusätzlich soll untersucht werden, ob die Visualisierungen und Kennwerte so präsentiert werden, dass konstante und proportionale Abweichungen zwischen Messmethoden korrekt erkannt werden können.

Konkrete Ziele:
- Erfolgreicher CSV-Upload und Start der Analyse.
- Verständliche Zuordnung der beiden Messmethoden bzw. Spalten.
- Korrekte Interpretation von Passing-Bablok-Parametern und Bland-Altman-Bias.
- Erkennen typischer Bedienprobleme, etwa bei Dateiformat, Spaltenwahl oder unklaren Achsenbezeichnungen.
- Bewertung der wahrgenommenen Vertrauenswürdigkeit der Resultate für wissenschaftliche oder praktische Entscheidungen.

## Hypothesenbildung
### Haupt-Hypothesen
**H1:** Mindestens 80 % der Testpersonen können ohne Unterstützung eine gültige CSV-Datei hochladen und eine vollständige Analyse starten.

**H2:** Mindestens 70 % der Testpersonen erkennen nach der Auswertung, dass ein Bland-Altman-Plot der Beurteilung der Übereinstimmung dient und nicht bloß der Korrelation.

**H3:** Mindestens 70 % der Testpersonen können nach Ansicht der Ergebnisse korrekt erklären, was eine positive bzw. negative mittlere Differenz im Bland-Altman-Plot bedeutet, sofern die Differenzrichtung in der App klar benannt ist.

**H4:** Mindestens 60 % der Testpersonen können die Passing-Bablok-Ausgabe so deuten, dass Steigung und Achsenabschnitt unterschiedliche Arten von Bias beschreiben, also proportionale versus konstante Abweichung.

**H5:** Nutzerinnen und Nutzer mit fachlichem Vorwissen in Statistik oder Labormedizin bearbeiten die Aufgaben schneller und mit weniger Rückfragen als fachfremde, aber digital affine Personen.

### Neben-Hypothesen
- Unklare Benennungen der Rollen von Referenzmethode und Testmethode führen zu Fehlinterpretationen der Richtung von Bias und Differenz.
- Fehlende Rückmeldungen bei ungeeigneten CSV-Dateien erhöhen Abbruchrate und Frustration.
- Eine Vorschau der importierten Daten verbessert die Sicherheit bei der Spaltenauswahl.
- Erläuternde Kurztexte direkt bei den Plots verbessern die inhaltliche Interpretation stärker als eine reine Ausgabe von Zahlenwerten.

## Testdesign
Empfohlen wird ein moderierter Usability-Test mit Think-Aloud-Methode, kombiniert mit kurzen Verständnisfragen nach jeder Kernaufgabe. Dieses Vorgehen deckt sowohl Bedienprobleme als auch fachliche Fehlinterpretationen auf.

### Zielgruppen
Es sollten 6 bis 10 Personen aus zwei Gruppen getestet werden:

- Gruppe A: Fachnahe Nutzende, z. B. aus Biomedizin, Analytik, Statistik oder Data Science.
- Gruppe B: Digital affine Nutzende ohne vertieftes Methodenvergleichs-Wissen.

### Testumgebung
- Laptop oder Desktop mit aktuellem Browser.
- Zugriff auf die laufende Streamlit-App.
- Drei vorbereitete CSV-Dateien: gültiger Standardfall, Datei mit Formatfehler, Datei mit fehlenden oder falsch benannten Spalten.
- Beobachtungsbogen und Zeitmessung.

## Testaufgaben
### Aufgabe 1: Einstieg und Orientierung
„Öffnen Sie die App und erklären Sie kurz, was Sie hier vermutlich tun können.“

**Beobachtungskriterien:** erster Eindruck, Verständnis des Zwecks, Orientierung in der Oberfläche.

### Aufgabe 2: CSV hochladen
„Laden Sie die bereitgestellte CSV-Datei hoch und starten Sie die Analyse.“

**Erfolgskriterien:** Datei wird gefunden, Upload gelingt, Analyse startet ohne Hilfe.

### Aufgabe 3: Spalten und Methoden zuordnen
„Ordnen Sie die Messwerte der Referenzmethode und der Vergleichsmethode korrekt zu.“

**Beobachtungskriterien:** Verständnis der Rollenverteilung, Sicherheit bei der Auswahl, Rückfragen.

### Aufgabe 4: Passing-Bablok interpretieren
„Beschreiben Sie mit eigenen Worten, was Ihnen die Regressionsausgabe über die Beziehung der beiden Methoden sagt.“

**Erwartete Inhalte:** Steigung nahe 1 spricht gegen starken proportionalen Bias; ein von 0 abweichender Achsenabschnitt spricht für konstanten Bias.

### Aufgabe 5: Bland-Altman interpretieren
„Beschreiben Sie, was der Bland-Altman-Plot aussagt und ob die beiden Methoden gut übereinstimmen.“

**Erwartete Inhalte:** Fokus auf mittlere Differenz und Limits of Agreement statt auf lineare Korrelation. Die Richtung der Differenz muss konsistent zur Benennung der Methoden verstanden werden.

### Aufgabe 6: Fehlerfall bearbeiten
„Laden Sie nun eine problematische CSV-Datei hoch und versuchen Sie herauszufinden, warum die Analyse nicht funktioniert.“

**Beobachtungskriterien:** Verständnis von Fehlermeldungen, Selbsthilfe, Frustration, gewünschte Systemunterstützung.

## Testprotokoll
### Metadaten
- Test-ID:
- Datum:
- Moderator/in:
- Testperson:
- Gruppe: fachnah / fachfremd
- Vorwissen Statistik: niedrig / mittel / hoch
- Vorwissen Method Comparison: niedrig / mittel / hoch

### Ablauf
1. Begrüßung und Einverständnis einholen.
2. Kurz erklären, dass die App getestet wird, nicht die Person.
3. Think-Aloud anregen.
4. Aufgaben nacheinander bearbeiten lassen.
5. Nur eingreifen, wenn die Person dauerhaft blockiert ist.
6. Nach jeder Aufgabe kurze Verständnisfrage stellen.
7. Abschließend subjektive Bewertung erheben.

### Beobachtungsbogen
| Aufgabe | Erfolgreich? | Zeit | Hilfe nötig? | Fehler / Stolperstellen | Zentrale Zitate |
|---|---|---:|---|---|---|
| Einstieg | Ja / Nein |  | Ja / Nein |  |  |
| CSV-Upload | Ja / Nein |  | Ja / Nein |  |  |
| Zuordnung Methoden | Ja / Nein |  | Ja / Nein |  |  |
| Passing-Bablok | Ja / Nein |  | Ja / Nein |  |  |
| Bland-Altman | Ja / Nein |  | Ja / Nein |  |  |
| Fehlerfall | Ja / Nein |  | Ja / Nein |  |  |

### Nachbefragung
Bewertung jeweils auf einer Skala von 1 bis 5:

- Die App war leicht zu bedienen.
- Ich wusste, was ich als Nächstes tun muss.
- Die Benennung von Referenz- und Testmethode war klar.
- Die Diagramme waren leicht interpretierbar.
- Die Fehlermeldungen waren hilfreich.
- Ich würde der Auswertung fachlich vertrauen.

Offene Fragen:
- Was war unklar oder irritierend?
- Was hat besonders gut funktioniert?
- Welche Information hat gefehlt?
- Was müsste verbessert werden, damit Sie die App im Alltag nutzen würden?

## Auswertungstemplate
### Quantitative Auswertung
| Kennzahl | Zielwert | Ist-Wert | Erfüllt? | Kommentar |
|---|---:|---:|---|---|
| Erfolgsquote CSV-Upload | >= 80 % |  | Ja / Nein |  |
| Erfolgsquote vollständige Analyse | >= 80 % |  | Ja / Nein |  |
| Korrekte Interpretation Bland-Altman | >= 70 % |  | Ja / Nein |  |
| Korrekte Interpretation Passing-Bablok | >= 60 % |  | Ja / Nein |  |
| Median Bearbeitungszeit Kernworkflow | Ziel definieren |  | Ja / Nein |  |
| Anteil mit Hilfebedarf | <= 30 % |  | Ja / Nein |  |
| Durchschnittliche Bedienbarkeit | >= 4.0 / 5 |  | Ja / Nein |  |
| Durchschnittliches Vertrauen | >= 4.0 / 5 |  | Ja / Nein |  |

### Qualitative Auswertung
Die qualitativen Beobachtungen sollten in Themenclustern zusammengefasst werden:

- Navigation und Orientierung.
- CSV-Verständnis und Dateneingabe.
- Zuordnung von Referenz- und Testmethode.
- Interpretierbarkeit von Passing-Bablok.
- Interpretierbarkeit von Bland-Altman.
- Verständlichkeit von Fehlermeldungen.
- Verbesserungsvorschläge der Testpersonen.

### Schweregrad-Schema
| Schweregrad | Definition | Beispiel |
|---|---|---|
| 1 – gering | Kosmetisches oder kleines Irritationsproblem | Unklare Beschriftung ohne Folgen |
| 2 – mittel | Verlangsamt den Ablauf deutlich | Unsicherheit bei Spaltenzuordnung |
| 3 – hoch | Führt zu Fehlinterpretation oder Abbruch | Bias-Richtung wird falsch verstanden |
| 4 – kritisch | Fachlich riskante Fehlbedienung | Falsche Methodenzuordnung erzeugt falsche Schlussfolgerung |

## Schlussfolgerungen und Ableitung
Die Schlussfolgerungen sollten nicht nur auf Erfolgsraten beruhen, sondern besonders auf inhaltlich kritischen Missverständnissen. Bei einer App für Methodenvergleich ist es zentral, dass Nutzende nicht nur einen Plot erzeugen, sondern auch erkennen, dass Bland-Altman die Übereinstimmung über Bias und Limits of Agreement beschreibt, während Passing-Bablok konstante und proportionale Abweichungen modelliert.

Für die Ergebnisableitung eignet sich folgende Struktur:

1. **Was funktioniert gut?**
   - Welche Aufgaben wurden schnell und sicher gelöst?
   - Welche UI-Elemente wurden intuitiv verstanden?

2. **Wo entstehen Fehlinterpretationen?**
   - Wird Korrelation mit Übereinstimmung verwechselt?
   - Wird die Richtung der Differenz im Bland-Altman-Plot missverstanden, weil Referenz- und Testmethode nicht eindeutig benannt sind?

3. **Welche Risiken sind fachlich relevant?**
   - Können Nutzende aus falscher Achsen- oder Methodenzuordnung unzutreffende Aussagen über Bias ableiten?
   - Werden Grenzen der Methode, etwa bei ungeeigneten Daten oder Dateiformaten, ausreichend verstanden?

4. **Welche Verbesserungen haben Priorität?**
   - Klare Labels für Referenzmethode, Testmethode und Differenzrichtung.
   - Hilfetexte direkt an Plot und Kennzahlen.
   - Robuste Validierung beim CSV-Upload mit verständlichen Fehlermeldungen.
   - Datenvorschau vor der Analyse.
   - Beispiel-Datensatz oder Demo-Modus für Erstnutzende.

## Empfehlung für die Dokumentation der Ergebnisse
Für den Abschlussbericht sollte pro identifiziertem Problem immer festgehalten werden:

- Beobachtung.
- Betroffene Aufgabe.
- Häufigkeit.
- Schweregrad.
- Vermutete Ursache.
- Konkrete Designempfehlung.

Ein Beispiel:

| Problem | Häufigkeit | Schweregrad | Ursache | Empfehlung |
|---|---:|---:|---|---|
| Testpersonen verwechseln Referenz- und Testmethode | 4 von 8 | 3 – hoch | Uneindeutige Labels und fehlende Erklärung der Differenzrichtung | Beschriftung präzisieren, Hilfetext und Default-Beispiel ergänzen |

## Kurzfazit
Eine gute User-Testung für diese App muss Bedienbarkeit und fachliche Interpretierbarkeit gemeinsam prüfen. Gerade bei Passing-Bablok- und Bland-Altman-Analysen ist das größte Risiko nicht nur ein technischer Bedienfehler, sondern eine plausibel wirkende, aber inhaltlich falsche Interpretation der Auswertung.

# Dokumentation
## Kurz zusammengefasst
Das Projekt ist eine Streamlit-Webanwendung, mit der Laboranwender CSV-Dateien hochladen und daraus Passing-Bablok-Regressionen sowie Bland-Altman-Plots erstellen können.

## Was die App macht
Die App hilft, zwei Messmethoden miteinander zu vergleichen, zum Beispiel ein neues Laborgerät mit einem etablierten Referenzgerät.

Nutzer laden Messdaten als CSV-Datei hoch, wählen die relevanten Spalten aus und erhalten automatisch eine statistische Auswertung inklusive Grafiken.

## Zielgruppe und Nutzen
Die Anwendung richtet sich an Laborpersonal, das Messergebnisse vergleichen möchte, aber keine tiefen Statistik- oder Programmierkenntnisse besitzt.

So können Methodenvergleiche schnell, reproduzierbar und ohne teure Spezialsoftware durchgeführt werden.

## Grundlagen: 
### Passing-Bablok-Regression
Die Passing-Bablok-Regression ist ein spezielles Regressionsverfahren, um zwei quantitative Messmethoden zu vergleichen.

Sie ist robust gegenüber Ausreißern und setzt keine besondere Verteilung der Messwerte voraus, weshalb sie in der Labormedizin häufig eingesetzt wird.

Typische Fragestellungen sind:

Gibt es eine systematische Abweichung zwischen zwei Methoden (Bias)?

Ist eine der Methoden proportional verzerrt (z.B. bei hohen Werten)?

### Bland-Altman-Plot
Der Bland-Altman-Plot stellt die Differenz zweier Messmethoden gegen deren Mittelwert dar.

Dadurch erkennt man, ob die Abweichungen zufällig sind oder ob es Muster gibt, zum Beispiel zunehmende Differenzen bei hohen Konzentrationen.

Der Plot zeigt typischerweise:

Mittlere Differenz (Bias) zwischen den Methoden

Vertrauensgrenzen (Limits of Agreement), innerhalb derer ein Großteil der Differenzen liegt

## Aufbau der App
Die App ist mit Streamlit umgesetzt, einer Python-Bibliothek zum schnellen Erstellen von Webanwendungen für Datenanalyse.

Die Benutzeroberfläche wird im Browser angezeigt und passt sich automatisch an, sodass keine Installation spezieller GUIs notwendig ist.

## Bestandteile:

Bereich zum Hochladen von CSV-Dateien

Auswahlfelder für X- und Y-Variablen (z.B. Referenz- und Testmethode)

Ausgabe von Kennzahlen (Regressionsparameter, Bias)

Interaktive Grafiken für Passing-Bablok-Regression und Bland-Altman-Plot

## Typischer Workflow
Der Workflow ist für Passing-Bablok und Bland-Altman identisch.
### CSV-Datei vorbereiten
Die Datei sollte Messwerte beider Methoden in separaten Spalten enthalten (z.B. „Referenz“ und „Testmethode“).

### Datei in der App hochladen
Entweder kann die Datei direkt per Drag and Drop in die Upload-Schaltfläche gezogen werden, oder über den Browse files button im Ordner ausgewählt werden.

### Spalten auswählen
Wähle nun aus, welche Spalten die x- und welche die y-Achse sein sollen.
#### x-Achse:
Die x-Achse sind typischerweise die Daten der etablierten- bzw. der Referenz Methode.
#### y-Achse
Die y-Achse sind typischerweise die Daten der neuen Methode.

### Grafiken abspeichern
Nach dem Dateiupload berechnet und erstellt die App automatisch die jeweiligen Plots. Diese können dann einfach entweder gedownloaded, oder auf Switch-drive hochgeladen werden.

## Ergebnisse interpretieren
Durch Blick auf Steigung, Achsenabschnitt und Bland-Altman-Grenzen lässt sich beurteilen, ob die neue Methode für die Praxis geeignet ist.

## Technische Rahmenbedingungen
Die App läuft als Streamlit-Anwendung in einer Python-Umgebung.

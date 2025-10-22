### 2025-10-16
**Was wurde gemacht:**  
Experiment: Einführung einer Normalisierungsfunktion für Eingaben. Beobachtung: Fehler durch überflüssige Leerzeichen verschwinden. Schlussfolgerung: Datenqualität steigt bei minimalem Implementierungsaufwand. 

**Warum:**  
Um mögliche Fehler bei der Eingabe der Ausgangsdaten zu vermeiden.  

**Ergebnisse:**  
Fehlerhafte Eingaben im Dokument werden automatisch entfernt, z. B. überflüssige Leerzeichen nach dem Namen.  

**Probleme:**  
Es können weiterhin Fehler auftreten, wenn die Ausgangsdaten stark fehlerhaft sind.  

**Ideen:**  
Die Schüler anhand eines eindeutigen Indexes zuordnen und die Ergebnisse zusätzlich mit den Namen ausgeben, um Verwechslungen zu vermeiden.


### 2025-10-17
**Was wurde gemacht:**  
Algorithmus zur Zuteilung aktualisiert (neue OR-Tools-Variante) für ausgewogenere Verteilung der Schüler.

**Warum:**  
Um die Verteilung klarer und gerechter zu gestalten.

**Ergebnisse:**  
Mittelwert der Zufriedenheit leicht gesunken, Streuung gestiegen – zeigt ausgeglichenere Verteilung trotz gleicher Kapazitätsgrenzen. 

Statistik vor und nach der Änderung:

| Metrik | Vorher | Nachher |
|--------|--------|---------|
| Mittelwert Zufriedenheit | 93.96 | 92.55 |
| Minimum | 67 | 33 |
| Maximum | 100 | 100 |
| Standardabweichung | 8.27 | 11.35 |
| Varianz | 68.41 | 128.82 |
| Median | 100 | 100 |

**Probleme:**  
Die Verarbeitung und Iteration im DataFrame über die Namen ist nicht vollständig zuverlässig;


**Ideen:**  
Die Zufriedenheitsmetriken können direkt extrahiert werden;
Implementiere einen Algorithmus, der die Verteilung direkt über drei Semester vornimmt, statt sie einzeln zu bearbeiten.


### 2025-10-17
**Was wurde gemacht:**  
Experiment: Erweiterung des Algorithmus auf gleichzeitige Zuteilung mehrerer Semester. Beobachtung: Laufzeit bleibt akzeptabel, Zufriedenheitswerte verbessern sich leicht. Schlussfolgerung: Multi-Semester-Zuordnung ist effizienter und gerechter.

Allgemeine Optimierung des Algorithmus durch Verwendung von .to_numpy() (ndarray)

**Warum:**  
um den durchschnittlichen Zufriedenheitswert der Studierenden zu verbessern
um die Zuordnung zuverlässiger und gerechter zu gestalten

**Ergebnisse:**  
Die durchschnittlichen Zufriedenheitswerte sind leicht gestiegen, während die Streuung (Standardabweichung, Varianz) deutlich abgenommen hat

Statistik Hung. Alg. , or-tools 1.0, or-tools 1.1 nach der Änderung:

| Metrik | Hungarian Algorithm | or-tools.linear_solver 1.0 | or-tools.linear_solver 1.1 |
|--------|--------|---------|---------|
| Mittelwert Zufriedenheit | 93.96 | 92.55 | 93.96 |
| Minimum | 67 | 33 | 67 |
| Maximum | 100 | 100 | 100 |
| Standardabweichung | 8.27 | 11.35 | 7.62 |
| Varianz | 68.41 | 128.82 | 58.04 |
| Median | 100 | 100 | 100 |

**Probleme:**  
Es wurden keine Probleme festgestellt

**Ideen:**  
Vereinfache die Berechnung der Statistik, sodass die statistischen Daten direkt nach der Zuordnung ausgegeben werden können


### 2025-10-19
**Was wurde gemacht:**  
Optimierung des Statistik-Moduls und Integration der Zufriedenheitsberechnung direkt im Zuteilungsalgorithmus (students_appointment).
Anstatt die Statistiken nachträglich über aufwendige Iterationen (apply-Schleifen, ~200 Zeilen Code) neu zu berechnen, wird nun bei jeder Zuteilung der Schüler die Zufriedenheit sofort in einem DataFrame im Long-Format gespeichert.

**Warum:**  
Bessere Performance (keine doppelten Berechnungen, keine aufwendigen Pandas-Schleifen).

Vereinfachung der Architektur: Die Statistiken entstehen direkt beim Zuteilungsschritt, dadurch ist das Statistik-Modul deutlich kompakter.

Vorbereitung für explorative Analysen: Das neue Long-Format erlaubt groupby-Auswertungen nach Sport, Semester oder Schüler.

**Ergebnisse:**  
Reduktion des Statistik-Codes von ca. 200 auf wenige Dutzend Zeilen.

Deutlicher Geschwindigkeitsgewinn (statistische Auswertung fast instantan auch bei >70 Schülern).

Die berechnete Statistik wurde etwas präziser als zuvor.

Vereinfachte Visualisierungen: Diagramme können direkt aus dem DataFrame erzeugt werden.

Beispiel: Durchschnittliche Zufriedenheit pro Sportart und Semester jetzt in 2 Zeilen Code statt kompletten Iterationen.

**Probleme:**  
Gefahr von Namenskonflikten bei Schülern mit identischem Namen.

Noch kein robustes Error-Handling für ungültige Eingaben (z. B. unbekannte Sportarten in Excel-Datei).

**Ideen:**  
Einführung einer eindeutigen Schüler-ID (z. B. Kombination aus Index + Name).

Automatische Validierung der Eingabedaten mit Warnungen im Log.

Nutzung der neuen Long-Format-Daten auch für multisemestrale Fairness-Analysen (z. B. sicherstellen, dass jeder Schüler mindestens einmal einen 1.-Wunsch erhält).


### 2025-10-21
**Was wurde gemacht:**  
Die Datei `config.py` wurde überarbeitet, sodass alle Dateipfade nun dynamisch mit der Bibliothek `pathlib` generiert werden. Dadurch erkennt das Programm automatisch die Projektstruktur, unabhängig vom Betriebssystem oder Speicherort.

**Warum:**  
Beim Übertragen des Projekts auf andere Geräte mussten die Dateipfade bisher manuell angepasst werden. Das führte zu Fehlern und erschwerte die Reproduzierbarkeit der Ergebnisse.

**Ergebnisse:**  
Das System erkennt nun selbstständig alle relevanten Verzeichnisse (z. B. *Data/*, *Output/*).  
Der Start des Programms ist auf jedem Rechner ohne zusätzliche Konfiguration möglich.  
Die Portabilität und Stabilität des Projekts wurde deutlich verbessert.

**Probleme:**  
Noch keine validierte Lösung für den Fall, dass Eingabedateien fehlen oder fehlerhaft benannt sind.

**Ideen:**  
Zukünftig soll das System automatisch prüfen, ob Eingabe- und Ausgabeverzeichnisse vorhanden sind,  
und bei Bedarf diese selbstständig anlegen.  
Außerdem könnten alle Parameter in `config.py` über eine Benutzeroberfläche anpassbar werden,  
um die Definition beliebiger Semester und Slots zu ermöglichen.


### 2025-10-22
**Was wurde gemacht:**  
Umstellung der gesamten Datenverarbeitung auf ein indexbasiertes, modulares Pipeline-System.
Die Schüler werden jetzt nicht mehr über Namen, sondern über eindeutige Indizes identifiziert.
Dadurch wurde die Datenübergabe zwischen den Modulen (Zuteilung → Statistik → Export) vollständig stabilisiert.

**Warum:**  
Die bisherige Architektur basierte auf Namensstrings, die bei Namensgleichheit zu fehlerhaften Zuordnungen führen konnten.
Außerdem war die Übergabe der DataFrames an die Ausgabemodule teilweise unflexibel.
Ziel war es, eine wissenschaftlich reproduzierbare Pipeline zu schaffen, bei der jede Komponente klar definierte Eingabe- und Ausgabeformate hat.

**Ergebnisse:**  
Einführung des Objekts ready_semestrs_dfs, das als zentrales Datenpaket zwischen den Modulen dient.

Vereinheitlichung der Datenflüsse im gesamten Projekt (von der Zuteilung bis zur finalen Ausgabe).

Wegfall redundanter Berechnungen und vereinfachte Erweiterbarkeit.

Deutlich verbesserte Robustheit beim Systemtransfer – kein manuelles Anpassen mehr nötig.

**Probleme:**  
Noch keine Fehler festgestellt, aber für große Datensätze (>200 Schüler) sollte die Performance weiter getestet werden.

**Ideen:**  
Ergänze ein optionales metadata-Feld in ready_semestrs_dfs (z. B. Rechenzeit, Durchschnittszufriedenheit, Schüleranzahl).

Erweiterung des Systems um eine automatisierte Validierung der Zwischenergebnisse.

Dokumentation der neuen Architektur im Diagrammformat (Dataflow- oder Pipeline-Skizze für den JuFo-Bericht).
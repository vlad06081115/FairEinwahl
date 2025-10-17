### 2025-10-16
**Was wurde gemacht:**  
Die Funktion `norm()` zur Normalisierung von Strings im Modul `students_appointment` wurde implementiert.  

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
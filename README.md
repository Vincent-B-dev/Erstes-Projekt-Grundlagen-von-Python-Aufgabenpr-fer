# Aufgabenprüfer

Mit meinem Aufgabenprüfer kann ich Aufgaben in der Konsole anzeigen, hinzufügen und wieder löschen.

## Einleitung – Wie habe ich gearbeitet?

Ich habe den Aufgabenprüfer Schritt für Schritt gemeinsam mit ChatGPT entwickelt. Dabei habe ich nicht einfach nur den fertigen Code übernommen: ChatGPT hat mir die einzelnen Schritte und Python-Bausteine erklärt, damit ich verstehen konnte, was der Code macht und warum er gebraucht wird.

Wenn ich etwas nicht verstanden habe, habe ich nachgefragt. Außerdem habe ich eigene Ideen und Verbesserungsvorschläge eingebracht. So ist das Programm nach und nach um weitere Funktionen ergänzt worden. Dazu gehören das Hinzufügen und Anzeigen von Aufgaben sowie das Löschen über eine Nummer. Ich habe auch darauf geachtet, dass das Programm auf leere Eingaben, ungültige Antworten und nicht vorhandene Aufgabennummern reagiert.

Bei der Entwicklung habe ich wichtige Python-Grundlagen praktisch angewendet: Eingaben mit `input()`, Ausgaben mit `print()`, Bedingungen mit `if`, Wiederholungen mit `while` und `for` sowie Listen zum Verwalten der Aufgaben.

## Anleitung

Am Anfang fragt mich das Programm nach einem Namen. Wenn ich „Max“ eingebe, werde ich als Administrator begrüßt und bekomme drei voreingestellte Aufgaben. Bei jedem anderen Namen werde ich als Gast begrüßt und starte mit einer leeren Aufgabenliste.

Danach kann ich Aufgaben hinzufügen. Eine leere Eingabe wird nicht angenommen. Wenn ich keine weiteren Aufgaben hinzufügen möchte, zeigt das Programm die Liste nummeriert an. Zum Löschen gebe ich die Nummer der gewünschten Aufgabe ein. Anschließend kann ich weitere Aufgaben löschen. Zum Schluss wird meine aktuelle Aufgabenliste ausgegeben.

### Voraussetzungen

- Python 3
- Ein Terminal oder eine Konsole

### Programm starten

Speichere den Code zum Beispiel als `aufgabenpruefer.py`. Unter Windows kann ich das Programm im Terminal mit diesem Befehl starten:

```bash
py -3 aufgabenpruefer.py
```

Falls der Befehl `py` nicht verfügbar ist, kann ich stattdessen Folgendes versuchen:

```bash
python aufgabenpruefer.py
```

Bei den Ja/Nein-Fragen kann ich auch Großbuchstaben verwenden. Bei einer ungültigen Antwort oder Aufgabennummer fragt mich das Programm erneut.

## Meine Verbesserungsvorschläge für Version 2.0

- **Menü in einer Schleife:** Ich möchte ein Menü einbauen, das nach jeder Aktion wieder erscheint. Erst wenn ich „Beenden“ auswähle, soll das Programm stoppen. So kann ich während eines Durchgangs immer wieder Aufgaben hinzufügen, löschen oder ansehen.
- **Speicherfunktion:** Die Aufgaben sollen in einer Datei gespeichert und beim nächsten Start wieder geladen werden. Dann bleibt die Liste auch nach dem Schließen des Programms erhalten.
- **Aufgaben bearbeiten:** Eine Funktion um Aufgaben später auch umbenennen zu können.
- **Code übersichtlicher aufteilen:** Man könnte einzelne Bereiche wie Anzeigen, Hinzufügen, Löschen und Speichern in eigene Funktionen aufteilen.

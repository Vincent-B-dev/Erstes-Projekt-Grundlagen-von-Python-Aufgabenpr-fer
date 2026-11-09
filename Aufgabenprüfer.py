print("Willkommen beim Aufgabenprüfer!")

name = input("Wie heißt du?")

if name.lower() == "max":
    print("Willkommen zurück Max!")
    print("Du bist der Administrator!")

else:
    print("Schön das du da bist " + name + "!")
    print("Du bist ein Gast!")

if name.lower() == "max":
    aufgaben = ["Python lernen", "Bewerbung schreiben", "Pc aufräumen"]
else:
    aufgaben =[]

for aufgabe in aufgaben:
    print(aufgabe)

weiter= "ja"

while weiter.lower() == "ja":

    neue_aufgabe = ""

    while neue_aufgabe == "":
        neue_aufgabe = input("Welche Aufgabe möchtest du hinzufügen?")

        if neue_aufgabe == "":
            print("Fehler: Bitte gib eine Aufgabe ein!")

    aufgaben.append(neue_aufgabe)

    weiter = input("Möchtest du eine weitere Aufgabe hinzufügen? (ja/nein) ")
    while weiter.lower() != "ja" and weiter.lower() != "nein":
        print("Bitte antworte nur mit ja oder nein.")
        weiter = input("Möchtest du eine weitere Aufgabe hinzufügen? (ja/nein) ")

print("Deine endgültige Aufgabenliste:")

nummer = 1

for aufgabe in aufgaben:
    print(nummer, "-", aufgabe)
    nummer = nummer + 1

weiter_loeschen = "ja"
if len(aufgaben) == 0:
    print("Es sind keine Aufgaben vorhanden!")

while weiter_loeschen.lower() == "ja" and len(aufgaben) > 0:

    gueltige_eingabe = False

    while gueltige_eingabe == False:

        eingabe = input("Welche Aufgabe möchtest du löschen? ")

        if eingabe.isdigit():
            nummer = int(eingabe)

            if nummer >= 1 and nummer <= len(aufgaben):
                index = nummer - 1
                aufgaben.pop(index)
                print("Aufgabe gelöscht!")
                gueltige_eingabe = True
                print("Aktuelle Aufgabenliste:")

                nummer = 1

                for aufgabe in aufgaben:
                    print(nummer, "-", aufgabe)
                    nummer = nummer + 1

                if len(aufgaben) > 0:
                    weiter_loeschen = input("Möchtest du noch eine Aufgabe löschen? (ja/nein) ")

                else:
                    print("Du hast alle Aufgaben gelöscht!")
                    weiter_loeschen = "nein"

                if len(aufgaben) > 0:
                    while weiter_loeschen.lower() != "ja" and weiter_loeschen.lower() != "nein":
                        print("Bitte antworte nur mit ja oder nein.")
                        weiter_loeschen = input("Möchtest du noch eine Aufgabe löschen? (ja/nein) ")

            else:
                print("Diese Aufgabennummer gibt es nicht!")

        else:
            print("Bitte gib eine Zahl ein.")

print("Vielen Dank! Hier ist deine aktuelle Aufgabenliste für heute:")

nummer = 1

for aufgabe in aufgaben:
    print(nummer, "-", aufgabe)
    nummer = nummer + 1

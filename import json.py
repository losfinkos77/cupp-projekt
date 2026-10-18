import json
import os

class SchubladenSystem:
    def __init__(self, datei='schubladen.json'):
        self.datei = datei
        self.schubladen = self.laden()

    def laden(self):
        if os.path.exists(self.datei):
            try:
                with open(self.datei, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Fehler beim Laden der Datei. Starte mit leerem System.")
                return {}
        return {}

    def speichern(self):
        with open(self.datei, 'w') as f:
            json.dump(self.schubladen, f, indent=4)
        print("✅ System gespeichert.")

    def schublade_erstellen(self, name):
        if name in self.schubladen:
            print(f"⚠️ Schublade '{name}' existiert bereits.")
        else:
            self.schubladen[name] = []
            self.speichern()
            print(f"✅ Schublade '{name}' erstellt.")

    def schublade_loeschen(self, name):
        if name in self.schubladen:
            del self.schubladen[name]
            self.speichern()
            print(f"🗑️ Schublade '{name}' gelöscht.")
        else:
            print(f"⚠️ Schublade '{name}' nicht gefunden.")

    def hinzufuegen(self, name, eintrag):
        if name in self.schubladen:
            self.schubladen[name].append(eintrag)
            self.speichern()
            print(f"➕ '{eintrag}' zu Schublade '{name}' hinzugefügt.")
        else:
            print(f"⚠️ Schublade '{name}' nicht gefunden.")

    def entfernen(self, name, eintrag):
        if name in self.schubladen:
            try:
                self.schubladen[name].remove(eintrag)
                self.speichern()
                print(f"➖ '{eintrag}' aus Schublade '{name}' entfernt.")
            except ValueError:
                print(f"⚠️ Eintrag '{eintrag}' nicht in Schublade '{name}'.")
        else:
            print(f"⚠️ Schublade '{name}' nicht gefunden.")

    def anzeigen(self, name):
        if name in self.schubladen:
            print(f"📂 Inhalt von '{name}':")
            for i, eintrag in enumerate(self.schubladen[name], 1):
                print(f"  {i}. {eintrag}")
        else:
            print(f"⚠️ Schublade '{name}' nicht gefunden.")

    def alle_schubladen(self):
        if self.schubladen:
            print("📁 Alle Schubladen:")
            for name in self.schubladen:
                print(f"  - {name}")
        else:
            print("📭 Keine Schubladen vorhanden.")

    def suchen(self, suchbegriff):
        gefunden = False
        for name, eintraege in self.schubladen.items():
            if suchbegriff in eintraege:
                print(f"🔎 Gefunden in '{name}': {suchbegriff}")
                gefunden = True
        if not gefunden:
            print(f"❌ '{suchbegriff}' nicht gefunden.")

    def sortieren(self, name):
        if name in self.schubladen:
            self.schubladen[name].sort()
            self.speichern()
            print(f"🔤 Schublade '{name}' sortiert.")
        else:
            print(f"⚠️ Schublade '{name}' nicht gefunden.")

# Beispiel-Nutzung
if __name__ == "__main__":
    system = SchubladenSystem()

    while True:
        print("\n📦 Schubladen-Menü:")
        print("1. Schublade erstellen")
        print("2. Inhalt hinzufügen")
        print("3. Inhalt anzeigen")
        print("4. Eintrag entfernen")
        print("5. Schublade löschen")
        print("6. Alle Schubladen anzeigen")
        print("7. Suchen")
        print("8. Schublade sortieren")
        print("9. Speichern")
        print("10. Beenden")
        auswahl = input("👉 Auswahl: ")

        if auswahl == "1":
            name = input("📛 Schubladenname: ")
            system.schublade_erstellen(name)
        elif auswahl == "2":
            name = input("📛 Schubladenname: ")
            eintrag = input("✍️ Eintrag: ")
            system.hinzufuegen(name, eintrag)
        elif auswahl == "3":
            name = input("📛 Schubladenname: ")
            system.anzeigen(name)
        elif auswahl == "4":
            name = input("📛 Schubladenname: ")
            eintrag = input("🗑️ Welcher Eintrag soll entfernt werden? ")
            system.entfernen(name, eintrag)
        elif auswahl == "5":
            name = input("📛 Schubladenname: ")
            system.schublade_loeschen(name)
        elif auswahl == "6":
            system.alle_schubladen()
        elif auswahl == "7":
            suchbegriff = input("🔎 Was suchst du? ")
            system.suchen(suchbegriff)
        elif auswahl == "8":
            name = input("📛 Schubladenname: ")
            system.sortieren(name)
        elif auswahl == "9":
            system.speichern()
        elif auswahl == "10":
            system.speichern()
            print("👋 Auf Wiedersehen!")
            break
        else:
            print("❌ Ungültige Eingabe.")
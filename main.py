# Visur ir komentāri lai varētu saprast kā šī programma darbojas.

import json
import os

# Faila nosaukums kur glabāsim receptes
faila_nosaukums = "receptes.json"

# Ielādē receptes no faila
def ieladet_receptes():
    if os.path.exists(faila_nosaukums):
        with open(faila_nosaukums, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}
    # Ja netiek atrasts vajadzīgais fails programma sāk darboties ar tukšu failu (tukšu recepšu sarakstu).


# Saglabā receptes failā
def saglabat_receptes(receptes):
    with open(faila_nosaukums, "w", encoding="utf-8") as f:
        json.dump(receptes, f, ensure_ascii=False, indent=2)

        # Tiek nodrošināts arī tas ka tiek saglabāti latviešu burti, un arī ir formatējums lai viss labāk pārskatāms

# Jaunas receptes pievienošanas funkcija (var saprast kas ir kas pēc input un print tekstiem)
def pievienot_recepti(receptes):
    nosaukums = input("Ievadi receptes nosaukumu: ")
    if nosaukums in receptes:
        print("Šāda recepte jau eksistē!")
        return
    sastavdalas = {}
    print("Ievadi sastāvdaļas (raksti 'gatavs', lai beigtu veidot recepti):")
    while True:
        produkts = input(" - Sastāvdaļa: ")
        if produkts.lower() == "gatavs":
            break
        daudzums = input("   Daudzums: ")
        sastavdalas[produkts] = daudzums
    receptes[nosaukums] = sastavdalas
    saglabat_receptes(receptes)
    print(f"Recepte '{nosaukums}' pievienota!\n")

# Galvenā programma

receptes = ieladet_receptes()

# Iespēja pievienot jaunu recepti
atbilde = input("Vai vēlies pievienot jaunu recepti? (jā/nē): ")
if atbilde.lower() == "jā":
    pievienot_recepti(receptes)
# Ja atbild nē (vai jebko kas nav "jā" ar mazajiem burtiem,zinu ka to var izdarīt pareizāk, bet programmas vajadzībām der) programma neko nedara ar to un vienkārši dodas pie nākamā soļa

# Parāda visas saglabātās receptes
print("\nPieejamās receptes:")
for i, nosaukums in enumerate(receptes.keys(), 1):
    print(f"{i}. {nosaukums}")
# Izvada recešu nosaukumus ar numuriem, manuprāt labāk nekā kad katru reizi jāraksta viss receptes nosaukums


# Šeit prasa ievadīt receptes numuru nevis nosaukumu, protams darbojas arī ar vairākiem skaitļiem ja tos atdala ar komatu kā tas tiek prasīts konsolē
izvele = input("\nIevadi receptes numurus, atdalot ar komatu (piemēram: 1,2): ")
izveletie = [int(nr.strip()) for nr in izvele.split(",")]

# Apkopo iepirkumu sarakstu
saraksts = {}

for idx in izveletie:
    nosaukums = list(receptes.keys())[idx - 1]
    for produkts, daudzums in receptes[nosaukums].items():
        if produkts in saraksts:
            saraksts[produkts].append(daudzums)
        else:
            saraksts[produkts] = [daudzums]

# Izvada iepirkumu sarakstu
print("\n Iepirkumu saraksts:")
for produkts, daudzumi in saraksts.items():
    print(f"- {produkts}: {', '.join(daudzumi)}")

print("\nProgramma pabeigta.")


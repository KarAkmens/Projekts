#  Recepšu kolekcija un iepirkumu saraksta izveidotājs.

##  Projekta uzdevuma apraksts

Šis projekts ir izstrādāts kā praktisks rīks, kas palīdz lietotājam pārvaldīt un izmantot ēdienu receptes ikdienas iepirkumu plānošanai. Projekta galvenais mērķis ir sniegt iespēju uzkrāt receptes ar visām nepieciešamajām sastāvdaļām, un pēc tam balstoties uz lietotāja izvēlētajām receptēm automātiski ģenerēt iepirkumu sarakstu. 

Lai katru reizi nebūtu jāatceras kādas sastāvdaļas ir vajadzīgas kādai receptei un lai neko neaizmirstu pierakstīt uz lapiņas ejot uz veikalu var savas receptes pierakstit un izmantot šo programmu lai uzreiz dabūtu pilnu iepirkumu sarakstu. Lietotājs var pievienot jaunas receptes un tās saglabāt ārējā failā (`receptes.json`), lai tās vienmēr būtu pieejamas. Programma ļauj izvēlēties vienu vai vairākas receptes no saraksta un apkopo visu nepieciešamo informāciju sarakstā.


##  Izmantotās Python bibliotēkas

Šī programma ir izstrādāta izmantojot tikai Python standarta bibliotēkas lai padarītu to vienkāršu un viegli izpildāmu jebkurā datorā, kur ir uzstādīts Python:

- `json` – Tiek izmantots recepšu datu saglabāšanai un ielādei no faila `receptes.json`. 
- `os` – Tiek izmantota lai pārbaudītu, vai fails `receptes.json` jau eksistē.


Nav izmantotas nekādas ārējās bibliotēkas, lai nodrošinātu vienkāršību.

##  Izmantotās datu struktūras

Programmas pamatā tiek izmantotas šādas datu struktūras:

- **Vārdnīcas (dict)** – Gan receptes, gan sastāvdaļas tiek glabātas dict formātā. katra recepte ir attēlota kā objekts ar nosaukumu un sastāvdaļām.
- **Saraksti (list)** – Tiek izmantoti lai apkopotu lietotāja izvēlēto recepšu numurus kā arī, lai uzkrātu sastāvdaļu daudzumus, ja viena un tā pati sastāvdaļa parādās vairākās receptēs.


##  Programmas darbība

Programma darbojas šādi:

1. **Faila pārbaude un ielāde:** Palaižot programmu, tā vispirms pārbauda, vai eksistē `receptes.json` fails. Ja fails eksistē tas tiek nolasīts, ja nav tad programma sāk ar tukšu receptes vārdnīcu.

2. **Jaunas receptes pievienošana:** Lietotājam tiek dota iespēja pievienot jaunu recepti ievadot receptes nosaukumu, pēc tam katru sastāvdaļu un tās daudzumu. Kad lietotājs ievada komandu “gatavs” ievade tiek pabeigta un jaunā recepte tiek pievienota datiem un saglabāta `json` failā.

3. **Receptes izvēle:** Lietotājam tiek parādīts visu recepšu saraksts ar numuriem, un tiek prasīts ievadīt vairāku vai vienas receptes numuru kuram viņš grib izveidot produktu sarakstu.

4. **Iepirkumu saraksta izveidošana:** Programma apvieno visu izvēlēto recepšu sastāvdaļas un izvada iepirkumu sarakstu, kur sastāvdaļas ar vienādiem nosaukumiem tiek saliktas kopā.

5. **Datu saglabāšana:** Visas receptes automātiski tiek saglabātas ārējā `json` failā, kas nozīmē, ka lietotājs var turpināt uzkrāt receptes un tās nevajadzēs ievadīt no jauna katru reizi, kas padarītu šo programmu bezjēdzīgu.


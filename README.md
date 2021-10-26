# Kodegolf

I kodegolf prøver du å løse en oppgave med så få tegn du klarer.
Du kan bruke hvilket som helst språk du vil og må huke tak i en dotkommer når dere har lyst vise fram en løsning.
Vi måler størrelsen på filen i bytes.
I kodegolf skal du "pipe" inn argumentet, og få ut et svar. For eksempel skal følgende funke i python.
Da kan du lese inn argumentet fra `stdin`.
Når du har gjort en oppgave så kan du lage en pull request med en fil som inneholder størrelsen på filen som svar!

```bash
echo "Her er inputet" | python losning.py
```

## Oppgave 1: Røverspråk (easy)

Røverspråk er et kodespråk som er ofte brukt av barn. Regelen er at etter hver konsonant, så skal man legge til en "o", og den samme konsonanten i lowercase etterpå.

Under ser du to eksempler på et slik program.

```bash
echo "Hei" | python losning.py // Hohei
```
En litt lengre setning.

```bash
echo "Jeg heter Eivind" | python losning.py // Jojegog hohetoteror Eivovinondod
```

## Oppgave 2: Ceasar var glad i Emojis (medium)

En vakker dag våkna Ceasar med en telefon og begynte å digge bruken av emojis for å uttrykke seg selv. Han bestemte seg derfor å enkryptere meldingene sine som Emojis, så glad var han i emojis. 

Lag en dekrypterings program som løser denne strengen til engelsk: 

`😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎`

Bruk av programmet 
```bash
echo "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎" | python losning.py"
```

Hva sier strengen?

## Oppgave 3: Bitcoin og Bønner (hard)

Carlos Matos hadde klart å kjøpt seg masse masse bitcoin, og begynner å bli litt sulten. Han er skikkelig gira på kidney bønner og bestemmer seg å selge en av bitcoinene sine. Finn ut hva det maksimale antall bokser med bønner du kan kjøpe på Meny for prisen av en Bitcoin på en gitt dag.

```bash
echo "2021-10-25" | python losning.py // 60428
```

Carlos syns også at det er viktig å tracke denne prisindeksen av BTC til Bønner, og mener at det er viktig at den er future-proof. Derfor må programmet hente prisen på bitcoin, på den gitte datoen, fra nettet. I tillegg kan prisen på den billigeste boksen med kidneybønner endre seg grunnet tilbud, så programmet må også velge ut den billigeste boksen med bønner.

- Du kan hente prisen på bitcoin fra [Coinbase sitt API](https://developers.coinbase.com/api/v2#get-spot-price). Du trenger ikke en auth key for å hente denne prisen
- Du kan hente prisen på bønner på [Meny sin nettside](https://meny.no/Sok/?query=kidney%20b%C3%B8nner)

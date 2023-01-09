## Beschrijving gekozen thema

In dit eindproject heb ik als thema voetbal gekozen, je zal dus 3 tabellen terug vinden.
1 tabel met spelers, 1 tabel met landen en als laatste 1 tabel met voetbal clubs

In dit project heb ik 8 Requests in totaal:
1. **3 Get Requests**
2. **3 Post Requests**
3. **1 Put Request**
4. **1 Delete Request**

## Links

- [Github Repository](https://github.com/bram104/api-endproject)
- [Okteto Link](https://system-service-bram104.cloud.okteto.net/)
- [OpenAPI Docs](https://system-service-bram104.cloud.okteto.net/docs)
- [OpenAPI JSON](https://system-service-bram104.cloud.okteto.net/openapi.json)

## API's
### Post Requests

#### **Post Request om Players te Createn**

Bij deze post request worden players aangemaakt. 
Met een playerId,name,height,date_of_birth,email en een password dat gehashed word.

![image](https://user-images.githubusercontent.com/79090832/211397628-777613ac-7c40-48ab-bdd3-3a91d04bbfed.png)

#### **Post Request om Country's te Createn**

Hier worden Country's aangemaakt.
de kolommen die worden aangemaakt zijn: CountryId,Country_name,Continent

![image](https://user-images.githubusercontent.com/79090832/211398195-90766ee5-0536-4ec9-a58f-af665fd3a567.png)

#### **Post Request om Club's te Createn**

Hier worden Club's aangemaakt.
de kolommen die worden aangemaakt zijn: ClubId,Club_name,Club_Value

![image](https://user-images.githubusercontent.com/79090832/211399665-ce773735-b476-435d-b10f-77d2561c0c57.png)

Bij deze Post Requests moet hetgene wat je wilt posten uniek zijn, dit wil dus zeggen dat je niet
meerdere keren dezelfde data kan versturen.

### Get Requests

#### **Get Request 1 (Country_name)**

Mijn eerste Get Request werkt helaas niet... Volgens mij klopt de Code wel bijna, Heb er lang achter gezocht helaas niet gevonden wat het probleem is.

![image](https://user-images.githubusercontent.com/79090832/211404445-3aef072f-a6cf-4983-af9b-1a20e1677a98.png)

#### **Get Request 2 (PlayerId)**

Via het PlayerId vragen we de informatie op uit de tabel players.

![image](https://user-images.githubusercontent.com/79090832/211404886-34e923ec-0049-41a8-9305-dc313ef0b9ad.png)

#### **Get Request 3 (Club_Value)**

Doormiddel van de Club_Value kunnen we de informatie ophalen uit de tabel Clubs.

![image](https://user-images.githubusercontent.com/79090832/211406759-da5fa907-ab58-4f32-9683-c30949496c60.png)

### Put Request

####**Put Request**

Met deze put request gaan we onze data van de tabel players veranderen die we bij de post hebben ingevoerd.

![image](https://user-images.githubusercontent.com/79090832/211408352-5730e385-de16-4edb-940b-a27ec8338ea4.png)

### Delete Request

#### **Delete Request**

Met onze Delete Request kunnen we data verwijderen uit de tabel van Clubs.

![image](https://user-images.githubusercontent.com/79090832/211409508-2adc8cb6-a9a0-4426-80bf-81dff180ec30.png)

## Screenshot OpenAPi Docs

![image](https://user-images.githubusercontent.com/79090832/211409872-f3753fc2-cd0c-4026-b7f7-b51b267548cb.png)
![image](https://user-images.githubusercontent.com/79090832/211409976-7f24092a-371d-4ec5-9a17-79fa1f8779f2.png)
![image](https://user-images.githubusercontent.com/79090832/211410036-fbd17bcd-230a-4bb2-a646-eebf3cd2772c.png)

## Slot

Als slot zou ik nog graag even willen meedelen dat ik
dit toch een leuke opdracht vond ook al heb ik deze niet afgekregen.
door mijn verkeerde planning kwam ik in tijdsnood en hierdoor had ik te weinig
tijd voorzien om deze opdracht af te maken.






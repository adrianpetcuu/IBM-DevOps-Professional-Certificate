# 🧠 Efectuarea de cereri API folosind cURL și Postman (Making API Requests Using cURL and Postman)

## 🔹 Introducere

După ce un **REST API** a fost creat, acesta trebuie testat pentru a verifica dacă funcționează corect.  
Două dintre cele mai comune instrumente pentru testarea API-urilor sunt **cURL** (Command Line Tool) și **Postman** (aplicație grafică).  

Ambele permit trimiterea de cereri HTTP către API și analizarea răspunsurilor primite.

---

## ⚙️ 1. Testarea API-urilor folosind cURL

### 🔸 Ce este cURL?
**cURL** este un instrument în linie de comandă care permite trimiterea de cereri HTTP (GET, POST, PUT, DELETE etc.) către un server.  
Este disponibil implicit în majoritatea sistemelor Linux și macOS, și poate fi instalat și pe Windows.

---

### 🔸 Exemple de utilizare

#### ▶️ Cerere GET
Obține lista de utilizatori din API:
```bash
curl -X GET https://api.example.com/users
```

#### ▶️ Cerere GET cu antete (headers)
Adăugăm antetul `Accept` pentru a specifica formatul răspunsului:
```bash
curl -X GET https://api.example.com/users -H "Accept: application/json"
```

#### ▶️ Cerere POST
Trimite o cerere pentru a crea un utilizator nou:
```bash
curl -X POST https://api.example.com/users   -H "Content-Type: application/json"   -d '{"name": "Maria", "email": "maria@example.com"}'
```

#### ▶️ Cerere PUT
Actualizează un utilizator existent:
```bash
curl -X PUT https://api.example.com/users/10   -H "Content-Type: application/json"   -d '{"email": "maria.popescu@example.com"}'
```

#### ▶️ Cerere DELETE
Șterge un utilizator după ID:
```bash
curl -X DELETE https://api.example.com/users/10
```

---

### 🔸 Vizualizarea răspunsului API

Răspunsul unui API este, de obicei, în format **JSON**:
```json
{
  "id": 10,
  "name": "Maria",
  "email": "maria.popescu@example.com"
}
```

Pentru a formata frumos răspunsul JSON (pe Linux/macOS), poți folosi:
```bash
curl -s https://api.example.com/users | jq
```

---

## ⚙️ 2. Testarea API-urilor folosind Postman

### 🔸 Ce este Postman?
**Postman** este o aplicație grafică prietenoasă care permite trimiterea de cereri HTTP, analizarea răspunsurilor și automatizarea testelor API.  
Este ideală pentru dezvoltatori, testeri și echipe DevOps.

Poți descărca Postman de aici: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

---

### 🔸 Cum se folosește Postman

1. Deschide aplicația **Postman**.  
2. Creează o cerere nouă (*New Request*).  
3. Alege metoda HTTP (GET, POST, PUT, DELETE).  
4. Introdu adresa URL a API-ului (ex: `https://api.example.com/users`).  
5. Dacă trimiți date, mergi la fila **Body** și selectează formatul **raw → JSON**.  
6. Apasă **Send** pentru a trimite cererea.  
7. Vezi răspunsul API-ului în partea de jos a ecranului (status code, body, headers).

---

### 🔸 Exemple rapide

#### ▶️ GET
Obține toate produsele:
```
GET https://api.example.com/products
```

#### ▶️ POST
Creează un produs nou:
```
POST https://api.example.com/products
Body (JSON):
{
  "name": "Laptop IBM",
  "price": 4999
}
```

#### ▶️ PUT
Actualizează un produs existent:
```
PUT https://api.example.com/products/7
Body (JSON):
{
  "price": 4599
}
```

#### ▶️ DELETE
Șterge un produs după ID:
```
DELETE https://api.example.com/products/7
```

---

## 🔐 Autentificare și securitate

Atât în **cURL**, cât și în **Postman**, poți adăuga antete de autentificare:

### 🔸 Token Bearer (ex: JWT)
```bash
curl -X GET https://api.example.com/users   -H "Authorization: Bearer <tokenul-tău>"
```

În Postman:  
- Mergi la tab-ul **Authorization**.  
- Alege tipul *Bearer Token*.  
- Introdu tokenul tău JWT.

---

## 🧩 Diferențe între cURL și Postman

| Caracteristică | cURL | Postman |
|-----------------|-------|----------|
| Tip | Linia de comandă | Interfață grafică |
| Ușurință de utilizare | Necesită cunoștințe CLI | Ușor de utilizat vizual |
| Automatizare | Poate fi folosit în scripturi | Oferă colecții și teste automate |
| Colaborare | Limitată | Excelentă pentru echipe (Postman Cloud) |
| Export/Import | Prin comenzi text | Prin colecții JSON |

---

## 🏁 Concluzie

Atât **cURL**, cât și **Postman** sunt instrumente esențiale pentru testarea și validarea API-urilor REST.  
- **cURL** este ideal pentru testare rapidă, scripting și automatizare.  
- **Postman** este excelent pentru testare interactivă, vizuală și colaborativă.  

Împreună, ele oferă un ecosistem complet pentru dezvoltarea și testarea API-urilor moderne.

---

📚 *Referințe:*  
- [Postman Learning Center](https://learning.postman.com/)  
- [cURL Documentation](https://curl.se/docs/)  
- [IBM Cloud – Test REST APIs](https://www.ibm.com/cloud/learn/rest-apis)

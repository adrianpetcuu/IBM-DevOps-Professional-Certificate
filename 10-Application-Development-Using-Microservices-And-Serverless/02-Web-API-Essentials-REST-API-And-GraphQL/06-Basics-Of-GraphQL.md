# 🧩 Noțiuni de bază despre GraphQL (Basics of GraphQL)

## 🔹 Introducere

**GraphQL** este un limbaj de interogare pentru API-uri și un runtime care permite clienților să solicite **exact datele de care au nevoie** — nimic mai mult, nimic mai puțin.  
A fost dezvoltat de **Facebook** în 2012 și open-sourcizat în 2015, fiind o alternativă modernă la **REST**.

Prin GraphQL, clientul poate defini structura răspunsului, iar serverul returnează doar datele solicitate.

---

## ⚙️ Cum funcționează GraphQL

Spre deosebire de REST, unde fiecare endpoint returnează un set fix de date, în **GraphQL** există un singur endpoint (de obicei `/graphql`) prin care clientul trimite **interogări (queries)** și **mutații (mutations)**.

Fluxul de lucru:

1. Clientul trimite o cerere GraphQL cu câmpurile dorite.  
2. Serverul procesează cererea și returnează doar datele cerute.  
3. Structura răspunsului reflectă structura cererii.

---

## 🔸 Exemplu comparativ: REST vs GraphQL

### ▶️ REST
Pentru a obține date despre un utilizator și postările sale:
```
GET /users/1
GET /users/1/posts
```
Două cereri separate sunt necesare.

### ▶️ GraphQL
Cu o singură cerere:
```graphql
{
  user(id: 1) {
    name
    email
    posts {
      title
      content
    }
  }
}
```

Răspunsul va fi:

```json
{
  "data": {
    "user": {
      "name": "Maria Popescu",
      "email": "maria@example.com",
      "posts": [
        { "title": "Primul articol", "content": "Conținutul articolului" },
        { "title": "Articol nou", "content": "Alt conținut" }
      ]
    }
  }
}
```

👉 Rezultat: o singură cerere, exact datele necesare.

---

## 🧱 Componentele principale ale GraphQL

| Componentă | Descriere |
|-------------|------------|
| **Schema** | Definește structura datelor disponibile (tipuri, câmpuri, relații). |
| **Query** | O cerere de date (citire). |
| **Mutation** | O operație care modifică datele (creare, actualizare, ștergere). |
| **Resolver** | Funcția care preia datele reale dintr-o sursă (bază de date, API, etc.). |
| **Subscription** | Permite actualizări în timp real (streaming de date). |

---

## 🧠 Exemple de Query și Mutation

### 🔹 Query (citire de date)
```graphql
{
  product(id: 5) {
    name
    price
    category {
      name
    }
  }
}
```

### 🔹 Mutation (modificare de date)
```graphql
mutation {
  addProduct(name: "Laptop IBM", price: 4999, category: "Electronice") {
    id
    name
    price
  }
}
```

### 🔹 Subscription (actualizări în timp real)
```graphql
subscription {
  newProduct {
    id
    name
    price
  }
}
```

---

## 🧩 Avantajele GraphQL

- ✅ Un singur endpoint pentru toate operațiile.  
- ✅ Clienții obțin doar datele de care au nevoie.  
- ✅ Performanță mai bună pentru aplicațiile mobile.  
- ✅ Structură tipizată și documentată (schema).  
- ✅ Se integrează ușor cu microservicii și baze de date diferite.  

---

## ⚠️ Dezavantaje ale GraphQL

- ⚙️ Configurarea inițială este mai complexă decât REST.  
- 📈 Poate necesita optimizări pentru interogări foarte mari.  
- 🔒 Necesită control suplimentar pentru autentificare și rate limiting.  

---

## 🧰 Exemple de implementare

### 🔸 În Node.js (Express + Apollo Server)
```javascript
const { ApolloServer, gql } = require('apollo-server-express');
const express = require('express');

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    email: String!
  }

  type Query {
    users: [User]
  }
`;

const resolvers = {
  Query: {
    users: () => [
      { id: 1, name: 'Ana', email: 'ana@example.com' },
      { id: 2, name: 'Mihai', email: 'mihai@example.com' }
    ]
  }
};

const app = express();
const server = new ApolloServer({ typeDefs, resolvers });
await server.start();
server.applyMiddleware({ app });

app.listen(4000, () => console.log('Serverul rulează pe http://localhost:4000/graphql'));
```

---

### 🔸 În Python (Flask + Graphene)
```python
from flask import Flask
from flask_graphql import GraphQLView
import graphene

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(root, info):
        return [
            User(id=1, name="Ana", email="ana@example.com"),
            User(id=2, name="Mihai", email="mihai@example.com")
        ]

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run()
```

Accesează în browser:
```
http://localhost:5000/graphql
```
pentru a deschide interfața **GraphiQL**, unde poți testa interogări și mutații.

---

## 🧭 GraphQL vs REST

| Caracteristică | GraphQL | REST |
|-----------------|----------|------|
| Endpoint-uri | Un singur endpoint (`/graphql`) | Mai multe endpoint-uri fixe |
| Format date | Flexibil, definit de client | Răspuns fix per endpoint |
| Over-fetching / Under-fetching | Evitat complet | Frecvent |
| Versionare | Nu este necesară | Adesea obligatorie (ex: `/v1/`, `/v2/`) |
| Performanță | Optim pentru cereri complexe | Optim pentru cereri simple |
| Suport pentru real-time | Da (Subscriptions) | Limitat |

---

## 🏁 Concluzie

**GraphQL** este o soluție modernă, flexibilă și eficientă pentru construirea API-urilor.  
El oferă o interfață unificată, tipizată și performantă pentru accesarea și manipularea datelor.

Ideal pentru:
- Aplicații **cloud-native** și **microservicii**.  
- Situații în care clienții (web, mobil, IoT) au nevoi de date diferite.  
- Scenarii care necesită **interogări complexe și optimizare de trafic**.

---

📚 *Referințe:*  
- [GraphQL Official Site](https://graphql.org/)  
- [Apollo GraphQL Documentation](https://www.apollographql.com/docs/)  
- [IBM Developer – GraphQL Basics](https://developer.ibm.com/articles/what-is-graphql/)

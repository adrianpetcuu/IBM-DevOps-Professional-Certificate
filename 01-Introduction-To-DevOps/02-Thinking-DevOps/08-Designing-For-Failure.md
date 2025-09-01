# 🛠️ Designing for Failure

## 🔹 Principiul de bază
- **Eșecul este inevitabil** – în sisteme distribuite și cloud, mereu vor exista erori.  
- Nu încercăm să prevenim toate erorile, ci **proiectăm sisteme care pot continua să funcționeze și să se recupereze rapid**.  

---

## 🔹 Practici esențiale

### 1. Resiliență în aplicații
- Dezvoltatorii trebuie să includă **mecanisme de rezistență** (self-healing, retry, fallback).  
- Obiectiv: sistemul să se recupereze rapid după un eșec.

### 2. Retry Patterns
- Operațiile eșuate sunt reluate automat după un anumit timp.  
- Evită pierderea datelor sau blocarea proceselor.  

### 3. Circuit Breaker Pattern
- Detectează serviciile care eșuează frecvent și **întrerupe conexiunile** temporar.  
- Evită **cascading failures** (erori care se propagă în întregul sistem).  

### 4. Bulkhead Pattern
- Inspirat din compartimentele navelor 🚢 – dacă un compartiment ia apă, restul nu se scufundă.  
- În software: izolează serviciile defecte ca să nu afecteze întregul sistem.  

### 5. Chaos Engineering
- Practica de a provoca intenționat eșecuri pentru a observa **cum reacționează sistemul**.  
- Exemple: Netflix **Chaos Monkey** 🐒.  
- Ajută la descoperirea punctelor slabe din infrastructură.  

---

## 🔹 Concluzie
- **Designing for Failure** = acceptarea faptului că erorile vor apărea.  
- Scopul este să construim aplicații **reziliente, fault-tolerant și auto-recuperabile**.  
- Tehnici precum **retry, circuit breaker, bulkhead și chaos engineering** sunt esențiale pentru aplicațiile cloud-native.  

✅ În DevOps și cloud computing, **fail fast & recover fast** este regula de aur.

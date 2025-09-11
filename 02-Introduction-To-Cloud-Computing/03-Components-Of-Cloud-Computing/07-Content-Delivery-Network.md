# Content Delivery Network (CDN)

## 📌 Ce este un CDN?
Un **Content Delivery Network (CDN)** este o rețea de servere distribuite la nivel global, care lucrează împreună pentru a livra rapid conținutul utilizatorilor finali.  
Conținutul static (imagini, fișiere video, CSS, JavaScript) este **copiat și stocat în cache** pe mai multe servere edge din apropierea utilizatorilor.

---

## ⚙️ Cum funcționează?
1. Utilizatorul face o cerere pentru un conținut (ex: un video sau o imagine).
2. Cererea este direcționată automat către serverul CDN cel mai apropiat geografic.
3. Dacă acel server are conținutul în cache, îl livrează imediat.  
   Dacă nu, îl cere din serverul de origine, îl salvează în cache și îl livrează utilizatorului.

---

## ✅ Avantajele utilizării CDN
- **Viteză crescută**: scade latența prin servirea conținutului din apropierea utilizatorilor.
- **Scalabilitate**: gestionează volume mari de trafic simultan (ideal pentru campanii, evenimente live).
- **Disponibilitate**: conținutul este servit chiar și dacă serverul de origine are probleme.
- **Securitate**: multe CDN-uri oferă protecție împotriva atacurilor DDoS.
- **Reducerea încărcării pe serverul principal**: traficul este preluat de serverele edge.

---

## 📌 Cazuri de utilizare
- Site-uri web cu trafic internațional.
- Platforme de streaming video și audio (Netflix, YouTube).
- Magazine online (e-commerce) cu mulți utilizatori simultan.
- Actualizări software distribuite global (Microsoft, Apple, Steam).

---

## 🔑 Exemple de CDN populare
- **Cloudflare CDN**
- **Akamai**
- **Amazon CloudFront (AWS)**
- **Google Cloud CDN**
- **Microsoft Azure CDN**

---

## 🎯 Concluzie
Un **CDN** este esențial pentru:
- Reducerea latenței,
- Îmbunătățirea experienței utilizatorilor,
- Creșterea performanței și securității aplicațiilor distribuite global.

# 📘 Overview of Linux Architecture  

Linux are o arhitectură pe straturi, unde fiecare nivel are rolul său. Înțelegerea acestei structuri ajută la înțelegerea modului în care funcționează sistemul.  

---

## 🔹 Straturile arhitecturii Linux  

### 1. **Hardware**  
- Include procesorul, memoria, hard disk-ul, placa de rețea și alte componente fizice.  
- Kernel-ul comunică direct cu hardware-ul pentru a-l gestiona.  

---

### 2. **Kernel (Nucleul Linux)**  
- Este inima sistemului de operare.  
- Roluri principale:  
  - Gestionează **procesele** (executarea programelor).  
  - Gestionează **memoria** (alocare și eliberare).  
  - Gestionează **dispozitivele** (intrare/ieșire, drivere).  
  - Gestionează **sistemul de fișiere**.  
- Kernel-ul rulează în **mode kernel** (nivel de privilegii ridicat).  

---

### 3. **Shell**  
- Interfața dintre utilizator și kernel.  
- Primește comenzile introduse de utilizator și le transmite către kernel.  
- Exemple de shell-uri:  
  - **Bash (Bourne Again Shell)** – cel mai comun.  
  - Zsh, Fish, Ksh.  
- Poate fi folosit **interactiv** (comenzi introduse manual) sau prin **scripturi**.  

---

### 4. **Aplicații și Utilizatori**  
- Programe rulate de utilizatori: browsere web, editoare de text, servere, jocuri etc.  
- Aceste aplicații nu comunică direct cu hardware-ul, ci prin shell și kernel.  

---

## 🔹 Reprezentare schematică  
+-------------------------+

| Aplicații / Utilizatori |

+-------------------------+

| Shell |

+-------------------------+

| Kernel |

+-------------------------+

| Hardware |

+-------------------------+

---

## 🔹 Pe scurt  
- **Hardware** = partea fizică.  
- **Kernel** = inima sistemului, gestionează resursele.  
- **Shell** = interfață pentru utilizatori și scripturi.  
- **Aplicații** = programe rulate la nivelul utilizatorului.  

# 🏗️ Infrastructure as Code (IaC)

## 🔹 Ce este Infrastructure as Code (IaC)?

**Infrastructure as Code (IaC)** este o practică DevOps prin care **infrastructura IT este definită și gestionată folosind cod**, la fel ca aplicațiile software.  
În loc să configurezi manual servere, rețele și baze de date, totul este descris într-un fișier de cod (ex: YAML, JSON, HCL).  

Astfel, infrastructura devine:
- **Automatizată** – se poate crea, modifica și distruge prin scripturi.  
- **Reproductibilă** – aceleași configurații pot fi refăcute oriunde, oricând.  
- **Versionată** – schimbările sunt urmărite în Git, exact ca în codul aplicației.  

---

## ⚙️ Cum funcționează IaC

1. **Definire** – infrastructura dorită este descrisă în fișiere de configurare (ex: rețele, servere, containere, baze de date).  
2. **Executare** – un instrument IaC interpretează fișierele și creează automat resursele necesare.  
3. **Versionare** – fișierele IaC sunt salvate în controlul versiunilor (Git), permițând rollback și colaborare.  
4. **Validare și testare** – se pot rula teste automate pentru a verifica dacă infrastructura respectă cerințele.  

---

## 🧩 Tipuri de abordări IaC

| Abordare | Descriere | Exemple de tool-uri |
|-----------|------------|----------------------|
| **Declarativă** | Definiți *starea dorită* a infrastructurii, iar instrumentul decide cum să ajungă acolo. | Terraform, CloudFormation, Kubernetes YAML |
| **Imperativă** | Specifici *pașii exacți* care trebuie executați pentru a crea infrastructura. | Ansible, Chef |
| **Funcțională** | Descrii infrastructura prin funcții reutilizabile și compoziție de module. | Pulumi (bazat pe Python/TypeScript) |

---

## 🧠 Beneficiile folosirii IaC

- ⚙️ **Automatizare completă** – elimină configurațiile manuale.  
- 📋 **Consistență și repetabilitate** – aceleași configurații pot fi aplicate pe multiple medii (dev, test, prod).  
- 🔄 **Versionare și istoric al modificărilor** – fiecare schimbare este urmărită în Git.  
- 🚀 **Scalare rapidă** – poți adăuga sau elimina resurse instant.  
- 🧩 **Integrare perfectă cu CI/CD** – infrastructura se actualizează automat în pipeline-uri.  
- 👥 **Colaborare ușoară** – echipele pot lucra împreună pe aceleași fișiere de infrastructură.  

---

## 🧰 Exemple populare de instrumente IaC

### 🏗️ **Terraform**
- Limbaj: HashiCorp Configuration Language (HCL).  
- Abordare: *Declarativă*.  
- Creează, modifică și distruge infrastructura în mod automat.  
- Poate lucra cu mai mulți provideri cloud (AWS, Azure, Google Cloud, IBM Cloud).  
- Comenzi principale:
  ```bash
  terraform init
  terraform plan
  terraform apply
  terraform destroy
  ```

---

### ⚙️ **Ansible**
- Limbaj: YAML.  
- Abordare: *Imperativă și declarativă hibrid*.  
- Ușor de utilizat, rulează prin SSH fără agent.  
- Folosește fișiere de tip **playbook** și **inventory**:
  ```yaml
  - hosts: webservers
    tasks:
      - name: Instalează Apache
        apt:
          name: apache2
          state: present
  ```

---

### 🍳 **Chef**
- Limbaj: Ruby.  
- Abordare: *Imperativă*.  
- Descrie pașii pentru a ajunge la o stare finală prin “recipes” și “cookbooks”.  

---

### 🧱 **AWS CloudFormation**
- Limbaj: JSON / YAML.  
- Abordare: *Declarativă*.  
- Instrument nativ AWS pentru definirea infrastructurii cloud.  

---

## 🧮 Exemple de fișiere IaC

Exemplu Terraform simplu (crearea unei mașini virtuale pe AWS):

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "DemoServer"
  }
}
```

---

## 🧭 Pe scurt

> **Infrastructure as Code (IaC)** transformă infrastructura dintr-un proces manual într-unul complet automatizat și repetabil.  
> Cu IaC, serverele, rețelele și serviciile cloud devin parte din codul tău — ceea ce înseamnă **viteză, control și siguranță**.

---

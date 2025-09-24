# GitHub Repositories

## Ce este un Repository?
- Un **repository** (sau repo) este o structură de stocare unde se află:
  - Codul sursă al aplicației
  - Documentația proiectului
  - Istoricul modificărilor (commits)
  - Alte resurse necesare dezvoltării
- Poate fi:
  - **Public** – vizibil tuturor utilizatorilor GitHub
  - **Privat** – accesibil doar echipei sau persoanelor autorizate

## Tipuri de Repository
- **Local Repository**
  - Stocat pe calculatorul dezvoltatorului
  - Permite lucrul offline și păstrează istoricul complet
- **Remote Repository**
  - Găzduit pe GitHub
  - Folosit pentru partajarea și sincronizarea codului între colaboratori

## Cum creezi un Repository pe GitHub
- Autentifică-te pe [GitHub](https://github.com)
- Click pe butonul **New Repository**
- Introdu:
  - Numele proiectului
  - O descriere (opțional)
  - Setează vizibilitatea: **Public** sau **Private**
- Opțional:
  - Adaugă un fișier **README.md** pentru descrierea proiectului
  - Adaugă un fișier **.gitignore** pentru a exclude fișiere nedorite
  - Alege o **licență** pentru cod
- Apasă **Create Repository**

## Cum conectezi Repository-ul local cu GitHub
```bash
- git init
- git remote add origin https://github.com/utilizator/nume-repo.git
- git push -u origin main
```
## Elemente cheie într-un Repository
- **README.md** – descrierea proiectului
- **LICENSE** – arată cum poate fi folosit codul
- **.gitignore** – specifică fișierele ignorate de Git
- **Commits** – istoricul modificărilor
- **Branches** – dezvoltarea paralelă a funcționalităților

## Beneficii ale Repository-urilor pe GitHub
- Colaborare ușoară cu alți dezvoltatori
- Păstrarea centralizată a codului
- Vizibilitate și transparență în contribuții
- Integrare cu alte servicii (CI/CD, code review, project boards)

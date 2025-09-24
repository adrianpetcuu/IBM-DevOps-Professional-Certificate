# GitHub Branches

## Ce este un Branch?
- Un **branch** este o ramură separată a repository-ului
- Permite dezvoltatorilor să lucreze la funcționalități noi sau la fix-uri de bug-uri
- Avantajul este că nu afectează codul din ramura principală (**main** sau **master**) până când nu este finalizat

## De ce folosim Branches?
- Permite lucrul în paralel la mai multe funcționalități
- Reduce riscul de a strica codul stabil din ramura principală
- Ajută echipele să colaboreze mai organizat
- Oferă un flux de lucru mai clar: dezvoltare → testare → integrare

## Cum creezi un Branch
```bash
- git branch nume-branch
```

## Cum te muți pe un Branch
```bash
- git checkout nume-branch
```

sau din Git 2.23+
```bash
- git switch nume-branch
```

## Cum creezi și schimbi branch-ul dintr-o singură comandă
```bash
- git checkout -b nume-branch
```

## Cum vizualizezi branch-urile existente
```bash
- git branch
```

## Cum trimiți branch-ul pe GitHub
```bash
- git push -u origin nume-branch
```

---

# Merging (Îmbinarea branch-urilor)

## Ce este Merging?
- Procesul prin care modificările dintr-un branch se combină cu un alt branch (de obicei în **main**)
- Se face atunci când funcționalitatea este gata și testată

## Cum faci un Merge
```bash
- git checkout main
- git pull origin main
- git merge nume-branch
```

## Rezolvarea conflictelor
- Dacă două persoane au modificat aceleași linii de cod, apare un **conflict**
- Git marchează conflictele în fișiere
- Tu trebuie să editezi manual fișierele pentru a alege varianta corectă
- După rezolvare:
```bash
- git add nume-fisier
- git commit -m "Rezolvat conflictele la merge"
```

---

## Alternative: Pull Requests pe GitHub
- În loc de `git merge` local, poți deschide un **Pull Request** pe GitHub
- Avantaje:
  - Codul este revizuit de colegi înainte de integrare
  - Discuții și comentarii pe modificări
  - Integrare mai sigură și transparentă

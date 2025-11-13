# Componentele unui Pipeline DevOps

Un pipeline DevOps este o succesiune automatizată de procese care permite echipelor să construiască, testeze și livreze software-ul mai rapid și mai sigur.  
Acesta este format din mai multe etape (stages) și componente (tools/processes) care lucrează împreună pentru a asigura o livrare continuă și de înaltă calitate.

---

## 1. **Planificare (Planning)**

Aceasta este etapa în care echipele definesc:
- cerințele aplicației,
- obiectivele sprintului,
- task‑uri,
- estimări.

### Instrumente utilizate:
- Jira  
- GitHub Projects  
- Azure Boards  
- Trello  

---

## 2. **Gestionarea Codului Sursă (Source Code Management - SCM)**

Reține și versionarea codului.  
Este centrul colaborării dintre dezvoltatori.

### Instrumente:
- Git  
- GitHub / GitLab  
- Bitbucket  
- Azure Repos  

---

## 3. **Construire (Build)**

Convertirea codului sursă în artefacte executabile.  
Include instalarea dependențelor, compilare, packaging.

### Instrumente:
- Maven  
- Gradle  
- npm / yarn  
- Docker (pentru build imagini)  

---

## 4. **Testare (Testing)**

Validarea funcțională și non-funcțională a aplicației.

### Tipuri de teste:
- Unit tests  
- Integration tests  
- Performance tests  
- Security scans  

### Instrumente:
- JUnit  
- Selenium  
- Cypress  
- SonarQube  
- OWASP ZAP  

---

## 5. **Integrare Continuă (CI – Continuous Integration)**

Combinarea automată a codului nou în aplicație prin rularea de build + teste.

### Instrumente:
- Jenkins  
- GitHub Actions  
- GitLab CI  
- Tekton  
- CircleCI  

---

## 6. **Livrare Continuă (CD – Continuous Delivery/Deployment)**

Automatizează livrarea aplicației către medii precum Dev, QA, Prod.

### Instrumente:
- Tekton  
- Argo CD  
- Spinnaker  
- Jenkins X  

---

## 7. **Monitorizare și Observabilitate (Monitoring & Observability)**

Asigură funcționarea aplicației în producție și detectarea rapidă a problemelor.

### Instrumente:
- Prometheus  
- Grafana  
- OpenTelemetry  
- ELK Stack (Elasticsearch + Logstash + Kibana)  
- Datadog  

---

## 8. **Managementul Artei (Artifact Management)**

Păstrează build-urile, imaginile Docker, binarele.

### Instrumente:
- Nexus  
- JFrog Artifactory  
- GitHub Packages  
- Docker Hub  
- Quay.io  

---

## 9. **Securitate în DevOps (DevSecOps)**

Integrarea securității în toate etapele pipeline-ului.

### Componente:
- Vulnerability scanning  
- Dependency scanning  
- Secret scanning  

### Instrumente:
- Trivy  
- Snyk  
- Aqua Security  

---

## 10. **Automatizare și Orchestrare**

Automatizarea proceselor și gestionarea resurselor containerizate.

### Instrumente:
- Kubernetes  
- OpenShift  
- Helm  
- Terraform  

---

## Concluzie

Un pipeline DevOps complet include:
- planificare,  
- versionare cod,  
- build,  
- testare,  
- CI/CD,  
- securitate,  
- monitorizare,  
- management de artefacte.

Scopul final este **automatizarea completă și livrarea software-ului rapid, sigur și fiabil**.


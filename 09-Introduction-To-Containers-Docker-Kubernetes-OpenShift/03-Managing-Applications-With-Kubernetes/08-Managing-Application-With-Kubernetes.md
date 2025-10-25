# ⚙️ Administrarea Aplicațiilor cu Kubernetes

Acest tabel conține cele mai utilizate comenzi `kubectl` pentru gestionarea aplicațiilor în Kubernetes, împreună cu descrierea lor.

---

| Comandă | Descriere |
|----------|------------|
| **kubectl autoscale deployment** | Auto-scalează un Deployment în Kubernetes (adaugă sau elimină pod-uri în funcție de sarcină). |
| **kubectl create configmap** | Creează o resursă de tip **ConfigMap** pentru a stoca date de configurare neconfidențiale. |
| **kubectl get deployments -o wide** | Listează toate **Deployment-urile** existente, împreună cu detalii suplimentare (imagine, nod, stare). |
| **kubectl get hpa** | Afișează toate obiectele de tip **Horizontal Pod Autoscaler (HPA)** din cluster. |
| **kubectl scale deployment** | Scalează manual un Deployment, modificând numărul de replici (pod-uri). |
| **kubectl set image deployment** | Actualizează imaginea (container image) utilizată de un Deployment. |
| **kubectl rollout** | Gestionează procesul de **rollout** al unei resurse (verificare stare, istoric etc.). |
| **kubectl rollout restart** | Repornește resursa (Deployment, DaemonSet, etc.), forțând repornirea containerelor. |
| **kubectl rollout undo** | Revine la o versiune anterioară a Deployment-ului (rollback). |


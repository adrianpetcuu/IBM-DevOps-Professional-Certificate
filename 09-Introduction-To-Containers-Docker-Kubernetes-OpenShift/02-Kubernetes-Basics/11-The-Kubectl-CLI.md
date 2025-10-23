# 📘 Fișă rapidă: Înțelegerea arhitecturii Kubernetes (Cheat Sheet)

Această fișă oferă o privire de ansamblu asupra comenzilor esențiale Kubernetes, utile pentru administrarea resurselor, gestionarea contextelor și monitorizarea aplicațiilor dintr-un cluster.

---

## ⚙️ Comenzi de bază Kubernetes

| **Comandă** | **Descriere** |
|--------------|---------------|
| `for …do` | Rulează o comandă `for` de mai multe ori, conform specificației. |
| `kubectl apply` | Aplică o configurație asupra unei resurse (creează sau actualizează). |
| `kubectl config get-clusters` | Afișează toate clusterele definite în fișierul `kubeconfig`. |
| `kubectl config get-contexts` | Afișează toate contextele disponibile și indică contextul curent. |
| `kubectl create` | Creează o resursă nouă pe baza unui fișier YAML sau a parametrilor specificați. |
| `kubectl delete` | Șterge una sau mai multe resurse din cluster. |
| `kubectl describe` | Afișează detalii complete despre o resursă sau un grup de resurse. |
| `kubectl expose` | Expune o resursă ca serviciu Kubernetes accesibil în rețea. |
| `kubectl get` | Listează resursele existente (pods, servicii, deploymenturi etc.). |
| `kubectl get pods` | Listează toate podurile din namespace-ul curent. |
| `kubectl get pods -o wide` | Listează toate podurile cu detalii suplimentare (noduri, IP-uri etc.). |
| `kubectl get deployments` | Listează toate deploymenturile create în cluster. |
| `kubectl get services` | Listează toate serviciile configurate în cluster. |
| `kubectl proxy` | Creează un server proxy între localhost și API server-ul Kubernetes. |
| `kubectl run` | Creează și rulează o imagine specificată într-un pod nou. |
| `kubectl version` | Afișează informații despre versiunile clientului și serverului Kubernetes. |



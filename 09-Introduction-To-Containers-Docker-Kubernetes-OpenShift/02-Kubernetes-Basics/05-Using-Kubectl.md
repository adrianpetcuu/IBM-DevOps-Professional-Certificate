# ☸️ Using kubectl - README

## 🔹 Ce este kubectl

**kubectl** este **interfața în linie de comandă (CLI)** pentru
Kubernetes.\
Este principalul instrument folosit pentru a **interacționa cu un
cluster Kubernetes**, pentru a crea, vizualiza, gestiona și șterge
resurse (pods, services, deployments, etc).

> Cu kubectl, poți comunica cu Kubernetes API Server-ul și îi poți spune
> ce vrei să facă --- adică să aplice modificări, să redea informații
> sau să diagnosticheze probleme.

------------------------------------------------------------------------

## 🧩 Cum funcționează kubectl

Fluxul este următorul:

    kubectl → Kubernetes API Server → Control Plane → Worker Nodes

-   Tu tastezi o comandă (ex: `kubectl get pods`)
-   `kubectl` trimite cererea către API Server
-   API Server verifică permisiunile și trimite datele sau execută
    acțiunea
-   Rezultatul este returnat în terminalul tău

------------------------------------------------------------------------

## ⚙️ Configurarea kubectl

Pentru a folosi kubectl, trebuie să ai un fișier de configurare numit
**kubeconfig** (de obicei în `~/.kube/config`), care conține:

-   adresa serverului API (`server:`)
-   certificatul de autentificare
-   contextul curent (cluster + utilizator + namespace)

Exemplu de context:

``` bash
kubectl config get-contexts
kubectl config use-context my-cluster
```

------------------------------------------------------------------------

## 🧱 Comenzi de bază kubectl

### 🔹 1️⃣ Vizualizarea resurselor

  --------------------------------------------------------------------------
  Comandă                             Descriere
  ----------------------------------- --------------------------------------
  `kubectl get pods`                  Listează toate podurile din
                                      namespace-ul curent

  `kubectl get pods -A`               Listează podurile din toate
                                      namespace-urile

  `kubectl get deployments`           Afișează toate deployment-urile

  `kubectl get svc`                   Listează serviciile active

  `kubectl get nodes`                 Afișează nodurile din cluster

  `kubectl describe pod <nume_pod>`   Afișează detalii despre un pod (stare,
                                      evenimente, IP etc.)
  --------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 2️⃣ Crearea și aplicarea resurselor

  ------------------------------------------------------------------------
  Comandă                           Descriere
  --------------------------------- --------------------------------------
  `kubectl create -f file.yaml`     Creează o resursă pe baza fișierului
                                    YAML

  `kubectl apply -f file.yaml`      Aplică sau actualizează o resursă
                                    (recomandat pentru CI/CD)

  `kubectl delete -f file.yaml`     Șterge o resursă pe baza fișierului
                                    YAML

  `kubectl delete pod <nume_pod>`   Șterge un pod (va fi recreat automat
                                    dacă e gestionat de un Deployment)
  ------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 3️⃣ Interacțiunea cu poduri

  -----------------------------------------------------------------------------------
  Comandă                                      Descriere
  -------------------------------------------- --------------------------------------
  `kubectl logs <nume_pod>`                    Afișează logurile unui pod

  `kubectl exec -it <nume_pod> -- /bin/bash`   Deschide un terminal interactiv în
                                               container

  `kubectl port-forward <nume_pod> 8080:80`    Redirecționează traficul local către
                                               portul din pod

  `kubectl cp <nume_pod>:/path/to/file ./`     Copiază un fișier din pod în sistemul
                                               tău local
  -----------------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 4️⃣ Gestionarea namespace-urilor

  -----------------------------------------------------------------------------------------------
  Comandă                                                  Descriere
  -------------------------------------------------------- --------------------------------------
  `kubectl get namespaces`                                 Listează namespace-urile existente

  `kubectl create namespace dev`                           Creează un nou namespace

  `kubectl config set-context --current --namespace=dev`   Setează namespace-ul implicit

  `kubectl delete namespace dev`                           Șterge un namespace (atenție: șterge
                                                           și toate resursele din el!)
  -----------------------------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 5️⃣ Monitorizarea clusterului

  ------------------------------------------------------------------------
  Comandă                           Descriere
  --------------------------------- --------------------------------------
  `kubectl top nodes`               Afișează utilizarea resurselor pe
                                    noduri

  `kubectl top pods`                Afișează consumul de CPU/RAM per pod

  `kubectl get events`              Listează evenimentele recente din
                                    cluster

  `kubectl get componentstatuses`   Verifică starea componentelor
                                    principale Kubernetes
  ------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 6️⃣ Gestionarea deployment-urilor

  -------------------------------------------------------------------------------------------------------
  Comandă                                                          Descriere
  ---------------------------------------------------------------- --------------------------------------
  `kubectl rollout status deployment/<nume>`                       Verifică progresul unui rollout

  `kubectl rollout undo deployment/<nume>`                         Revine la o versiune anterioară a
                                                                   aplicației

  `kubectl scale deployment <nume> --replicas=5`                   Schimbă numărul de replici manual

  `kubectl set image deployment/<nume> container=<noua_imagine>`   Actualizează imaginea rulată
  -------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

### 🔹 7️⃣ Export, backup și debugging

  ---------------------------------------------------------------------------------
  Comandă                                    Descriere
  ------------------------------------------ --------------------------------------
  `kubectl get all -o yaml > backup.yaml`    Exportă toate resursele dintr-un
                                             namespace

  `kubectl get pod <nume> -o json`           Afișează informațiile unui pod în
                                             format JSON

  `kubectl describe node <nume>`             Afișează detalii și stare pentru un
                                             nod

  `kubectl get logs <nume_pod> --previous`   Vezi logurile dintr-un container care
                                             s-a restartat
  ---------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Moduri de output în kubectl

Poți schimba modul în care sunt afișate rezultatele:

  ----------------------------------------------------------------------------------
  Format                Exemplu                           Descriere
  --------------------- --------------------------------- --------------------------
  `-o wide`             `kubectl get pods -o wide`        Afișează detalii
                                                          suplimentare (IP, nod,
                                                          container)

  `-o yaml`             `kubectl get pod nginx -o yaml`   Afișează configurația YAML
                                                          completă

  `-o json`             `kubectl get svc -o json`         Afișează în format JSON

  `--watch`             `kubectl get pods --watch`        Monitorizează live
                                                          modificările în resurse
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🔒 Autentificare și acces

Kubectl folosește fișierele de configurare din `~/.kube/config` pentru a
autentifica utilizatorii.\
Poți vizualiza și schimba contextul actual:

``` bash
kubectl config view
kubectl config current-context
kubectl config use-context my-cluster
```

Pentru gestionarea conturilor de utilizatori și permisiunilor se
folosesc obiectele **ServiceAccount**, **Role** și **RoleBinding**.

------------------------------------------------------------------------

## 💡 Sfaturi utile pentru kubectl

-   Folosește **aliasuri** pentru comenzi frecvente:

    ``` bash
    alias k=kubectl
    alias kgp='kubectl get pods'
    ```

-   Autocomplete:

    ``` bash
    source <(kubectl completion bash)
    ```

-   Verifică rapid versiunea:

    ``` bash
    kubectl version --short
    ```

-   Creează rapid o resursă temporară pentru testare:

    ``` bash
    kubectl run test-nginx --image=nginx --port=80
    ```

------------------------------------------------------------------------

## ✅ Concluzie

**kubectl** este instrumentul esențial pentru lucrul cu Kubernetes.\
El permite controlul total asupra aplicațiilor, resurselor și
configurațiilor din cluster.

> Cu kubectl poți construi, scala, depana și administra un întreg sistem
> Kubernetes dintr-o singură linie de comandă.

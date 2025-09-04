# ☁️ Overview of Cloud Infrastructure

## 📌 Ce este infrastructura cloud?
Cloud infrastructure reprezintă ansamblul de resurse și servicii IT livrate prin cloud, care includ:
- **Data centers** (centre de date)
- **Storage** (stocare)
- **Networking** (rețelistică)
- **Compute resources** (resurse de procesare)

---

## 🖥️ Virtualizare și Hypervisors
- **Virtualization** = procesul prin care resursele fizice sunt transformate în resurse software.
- Se face prin **hypervisors** (ex: VMware ESX, KVM, Hyper-V).
- Permite rularea mai multor **Virtual Machines (VMs)** pe același hardware.

### 🔹 Tipuri de VM-uri în Cloud
1. **Shared/Public Cloud VMs** – multi-tenant, administrate de furnizor.  
2. **Transient/Spot VMs** – folosesc resurse neutilizate, cost redus.  
3. **Reserved VMs** – rezervă resurse pentru viitor.  
4. **Dedicated hosts** – servere virtuale izolate pentru un singur client.  
5. **Bare metal servers** – servere fizice dedicate (single-tenant), ideale pentru **HPC** și aplicații cu cerințe stricte de securitate.

---

## 🌐 Rețelistică în Cloud
- Furnizată ca **serviciu**, nu ca echipamente fizice.  
- Resursele (VMs, storage, networking, load balancers) sunt implementate în **Virtual Private Clouds (VPCs)**.  
- **Subnets (subrețele)** → principalele zone unde se implementează securitatea.  
- **Load balancers** → distribuie traficul și mențin aplicațiile responsive.

---

## 📦 Containere
- Unități executabile de software ce includ **cod, librării și dependențe**.  
- Pot rula oriunde: pe desktop, servere tradiționale sau cloud.  
- **Mai ușoare decât VM-urile** și consumă mai puține resurse.  
- Esențiale pentru aplicațiile **cloud-native** și microservicii.  

---

## ✅ Beneficii cheie ale infrastructurii cloud
- **Scalabilitate** (poți adăuga sau reduce resurse rapid).  
- **Flexibilitate** (multiple opțiuni: VMs, bare metal, containere).  
- **Cost-eficiență** (plătești doar ce folosești).  
- **Securitate și izolare** prin subrețele, load balancers și opțiuni dedicate.  
- **Inovație rapidă** prin utilizarea containerelor și a aplicațiilor cloud-native.  

---

## 📝 Concluzie
Infrastructura cloud oferă baza pentru orice serviciu cloud (IaaS, PaaS, SaaS).  
Prin combinația dintre **centre de date, virtualizare, rețelistică, containere și bare metal**, organizațiile își pot scala și securiza aplicațiile într-un mod flexibil și eficient.

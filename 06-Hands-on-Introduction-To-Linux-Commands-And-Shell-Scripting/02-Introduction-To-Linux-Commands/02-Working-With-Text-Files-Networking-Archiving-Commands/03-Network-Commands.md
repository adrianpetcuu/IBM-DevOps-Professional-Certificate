# 📘 Networking Commands in Linux

Acest document prezintă comenzile utilizate pentru configurarea și testarea rețelelor în Linux.

---

## 🔹 hostname
- Afișează sau setează numele gazdei sistemului.
```bash
hostname             # afișează numele curent
sudo hostname nou_nume   # setează un nou hostname
```

---

## 🔹 ip
- Afișează informații despre interfețele de rețea și IP-uri.
```bash
ip a        # arată toate interfețele și adresele IP
ip link     # afișează interfețele de rețea
ip route    # afișează rutele de rețea
```

---

## 🔹 ping
- Testează conectivitatea la un host sau o adresă IP.
```bash
ping google.com
ping -c 4 8.8.8.8   # trimite doar 4 pachete
```

---

## 🔹 curl
- Transferă date de la și către un URL (HTTP, HTTPS, FTP etc.).
```bash
curl http://example.com
curl -O http://example.com/fisier.zip   # descarcă un fișier
```

---

## 🔹 wget
- Descarcă fișiere de la un URL.
```bash
wget http://example.com/fisier.zip
wget -c http://example.com/fisier.zip   # continuă descărcarea dacă s-a întrerupt
```

---

## 🔹 Pe scurt
- **hostname** → numele gazdei.  
- **ip** → informații despre interfețe și IP-uri.  
- **ping** → test conexiune.  
- **curl** → transfer de date.  
- **wget** → descărcare fișiere.  

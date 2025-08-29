
## 📌 Project Overview  
This project demonstrates the use of **DNSDumpster**, an open-source DNS reconnaissance and OSINT tool, to analyze the DNS infrastructure of the domain **iana.org**.  
The goal was to collect DNS records, subdomains, hosting/network details, and service banners, and then evaluate them from a **cybersecurity perspective**.  

---

## ⚙️ Tools & Technologies Used  
- **DNSDumpster** – For DNS reconnaissance and OSINT  
- **Internet WHOIS & ASN Data** – To identify network owners  
- **Python / Pandas / Matplotlib** – For table generation and formatting  
- **Report Writing** – Structured documentation in academic format  

---

## 📡 DNS Records Analyzed  
- **A Records** → IPv4 addresses mapping domain names to servers  
- **AAAA Records** → IPv6 address mappings  
- **NS Records** → Authoritative DNS servers for the domain  
- **MX Records** → Mail servers responsible for email delivery  
- **TXT Records** → Security configurations (SPF, DKIM, DMARC, verification)  

---

## 🌍 Hosting / Network Findings  
- ICANN Data Centers (LAX, DC)  
- ICANN Anycasted Services (global redundancy)  
- AS112 Project (misdirected reverse DNS queries)  
- FASTLY CDN (content distribution & performance optimization)  

---

## 🛡️ Services & Banners (Security Perspective)  
- Apache, Nginx, GitHub Hosting detected  
- FTP banner message (`421 Please use ftp.iana.org`)  
- **Security Takeaways:**  
  - Exposed banners reveal server versions → possible vulnerabilities  
  - Helps attackers in service fingerprinting  
  - Defenders should minimize banner exposure  
  - Supports network segmentation and strict access control  

---

## 📑 Learning Outcomes  
- Understood practical **DNS footprinting & enumeration**  
- Learned interpretation of DNS records and hosting data  
- Gained skills in identifying **attack surfaces** via OSINT  
- Recognized importance of **banner hardening** and **DNS hygiene**  

---

## 🙏 Acknowledgment  
I would like to express my sincere gratitude to my faculty **Mr. U. Sai Ram** for his continuous guidance and support during this project.  
I also acknowledge the use of **dnsdumpster.com** as a key resource for performing DNS reconnaissance.  

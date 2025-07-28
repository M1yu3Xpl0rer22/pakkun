# pakkun
 Pakkun — Subdomain Takeover Detection Tool

 # 🥷 Pakkun — Subdomain Takeover Detection Tool

**Pakkun** is a lightweight Python tool designed for educational and ethical security research. It scans a list of subdomains and checks for potential subdomain takeover vulnerabilities and misconfigurations like default server pages or unclaimed third-party services.

---

## ✨ Features

- 🔍 Detects subdomain takeover opportunities (CNAME or HTTP-based)
- 📡 Identifies known 3rd-party services (GitHub Pages, Heroku, AWS S3, Netlify, etc.)
- ⚠️ Detects misconfigured servers (e.g. IIS 404, Plesk default pages)
- 📝 Logs clean output to `.txt` files (no CSV, easy to read)
- ⚡ Fast multithreaded scanning
- ✅ Works on both **Linux** and **Windows**

---

## ⚙️ Requirements

- Python 3.7+
- `requests`
- `dnspython`
- `colorama`

### 🔧 Install Requirements:

pip install -r requirements.txt

---

### 🚀 Usage:

🧾 Step 1: Prepare Your Subdomain List
Create a file called subdomains.txt:

lua
Copy
Edit
blog.example.com
cdn.example.com
test.herokuapp.com
ghostsite.github.io
mysite.netlify.app

---

### ▶️ Step 2: Run the Tool:
On Linux/macOS:
python3 subdomain_takeover_scanner.py subdomains.txt

On Windows:
python subdomain_takeover_scanner.py subdomains.txt

---



### 🔍 Example Usage & Output
Sample Command:
python subdomain_takeover_scanner.py subdomains.txt

Sample Terminal Output:
[TAKEOVER-POSSIBLE] ghostsite.github.io → github.io (GitHub Pages)
[UNCLAIMED-SERVICE] test.herokuapp.com → Heroku (Unclaimed)
[INFO] cdn.example.com → Plesk Default Page
[OK] blog.example.com → HTTP 200 (Active / No Fingerprint)
[UNREACHABLE] unknown.example.com

---


### 📁 Output Files
File Name	Description
takeover_results.txt	Full scan log (all scanned subdomains + findings)
vuln_only.txt	Only subdomains with possible takeover risks

---

### 📜 License
MIT License — see LICENSE for more details.

---

# 🛡️ Ethical Notice:
This tool is made for educational and authorized testing only.
Do not use against domains you don’t own or control.
Unauthorized scanning may violate local laws and terms of service.

---

# 👨‍🎓 Built For Students
Pakkun is created for student researchers, bug bounty beginners, and cybersecurity learners who want a clean, safe, and focused tool for practicing recon and basic vulnerability detection.

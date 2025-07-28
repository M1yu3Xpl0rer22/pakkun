🥷 Pakkun — Subdomain Takeover Detection Tool
Pakkun is a lightweight Python tool built for educational and ethical security research. It scans a list of subdomains to identify potential subdomain takeover vulnerabilities and misconfigurations like default server pages or unclaimed third-party services.

✨ Features
🔍 Detects subdomain takeover opportunities (CNAME or HTTP-based)

📡 Identifies known third-party services (GitHub Pages, Heroku, AWS S3, Netlify, etc.)

⚠️ Flags misconfigured servers (e.g., IIS 404, Plesk default pages)

📝 Clean .txt output files — no CSV clutter

⚡ Fast multithreaded scanning

✅ Compatible with Linux and Windows

⚙️ Requirements
Python 3.7+

Python modules:

requests

dnspython

colorama

🔧 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
🧾 Step 1: Prepare Your Subdomain List
Create a file named subdomains.txt:

lua
Copy
Edit
blog.example.com  
cdn.example.com  
test.herokuapp.com  
ghostsite.github.io  
mysite.netlify.app  
▶️ Step 2: Run the Tool
On Linux/macOS:

bash
Copy
Edit
python3 subdomain_takeover_scanner.py subdomains.txt
On Windows:

bash
Copy
Edit
python subdomain_takeover_scanner.py subdomains.txt
🔍 Example Output
bash
Copy
Edit
[TAKEOVER-POSSIBLE] ghostsite.github.io → github.io (GitHub Pages)
[UNCLAIMED-SERVICE] test.herokuapp.com → Heroku (Unclaimed)
[INFO] cdn.example.com → Plesk Default Page
[OK] blog.example.com → HTTP 200 (Active / No Fingerprint)
[UNREACHABLE] unknown.example.com
📁 Output Files
File Name	Description
takeover_results.txt	Full scan log (all subdomains + findings)
vuln_only.txt	Only subdomains with possible takeover risks

📜 License
MIT License — see the LICENSE file for details.

🛡️ Ethical Notice
This tool is intended for educational use and authorized testing only.
Do not scan or test domains you do not own or have explicit permission to audit.
Unauthorized scanning may violate laws or terms of service.

👨‍🎓 Built for Students
Pakkun was created for student researchers, beginner bug bounty hunters, and cybersecurity learners who want a focused, ethical, and beginner-friendly tool to practice reconnaissance and basic vulnerability detection.
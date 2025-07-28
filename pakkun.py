import dns.resolver
import requests
import sys
import threading

# Load list of known services and error fingerprints
known_services = {
    "github.io": ("GitHub Pages", "There isn't a GitHub Pages site here."),
    "herokuapp.com": ("Heroku", "no such app"),
    "s3.amazonaws.com": ("AWS S3", "NoSuchBucket"),
    "storage.googleapis.com": ("Google Cloud", "No such object"),
    "cloudfront.net": ("CloudFront", "ERROR: The request could not be satisfied"),
    "netlify.app": ("Netlify", "Page Not Found"),
    "readthedocs.io": ("ReadTheDocs", "Unknown Domain"),
    "unbouncepages.com": ("Unbounce", "doesn’t exist"),
    "helpscoutdocs.com": ("HelpScout", "docs not found"),
    "azurewebsites.net": ("Azure Web App", "404 Web Site not found"),
    "fastly.net": ("Fastly", "Fastly error: unknown domain"),
    "wordpress.com": ("WordPress", "Do you want to register this domain?"),
    "surge.sh": ("Surge.sh", "project not found"),
    "pantheonsite.io": ("Pantheon", "404 error unknown site"),
    "statuspage.io": ("StatusPage", "page isn’t available")
}

results = []

def check_cname(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        for rdata in answers:
            target = str(rdata.target).strip('.')
            for service_domain, (service_name, _) in known_services.items():
                if service_domain in target:
                    return target, service_name
            return target, "Unknown Hosting"
    except:
        return None, None

def check_http(subdomain):
    try:
        url = f"http://{subdomain}"
        response = requests.get(url, timeout=6)
        body = response.text.lower()
        for _, (service_name, fingerprint) in known_services.items():
            if fingerprint.lower() in body:
                return service_name, fingerprint
        return None, None
    except:
        return None, None

def scan_subdomain(subdomain):
    cname_target, cname_service = check_cname(subdomain)
    if cname_target:
        print(f"[CNAME] {subdomain} → {cname_target} ({cname_service})")
        results.append(f"CNAME,{subdomain},{cname_target},{cname_service}")
    else:
        http_service, fingerprint = check_http(subdomain)
        if http_service:
            print(f"[HTTP]  {subdomain} → Vulnerable response ({http_service})")
            results.append(f"HTTP,{subdomain},N/A,{http_service}")
        else:
            print(f"[-]     {subdomain} → No vulnerability detected")

def main():
    if len(sys.argv) != 2:
        print("Usage: python takeover_scanner.py subdomains.txt")
        sys.exit(1)

    subdomain_file = sys.argv[1]

    try:
        with open(subdomain_file, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {subdomain_file}")
        sys.exit(1)

    threads = []
    print(f"\n[+] Starting scan for {len(subdomains)} subdomains...\n")

    for sub in subdomains:
        t = threading.Thread(target=scan_subdomain, args=(sub,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open("takeover_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")

    print("\n✅ Scan complete. Results saved to takeover_results.txt")

if __name__ == "__main__":
    main()

import subprocess
import json
import requests


class DomainInformation:
    @staticmethod
    def get_subdomains(domain):
        # Passive using Certificate Logs
        subdomain_stdout = subprocess.run(["curl", "https://tls.bufferover.run/dns?q=" + domain], capture_output=True)
        subdomain_stdout = json.loads(subdomain_stdout.stdout.decode())
        subdomain_stdout = subdomain_stdout["Results"]

        subdomain_list = []

        for i in range(0 , len(subdomain_stdout)):
            liste = subdomain_stdout[i].split(",")
            subdomain_list.append(liste[-1].replace(domain, ""))
            i = i + 1

        

        # Aktive by DNS brute forcing
        top5 = ["www", "ftp", "blog", "image", "search"]
        for subdomain in top5:
            new_url = "http://" + subdomain + "." + domain
            try:
                res = requests.get(new_url)
                subdomain_list.append(subdomain)
            except:
                pass

        subdomain_list = list(dict.fromkeys(subdomain_list))
        return subdomain_list

    @staticmethod
    def get_whois_info(domain):
        whois_stdout = subprocess.run(['whois', domain], capture_output=True)
        whois_stdout = whois_stdout.stdout.__str__().replace("b'   ", "")

        whois_info = {}
        for row in whois_stdout.split("\\n"):
            if ': ' in row:
                key, value = row.split(': ')
            if whois_info.get(key.strip(' .')) != None:
                if isinstance(whois_info[key.strip(' .')], str):
                    val = whois_info[key.strip(' .')]
                    whois_info[key.strip(' .')] = [val, value.strip()]
                    continue
                if isinstance(whois_info[key.strip(' .')], str):
                    whois_info[key.strip(' .')].append(value.strip())
                    continue
            whois_info[key.strip(' .')] = value.strip()
        
        whois_info.pop('TERMS OF USE')
        whois_info.pop('NOTICE')

        return whois_stdout, whois_info

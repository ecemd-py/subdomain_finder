import subprocess
import requests


class DomainInformation:
    @staticmethod
    def get_subdomains(domain):
        # Get subdomain information
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)

        try:
            json_response = response.json()
        except ValueError:
            print("Error parsing JSON response")
            return []
        
        subdomain_list = []
        for info in json_response:
            subdomains = info['name_value'].split('\n')
            for subdomain in subdomains:
                if not subdomain in subdomain_list:
                    subdomain_list.append(subdomain)

        subdomain_list = list(dict.fromkeys(subdomain_list))
        return subdomain_list

    @staticmethod
    def get_whois_info(domain):
        whois_stdout = subprocess.run(['wsl', 'whois', domain], capture_output=True)
        whois_stdout = whois_stdout.stdout.decode('utf-8')

        whois_info = {}
        for row in whois_stdout.split('\n'):
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

        return whois_info

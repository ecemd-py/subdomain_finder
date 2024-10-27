from DomainInformation import DomainInformation
from DatabaseOperations import DatabaseOperations


class StartOperation:
    @staticmethod
    def start():
        # Read domain from file
        with open("FindSubdomainInfo\\app\\scripts\\domains.txt", "r") as file:
            content = file.read()

        domain_list = content.split("\n")
        print(domain_list)

        db_ops = DatabaseOperations()
        for domain in domain_list:
            print("Domain information is loading: " + domain)
            # Find subdomain and whois info
            subdomain_list = DomainInformation.get_subdomains(domain)
            dict_whois = DomainInformation.get_whois_info(domain)

            # Write to db
            db_ops.add_domain_info(domain, subdomain_list, dict_whois)

        db_ops.dispose_engine()

if __name__ == "__main__":
    StartOperation.start()

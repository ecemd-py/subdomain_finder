from Core.DomainInformation import DomainInformation
from Core.DatabaseOperations import DatabaseOperations


class StartOperation:
    @staticmethod
    def start():
        # Read domain from file
        with open("/workspace/repo/FindSubdomainInfo/domains.txt", "r") as file:
            content = file.read()

        domain_list = content.split("\n")
        print(domain_list)

        db_ops = DatabaseOperations()
        for domain in domain_list:
            print(domain + " bilgileri bulunuyor.")
            # Find subdomain and whois info
            subdomain_list = DomainInformation.get_subdomains(domain)
            raw_whois, dict_whois = DomainInformation.get_whois_info(domain)

            # Write to db
            db_ops.add_domain_info(domain, subdomain_list, raw_whois, dict_whois)

        db_ops.dispose_engine()


if __name__ == "__main__":
    StartOperation.start()

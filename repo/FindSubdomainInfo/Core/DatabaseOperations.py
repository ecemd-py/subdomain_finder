import pandas as pd
from sqlalchemy import create_engine
import json


class DatabaseOperations:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

    def select_all_data(self):
        query = """
            SELECT *
            FROM domaininfodb
        """

        df = pd.read_sql_query(query, con=self.engine)        
        return df.to_json()

    def select_domain_data(self, domain):
        query = f"""
            SELECT *
            FROM domaininfodb
            WHERE domain = '{domain}'
        """

        df = pd.read_sql_query(query, con=self.engine)
        
        if len(df) > 0:
            return df.to_json()
        
        return json.dumps({"response": domain + " Bulunamadi!"})

    def add_domain_info(self, domain, subdomain_list, whois_raw, whois_formatted):
        check_domain = json.loads(self.select_domain_data(domain))
        if "domain" not in check_domain:
            with self.engine.connect() as con:
                query = f"""
                    INSERT INTO domaininfodb (domain, subdomain_list, whois_raw, whois_formatted)
                    VALUES ('{domain}', '{str(subdomain_list).replace("'", '"')}', '{whois_raw.replace("'", "")}', '{str(whois_formatted).replace("'", '"')}')
                """
                result = con.execute(query)
            
            return result
        else:
            print("Domain bilgileri DB'de var!")

    def dispose_engine(self):
        self.engine.dispose()

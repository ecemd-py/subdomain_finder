import pandas as pd
from sqlalchemy import create_engine, text
import json


class DatabaseOperations:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

    def select_domain_data(self, domain):
        query = f"""
            SELECT *
            FROM domaininfodb
            WHERE domain = '{domain}'
        """

        df = pd.read_sql_query(query, con=self.engine)
        
        if len(df) > 0:
            return df.to_json()
        
        return json.dumps({"response": domain + " Not Found!"})

    def add_domain_info(self, domain, subdomain_list, whois_formatted):
        check_domain = json.loads(self.select_domain_data(domain))
        if "domain" not in check_domain:
            with self.engine.connect() as con:
                query = text("""
                    INSERT INTO domaininfodb (domain, subdomain_list, whois)
                    VALUES (:domain, :subdomain_list, :whois)
                """)
                con.execute(query, {"domain":domain, "subdomain_list": json.dumps(subdomain_list), "whois": json.dumps(whois_formatted)})
                con.commit()

        else:
            print("Domain information already exist in the database!")

    def dispose_engine(self):
        self.engine.dispose()

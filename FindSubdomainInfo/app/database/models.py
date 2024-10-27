import pandas as pd
from sqlalchemy import create_engine, text
import json

DATABASE_URI  = 'postgresql://postgres:postgres@localhost:5432/postgres'
engine = create_engine(DATABASE_URI)

def get_all_data():
    query = """
        SELECT domain, subdomain_list, whois
        FROM domaininfodb
    """

    df = pd.read_sql_query(query, con=engine)        
    return df

def get_subdomains(domain):
    query = text(f"""
        SELECT subdomain_list
        FROM domaininfodb
        WHERE domain = '{domain}'
    """)

    df = pd.read_sql_query(query, con=engine)
    
    if len(df) > 0:
        return json.loads(df['subdomain_list'][0])
    
    return json.dumps({"response": domain + " Not Found!"})

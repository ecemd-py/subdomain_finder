CREATE TABLE domaininfodb (
	id SERIAL PRIMARY KEY,
	domain VARCHAR(255) NOT NULL,
	subdomain_list TEXT,
	whois_raw TEXT,
    	whois_formatted TEXT
);
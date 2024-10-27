# FindSubdomainInfo
A simple web application to find subdomain and whois information of the given domains.

## Features
- Input a domain name to retrieve its all subdomains.
- Displays WHOIS information for the entered domain.
- Shows all stored subdomain data from the PostgreSQL database.

## Technologies Used
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS

## API Endpoints
GET /: Displays the homepage with the domain input form.
GET /get_info: Retrieves subdomains and WHOIS information for the entered domain.
GET /show_db: Displays all data stored in the PostgreSQL database.

## PopulateDatabase Script
The PopulateDatabase.py script is for populating the test database with sample data. It reads domain names from the domains.txt file, finds the associated subdomains and WHOIS information, and inserts them into the PostgreSQL database. This allows you to test the API using this test data. Also, create_table.sql has the table information.
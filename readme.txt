- Linux ortamı için Docker kullandım.
- Containerda PostgreSQL kurulu.
- main.py çalışınca repo/FindSubdomainInfo atında domains.txt'den domainleri alıp 
subdomain ve whois bilgilerini db'ye yazıyor.
- app.py çalıştırılınca localhost:5000'de API ayağa kalkıyor. Örnek istek, belli bir
domain adıyla istek atılabiliyor. Veritabanındaki verinin hepsine de select atılabiliyor.
- Subdomain ve whois bilgisi bulma: DomainInformation.py
- Database işlemleri: DatabaseOperations.py
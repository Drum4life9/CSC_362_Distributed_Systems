import dns.resolver
import time

domain = "example.com"
root = "198.41.0.4"
tld = "com."

tld_ns_list = []

try:
	print(f"Querying root server {root} for NS records...")
	start = time.time()
	query = dns.message.make_query(tld, dns.rdatatype.NS)
	response = dns.query.udp(query, root, timeout=5)
	
	for rrset in response.authority:
		for rr in rrset:
			tld_ns_list.append(rr.to_text())
	
	print(f"Root server {root} returned NS: {tld_ns_list}")
	
	# todo check for non-empty
	
	tld_ns_name = tld_ns_list[3]
	tld_ns_ip = dns.resolver.resolve(tld_ns_name, "A")[0].to_text()
	print(tld_ns_ip)
	
	tld_query = dns.message.make_query(domain, dns.rdatatype.NS)
	tld_response = dns.query.udp(tld_query, tld_ns_ip, timeout=5)
	
	domain_ns_list = []
	for rrset in tld_response.authority:
		for rr in rrset:
			domain_ns_list.append(rr.to_text())
	print(domain_ns_list)
	
	auth_ns_name = domain_ns_list[0]
	auth_ip = dns.resolver.resolve(auth_ns_name, "A")[0].to_text()
	
	auth_resolver = dns.resolver.Resolver()
	auth_resolver.nameservers = [auth_ip]
	answers = auth_resolver.resolve(domain, "A")
	a_records = [r.to_text() for r in answers]
	end = time.time()
	
	print(a_records)
	print(str((end-start) * 1000))
except Exception as e:
	print(f"Root server {root} returned {e}")
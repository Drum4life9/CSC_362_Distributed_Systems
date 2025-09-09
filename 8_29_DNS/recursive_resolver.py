import dns.resolver
import time

domain = "example.com"
rtype = "A"
nameserver = "8.8.8.8"
# root = "198.41.0.4"
# tld = "com."

tld_ns_list = []

try:
	resolver = dns.resolver.Resolver()
	resolver.nameservers = [nameserver]
	resolver.lifetime = 5
	
	start = time.time()
	answer = resolver.resolve(domain, rtype)
	end = time.time()
	
	ips_or_records = [r.to_text() for r in answer]
	duration = (end - start) * 1000
	
	print(ips_or_records)
	print(str(duration))
except Exception as e:
	print(e)
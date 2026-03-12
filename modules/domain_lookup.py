
import whois

def lookup(domain):

    data = whois.whois(domain)

    return data

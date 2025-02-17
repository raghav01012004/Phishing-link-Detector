import tldextract
import Levenshtein as lv

legitimate_domains = {'example.com', 'google.com', 'facebook.com'}

test_urls = [
    'http://example.co',
    'http://example.com',
    'http://www.google.security-update.com',
    'http://www.faceb00k.com',
    'http://www.google.com',
]

def extract_domains_parts(url):
    extracted = tldextract.extract(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

def is_misspelled_domain(domain,legitimate_domains, threshold=0.9):
    for legit_domain in legitimate_domains:
        if lv.ratio(domain, legit_domain) > threshold:
            return False
    return True

def is_phishing_url(url, legitimate_domains):
    subdomain, domain, suffix = extract_domains_parts(url)

    if f"{domain}.{suffix}" in legitimate_domains:
        return False

    if is_misspelled_domain(domain, legitimate_domains):
        print(f"Potential phishing detected : {url}")
        return True
    return False



if __name__  == '__main__':
    for url in test_urls:
        is_phishing_url(url, legitimate_domains)
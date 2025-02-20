
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            
            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in domain_count:
                    domain_count[subdomain] += count
                else:
                    domain_count[subdomain] = count
        
        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result


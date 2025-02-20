
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result = []
        domain_count = {}

        for entry in cpdomains:
            count, domain = entry.split(" ")
            count = int(count) 
            subdomains = domain.split('.')  # Split domain into parts


            for i in range(len(subdomains)):
                # Join subdomain parts
                subdomain = ".".join(subdomains[i:])  
                if subdomain in domain_count:
                    domain_count[subdomain] += count
                else:
                    domain_count[subdomain] = count

        for key, value in domain_count.items():
            result.append(f"{value} {key}")

        return result

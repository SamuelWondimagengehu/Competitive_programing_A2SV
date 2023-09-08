class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        book = defaultdict(int)
        for cpdomain in cpdomains:
            subdomain = ''
            c = int(cpdomain.split(' ')[0])
            subdomains = cpdomain.split(' ')[1].split('.')
            while len(subdomains) > 0:
                if subdomain == '':
                    subdomain = subdomains.pop() + subdomain
                else:
                    subdomain = subdomains.pop() +"." + subdomain 
                book[subdomain] += c
        return [str(book[key]) + " " + key for key in book.keys()]
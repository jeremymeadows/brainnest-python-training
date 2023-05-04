# dns resolver

import dns.resolver

result = dns.resolver.resolve('google.com', 'NS')
for val in result:
    print('A Record:', val.to_text())

result = dns.resolver.resolve('google.com', 'MX')
for val in result:
    print('A Record:', val)

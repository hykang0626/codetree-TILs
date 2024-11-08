class Address:
    def __init__(self, name, addr, region):
        self.name = name
        self.addr = addr
        self.region = region

n = int(input())
address1 = []

for i in range(n):
    name, a, r = tuple(input().split())
    address1.append(Address(name, a, r))
    
address1.sort(key = lambda address:address.name)
print("name", address1[n-1].name)
print('addr', address1[n-1].addr)
print("city", address1[n-1].region)
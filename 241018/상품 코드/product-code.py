class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
n, c = input().split()

product1 = Product("codetree", "50")
product2 = Product(n, c)

print("product %s is %s"%(product1.code, product1.name))
print("product %s is %s"%(product2.code, product2.name))
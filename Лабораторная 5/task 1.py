from pprint import pprint

def table(i):
   return {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}

pprint ([table(n) for n in range(16)])
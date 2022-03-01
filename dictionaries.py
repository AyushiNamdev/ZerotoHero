my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
print(my_dict['key1'])
prices_lookup = {'apple':2.99, 'oranges': 1.99}
print(prices_lookup['apple'])
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d)
print(d['k2'][2])

#-------------

a = {'key1': ['a','s','r']}
print(a)
print(a['key1'][2])
e = a['key1'][2]
print(e.upper())
print(a['key1'][2].upper()) #in single line
 #add new key value pair

p = {'k1':100, 'k2': 200}
p['k3'] = 300
print(p)

print(p.keys())
print(p.values())
print(p.items())


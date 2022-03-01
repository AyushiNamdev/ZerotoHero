x = "hello World"
y = "hi, this is a string"

print( x.upper() )
print(x.lower())

#splitting

print(x.split())
print(y.split('i'))

#------Print formatting with Strings--------
#.format() method
#f-string

print('this is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'. format('fox', 'brown', 'quick'))


'''
def _old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest
_old_macdonald('macdonald')

print(_old_macdonald('macdonald'))

'''

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()
old_macdonald('macdonald')
print(old_macdonald('macdonald'))
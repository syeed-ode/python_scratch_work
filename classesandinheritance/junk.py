from bitarray import bitarray


def generate_password(length, options):
    print(length, 'Options:', options)
    if(options[0]):
        print('Use uppercase')
    if(options[1]):
        print('Use lowercase')
    if(options[2]):
        print('Use numbers')
    if(options[3]):
        print('Gotta ignore that one')


a = bitarray()
a.extend([True, False, False, True])
generate_password(8, options=a)




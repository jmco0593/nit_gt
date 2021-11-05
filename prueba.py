import re

def validar_nit(nit):
    pattern = r'^[0-9]+(-?[0-9kK])?$'
    val = re.match(pattern, nit)
    if val == None:
        return False

    nit = nit.replace(' ', '')
    nit = nit.replace('-', '')
    number = list(nit[0:-1])
    expectedCheker = nit[-1].upper()
    factor = len(nit)
    total = 0

    for i in number:
        digit = int(i)
        total = total + digit*factor
        factor = factor -1

    modulus = (11 - (total %11)) % 11
    if modulus == 10:
        checker = "K"
    else:
        checker = str(modulus)
    
    if checker == expectedCheker:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        nit = str(input('Ingresa el NIT: \n'))
        print(validar_nit(nit))
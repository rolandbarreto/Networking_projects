def address_type(address):
    address_ip = address.split('.')
    first_octet = int(address_ip[0])
    if first_octet >= 1 and first_octet <= 127:
        return 'A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'C'
    else:
        return 'Unknown'
    

def run():
    address = input('Ingrese su dirección IP: ')
    print('Esta dirección es de tipo: ' + address_type(address))


if __name__ == '__main__':
    run()
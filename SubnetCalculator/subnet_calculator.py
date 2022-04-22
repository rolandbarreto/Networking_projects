import ipaddress


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


def address_mask(address_class):
    if address_class == 'A':
        return '255.0.0.0'
    elif address_class == 'B':
        return '255.255.0.0'
    elif address_class == 'C':
        return '255.255.255.0'
    else:
        return 'Unknown'


def get_ip_type(ip):
    if ip.is_private:
        return 'Privada'
    elif ip.is_loopback:
        return 'Loopback'
    elif ip.is_multicast:
        return 'Multicast'
    elif ip.is_reserved:
        return 'Reservada'
    elif not ip.is_private:
        return 'Publica'
    else:
        return 'Unknown'
    

def run():
    address = input('Ingrese su dirección IP: ')
    address_class = address_type(address)
    mask = address_mask(address_class)
    print('Esta dirección es de tipo: ' + address_class)
    print('Esta es su mascara correspondiente: ' + mask)
    

    ip = ipaddress.IPv4Address(address)
    print('Esta es el tipo: ' + get_ip_type(ip))



if __name__ == '__main__':
    run()
import string


def crypt(message, pas=1):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    return ''.join([caracteres[(caracteres.index(c) + pas) % len(caracteres)] for c in message])

def decrypt(message, pas=1):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    return ''.join([caracteres[(caracteres.index(c) - pas) % len(caracteres)] for c in message])

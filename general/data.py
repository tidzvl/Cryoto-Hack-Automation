from Crypto.PublicKey import RSA

def load_rsa_key(file_path: str) -> RSA.RsaKey:
    """Load an RSA key from a PEM file."""
    with open(file_path, 'rb') as key_file:
        key_data = key_file.read()
    return RSA.import_key(key_data)


a = load_rsa_key('../code_base/data.pem')
# print(a.d)

# b = load_rsa_key('../code_base/data.der')
# print(b.d)
from cryptography import x509
from cryptography.hazmat.backends import default_backend
with open("../code_base/data.der", "rb") as f:
    a = f.read()
c = x509.load_der_x509_certificate(a, default_backend())

p = c.public_key()

m = p.public_numbers().n

# print("Modulus (n):", m)
from cryptography.hazmat.primitives import serialization
with open("../code_base/data.pub", "rb") as f:
    p = f.read()

pk = serialization.load_ssh_public_key(p, backend=default_backend())

n = pk.public_numbers()
# print("n:", n.n)

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open("../code_base/trans.pem", "rb") as f:
    pem_data = f.read()

pub_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

modulus = pub_key.public_numbers().n
print("Modulus:", modulus)

modulus_hex = hex(pub_key.public_numbers().n)[2:]  # Bỏ '0x' đầu
print("Modulus HEX:", modulus_hex)


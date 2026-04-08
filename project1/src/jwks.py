import datetime
import base64
from cryptography.hazmat.primitives.asymmetric import rsa

# Generate RSA keys
active_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
expired_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Key IDs
active_kid = "active123"
expired_kid = "expired123"

# Expirations
active_exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
expired_exp = datetime.datetime.utcnow() - datetime.timedelta(hours=1)

def public_jwk(key, kid):
    pub = key.public_key()
    numbers = pub.public_numbers()
    n = base64.urlsafe_b64encode(numbers.n.to_bytes((numbers.n.bit_length() + 7) // 8, "big")).rstrip(b"=").decode("utf-8")
    e = base64.urlsafe_b64encode(numbers.e.to_bytes((numbers.e.bit_length() + 7) // 8, "big")).rstrip(b"=").decode("utf-8")
    return {
        "kty": "RSA",
        "use": "sig",
        "kid": kid,
        "alg": "RS256",
        "n": n,
        "e": e
    }

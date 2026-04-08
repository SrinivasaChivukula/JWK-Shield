import jwt
import datetime

def sign_jwt(key, kid, subject, exp):
    token = jwt.encode(
        {"sub": subject, "exp": exp, "iat": datetime.datetime.utcnow()},
        key,
        algorithm="RS256",
        headers={"kid": kid}
    )
    return token

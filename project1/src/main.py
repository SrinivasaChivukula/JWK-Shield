from flask import Flask, jsonify, request
import datetime
from jwks import active_key, expired_key, active_kid, expired_kid, active_exp, expired_exp, public_jwk
import jwt

app = Flask(__name__)

@app.route("/.well-known/jwks.json", methods=["GET"])
def jwks_endpoint():
    keys = []
    if active_exp > datetime.datetime.utcnow():
        keys.append(public_jwk(active_key, active_kid))
    return jsonify({"keys": keys})

@app.route("/auth", methods=["POST"])
def auth_endpoint():
    use_expired = "expired" in request.args
    if use_expired:
        key, kid, exp = expired_key, expired_kid, expired_exp
    else:
        key, kid, exp = active_key, active_kid, active_exp
        if exp < datetime.datetime.utcnow():
            return "no unexpired signing key", 503

    token = jwt.encode(
        {"sub": "fake-user", "exp": exp, "iat": datetime.datetime.utcnow()},
        key,
        algorithm="RS256",
        headers={"kid": kid}
    )
    return jsonify({"token": token, "kid": kid, "expires_at": int(exp.timestamp())})

@app.route("/healthz", methods=["GET"])
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(port=8080)

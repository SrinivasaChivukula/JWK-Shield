# JWK-Shield 🛡️

**JWK-Shield** is a high-speed simulation of a modern OIDC identity provider. I built this to master how the big players (like Okta or Auth0) handle **JWKS (JSON Web Key Sets)** and token discovery at scale.

### 🛡️ Why it matters
In a huge microservice architecture, you need a way to verify tokens without querying a central database every time. **JWK-Shield** exposes public keys at the `/.well-known/jwks.json` endpoint, allowing other services to verify JWTs instantly and locally.

### 🛠 The Stack
- **Flask:** Lean RESTful API handling auth flows and key discovery.
- **RS256:** Asymmetric signing using private/public key pairs.
- **Statelessness:** Designed to be fast and horizontally scalable. No database bottleneck here.
- **Docker Ready:** Fully containerized for one-command deployment.

### 🚀 Launch it
- **Local:** `python project1/src/main.py`
- **Docker:** `docker build -t jwk-shield . && docker run -p 8080:8080 jwk-shield`

---
"Speed meets security at the identity layer." 🛡️

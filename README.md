# JWK-Shield: Stateless Cryptographic Auth Simulation 🛡️

Hey! Welcome to **JWK-Shield**. This is a high-performance simulation of a modern Authentication and Key Management service. It's designed to mimic how big identity providers (like Auth0 or Okta) handle **JSON Web Key Sets (JWKS)** and **Token Issuance**.

## 🧐 What's the vision?
Authentication isn't just about passwords anymore; it's about secure, verifiable claims. **JWK-Shield** acts as a lightweight identity provider that generates signed **JWTs (JSON Web Tokens)** and exposes public keys so that other services can verify them without talking to a central database every single time.

This project focuses on the core mechanics of the **OpenID Connect (OIDC)** discovery pattern, specifically the `/.well-known/jwks.json` endpoint.

---

## 🛠 Tech Stack & Engineering
I used a lean but powerful stack to keep the latency low and the security high:

- **Flask:** Used the routing engine to build clean, RESTful endpoints for `/auth` and `/jwks`.
- **PyJWT:** Handles the heavy lifting of signing tokens using the **RS256** algorithm.
- **Cryptography (RSA-2048):** Implemented asymmetric encryption to ensure that even if someone sees my public key, they can't forge my tokens.
- **Dockerized Architecture:** The app is fully containerized, making it a "one-command" deploy to any cloud environment.
- **Stateless Design:** Fast and horizontally scalable—perfect for high-concurrency environments.

---

## 🚀 How to Run
### Using Docker (The Pro Way)
```bash
docker build -t jwk-shield .
docker run -p 8080:8080 jwk-shield
```

### Using Python
1. **Setup Environment:**
   ```bash
   pip install -r project1/requirements.txt
   ```
2. **Ignition:**
   ```bash
   python project1/src/main.py
   ```

---

## 📂 Project Structure
- `src/main.py`: The primary server logic handling auth flows.
- `src/jwks.py`: Utilities for managing the JSON Web Key Set.
- `src/jwtutil.py`: Low-level JWT encoding and decoding logic.
- `Dockerfile`: Production-ready container configuration.

---

## 🧠 Strategic Takeaways
- **The OIDC Pattern:** Mastered the standard way modern apps "trust" each other using public key discovery.
- **Asymmetric Signature Verification:** Deeply understood why signing with a private key and verifying with a public one is the backbone of modern web security.
- **Graceful Token Handling:** Implemented logic to handle expired keys, which is crucial for testing how clients behave when keys rotate.

---

## 👨‍💻 Author
**Srinivasa Chivukula**  
*Computer Science Major | AIML, CyberSecurity, and Cloud Technologies*

---
"Security is not a product, it's a process." 🚀

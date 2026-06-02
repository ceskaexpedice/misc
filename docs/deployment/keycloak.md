
---

# 📁 reference/deployment/keycloak.md

```md
# Keycloak deployment

## Přehled

Každá instalace Krameria provozuje vlastní Keycloak instanci.

---

## Nasazení

- Docker / VM / Kubernetes
- reverse proxy
- TLS terminace

---

## Integrace

- OIDC provider pro Kramerius
- SAML federace (volitelně)

---

## Scaling

- stateless backend
- DB persistence Keycloak

---

## Shrnutí

Keycloak je externí identity služba pro Kramerius.
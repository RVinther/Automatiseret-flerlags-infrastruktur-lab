# Sikkerhed

Det her lab er først og fremmest bygget som et læringsmiljø, som en læringsøvelse for mig selv.

## Begrænsninger

- Ingen TLS mellem services
- Database eksponeret på internt netværk
- Ingen firewall-regler
- Ingen adgangskontrol i Grafana

## Hvad man kan gøre

- Bruge secrets management (Vault, Key Vault)
- Implementere TLS
- Segmentere netværk
- Begrænse adgang til databasen
- Tilføje autentificering og autorisation
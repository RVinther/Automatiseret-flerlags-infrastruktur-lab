# Arkitektur

Infrastrukturen er delt op i fem dedikerede virtuelle Ubuntu-servere, som hver repræsenterer et logisk lag i en traditionel flerlags-arkitektur, men i et containeriseret setup.

## Overordnet flow

Klient
-> Nginx (web)
-> Flask API (app)
-> PostgreSQL (db)

Logging:

Node Exporter + Docker metrics
-> Prometheus
-> Grafana

## Design

- Én rolle pr. VM
- Docker til service-isolation
- Ekstern Docker-netværk (infra_net)
- Centraliseret overvågning
- Deployment via Ansible

Arkitekturen er opdelt sådan for at gøre afhængigheder og trafikflow tydelige (for læring).
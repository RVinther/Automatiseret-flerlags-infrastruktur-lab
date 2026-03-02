# Services

## App (Flask)

- Simpel API
- Endpoint: /
- Endpoint: /db-check
- Forbinder til PostgreSQL via miljø-variabler

## Database (PostgreSQL)

- Version 15
- Persistent volume
- Oprettes automatisk via docker-compose

## Workers 

- Skaber kontinuerlig trafik
- Rammer både "/" og "/db-check"
- Bruges til at skabe realistisk load

## Logging

### Node Exporter

- CPU
- RAM
- Disk
- Netværk

### Docker metrics

- Container-statistik
- Engine metrics

### Prometheus

- Scraper alle metrics

### Grafana 

- Visualiserer data
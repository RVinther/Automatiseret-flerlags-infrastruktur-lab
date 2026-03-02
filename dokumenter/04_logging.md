# Logging

Monitorering er centraliseret på log-serveren.

## Hvad bliver overvåget?

- CPU-forbrug
- Hukommelse
- Disk I/O
- Netværkstrafik
- Docker engine metrics
- Container metrics

## Hvordan?

Hver VM kører:

- node_exporter (9100)
- Docker metrics (9393)

Prometheus scraper alle targets hver 5. sekund.

Grafana kobles på Prometheus som data-kilde.

Worker-serveren genererer trafik, så ændringer kan ses i realtid. 
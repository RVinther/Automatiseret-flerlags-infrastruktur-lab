# Netværk

Alle Ubuntu-servere kører på et Host-Only-netværk i Oracle VirtualBox: 

192.168.56.0/24

Hver VM har en fast IP-adresse.

## Portoversigt

| Service               | Port |
|-----------------------|------|
| Nginx                 | 80   |
| Flask API             | 5000 |
| PostgreSQL            | 5432 |
| Prometheus            | 9090 |
| Grafana               | 3000 |
| Node Exporter         | 9100 |
| Docker daemon metrics | 9393 |

## Docker-netværk

Alle containere kobles på et eksternt Docker-netværk:

infra_net

Så kan services på tværs af VMs kommunikere.
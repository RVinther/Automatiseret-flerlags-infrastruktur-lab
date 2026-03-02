# Automatiseret flerlags-infrastruktur-lab  
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?logo=ansible&logoColor=white)

Et containeriseret flerlagsmiljø fordelt på fem Ubuntu-servere i VirtualBox.

Al automatisering (playbooks) er skrevet til Debian/Ubuntu-baserede systemer (apt og systemd).

Jeg har selv anvendt WSL (Ubuntu) på min Windows-host til at provisionere miljøet via Ansible.

Miljøet består af:

- Reverse proxy (Nginx)
- Flask API
- PostgreSQL database
- Worker-server til at generere trafik
- Prometheus monitorering
- Grafana visualisering

Den grundlæggende infrastruktur provisioneres via Ansible. 

Services deployeres via Docker Compose pr. rolle.

Men kan også deployeres via Ansible-playbooks.

## Formålet med projektet

Projektet er baseret på min interesse i at lære Docker, Ansible og IaC (Infrastructure as Code).

Samtidigt ønskede jeg at lære det med udgangspunkt i et realistisk servermiljø med tydelig rolleopdeling og overvågning.

Projektet samler teori fra:

- Netværk og segmentering
- Linux-serverdrift
- Docker og containerisering
- Monitorering og observability
- Infrastructure as Code

Målet har også været at skabe et veldokumenteret og containeriseret miljø.

## Serverroller

| Rolle   | Formål                     |
|---------|----------------------------|
| web     | Reverse proxy (Nginx)      |
| app     | Flask API                  |
| db      | PostgreSQL                 |
| logs    | Prometheus + Grafana       |
| workers | Genererer trafik           |

## Teknologier

- Headless Ubuntu-servere
- Docker & Docker Compose
- Ansible
- Nginx
- Flask
- PostgreSQL
- Prometheus
- Grafana

## Krav

- Ubuntu Server (22.04 testet)
- Docker
- Ansible 2.12+
- Oracle VirtualBox

## Øvrig information

- [Arkitektur](dokumenter/01_arkitektur.md)
- [Netværk](dokumenter/02_netværk.md)
- [Services](dokumenter/03_services.md)
- [Logging](dokumenter/04_logging.md)
- [Sikkerhed](dokumenter/05_sikkerhed.md)
- [Automatisering](dokumenter/06_infrastruktur_automation.md)
- [Genopbygning](dokumenter/07_genopbygning.md)

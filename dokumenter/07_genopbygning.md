# Genopbygning af miljøet

Miljøet er fuldt automatiseret og kan provisioneres med én samlet playbook "site.yml".

## Forudsætninger

Følgende skal være opfyldt:

- 5 Ubuntu-servere (testet på Ubuntu 22.04)
- Netværk konfigureret (Host-Only anbefales i VirtualBox)
- SSH-adgang til alle servere fra host
- Ansible installeret på host-maskinen
- Git installeret på host-maskinen

Automatiseringen er skrevet til Debian/Ubuntu-baserede systemer (apt og systemd).

## 1. Opret virtuelle maskiner

Opret fem Ubuntu-servere med følgende roller:

- web
- app
- db
- logs
- workers

Tildel statiske IP-adresser, så de matcher inventory-filen.

## 2. Klon repository

På din host-maskine, skriv i terminalen:

```bash
git clone https://github.com/RVinther/Automatiseret-flerlags-infrastruktur-lab
cd Automatiseret-flerlags-infrastruktur-lab
```
## 3. Tilpas inventory

Redigér "ansible/inventory/inventory.ini"

Opdatér IP-adresser, så de matcher dine servere.

Sørg for:
"ansible_user" matcher brugeren på serverne

## Kør samlet deployment

Fra mappen "Automatiseret-flerlags-infrastruktur-lab/" i terminalen:

```bash
ansible-playbook -i ansible/inventory/inventory.ini ansible/playbooks/site.yml
```

Så sker følgende automatisk:
1. Installering af Docker på alle servere
2. Konfiguration af Docker daemon (metrics)
3. Deployment af node_exporter
4. Deployment af PostgreSQL (db)
5. Deployment af Flask API (app)
6. Deployment af Nginx reverse proxy (web)
7. Deployment af Prometheus og Grafana (logs)
8. Deployment af workers 

## Tjek om det virker

- Web (via reverse proxy):  http://<web-ip>
- Prometheus:               http://<logs-ip>:9090
- Grafana:                  http://<logs-ip>:3000

Grafana-login:
- Brugernavn: admin
- Password: defineret i docker-compose.yml (dit_kodeord_her)

# Automation af infrastruktur

Miljøet provisioneres og deployes via Ansible.

## Inventory

Serverne er opdelt i følgende roller:

- web
- app
- db
- logs
- workers

Samlet gruppe:

- infra

## Automatiserede opgaver

Playbooks køres i følgende rækkefølge:

1. Installation af Docker
2. Konfiguration af Docker daemon (metrics)
3. Deployment af node_exporter
4. Deployment af database (PostgreSQL)
5. Deployment af applikation (Flask API)
6. Deployment af reverse proxy (Nginx)
7. Deployment af logging og monitorering (Prometheus + Grafana)
8. Deployment af workers

Den samlede playbook "site.yml" importerer alle ovenstående playbooks og gør det muligt at provisionere hele miljøet med én kommando.

## Kørsel

Kør fra mappen "ansible/playbooks/":

```bash
ansible-playbook -i ../inventory/inventory.ini site.yml
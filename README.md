# Kubecon2020EU
This Repo is for the demo for preparing k3s cluster and monitoring raspberry pi temperature using Python, influxdb and grafana


## K3s installation 

Server - curl -sfL https://get.k3s.io | sh - <br>
Get Node Token - /var/lib/rancher/k3s/server/node-token <br>
Agent Install - curl -sfL https://get.k3s.io | K3S_URL=https://myserver:6443 K3S_TOKEN=mynodetoken sh - <br>

Deploy all Yaml files 

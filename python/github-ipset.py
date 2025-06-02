# Script to add all GitHub IPs to an IPSet on PVE
import requests
import os
import subproccess

headers = {'Authorization': 'TOKEN'}
response = requests.get('https://api.github.com/meta')
data = response.json()
cats = ['hooks', 'web', 'api', 'git', 'github_enterprise_importer', 'packages', 'pages', 'importer', 'actions', 'actions_macos', 'codespaces', 'dependabot', 'copilot'] # TODO: simplify this eventually instead of needing to list out each one

ips = []

for cat in cats:
    for ip in data[f'{cat}']:
        ips.append(ip)

ips = list(set(ips))

for ip in ips:
    cmd = ["pvesh", "create", "/cluster/firewall/ipset/github", "-cidr", ip]
    subprocess.run(cmd, capture_output=True, text=True, check=True)

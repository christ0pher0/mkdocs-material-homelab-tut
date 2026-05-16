#!/usr/bin/env python3
"""
generate_network_diagram.py
Reads inventory_auto and /etc/hosts, queries Proxmox nodes via SSH,
and generates a clean Mermaid graph LR for the mkdocs network diagram page.
- Proxmox cluster shown as subgraph with VMs/LXCs under each node
- All other hosts connect directly to Switch — no group bubbles
"""
import re
import sys
import subprocess
from datetime import datetime
from pathlib import Path

INVENTORY_FILE = Path("/home/cos/ansible_dev/inventory_auto")
OUTPUT_FILE    = Path("/home/cos/material/mkdocs_dev_material/docs/network_diagram.md")
HOSTS_FILE     = Path("/etc/hosts")

PROXMOX_NODES = {
    "shardik": "192.168.1.2",
    "maturin": "192.168.1.7",
}

# Groups to skip entirely — proxmox handled by topology, control is a VM
SKIP_GROUPS = {"proxmox", "control", "debian", "redhat"}
SKIP_HOSTS = {"router-net", "netgate-net", "ha-net", "homeassistant-wifi", "argos-deb-wifi"}

# OS label by hostname suffix
OS_LABELS = {
    "-deb": "Debian/Ubuntu",
    "-rpm": "RHEL/Rocky",
    "-win": "Windows",
    "-bsd": "TrueNAS",
    "-net": "Network",
    "-droid": "Android",
    "-media": "Media",
    "-mac": "macOS",
}

def get_os_label(hostname):
    for suffix, label in OS_LABELS.items():
        if hostname.endswith(suffix):
            return label
    return "Linux"

def parse_inventory(path):
    groups = {}
    current_group = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            m = re.match(r"^\[(.+)\]$", line)
            if m:
                current_group = m.group(1)
                groups[current_group] = []
            elif current_group:
                m2 = re.match(r"^(\S+)\s+ansible_host=(\S+)", line)
                if m2:
                    groups[current_group].append((m2.group(1), m2.group(2)))
    return groups

def build_hosts_map():
    hosts_map = {}
    with open(HOSTS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2 and re.match(r"^\d+\.\d+\.\d+\.\d+$", parts[0]):
                ip = parts[0]
                hostname = parts[1]
                # Only map 192.168.x.x addresses — skip localhost/loopback
                if ip.startswith("192.168."):
                    hosts_map[ip] = hostname
    return hosts_map

def get_proxmox_vms(node_ip):
    try:
        r = subprocess.run(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=5",
             f"root@{node_ip}", "qm list"],
            capture_output=True, text=True, timeout=10
        )
        vms = []
        for line in r.stdout.splitlines():
            if line.strip().startswith("VMID") or not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 3:
                vms.append({"vmid": parts[0], "name": parts[1], "status": parts[2]})
        return vms
    except Exception as e:
        print(f"Warning: qm list failed on {node_ip}: {e}", file=sys.stderr)
        return []

def get_proxmox_lxc(node_ip):
    try:
        r = subprocess.run(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=5",
             f"root@{node_ip}", "pct list"],
            capture_output=True, text=True, timeout=10
        )
        cts = []
        for line in r.stdout.splitlines():
            if line.strip().startswith("VMID") or not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 3:
                cts.append({"vmid": parts[0], "status": parts[1], "name": parts[2]})
        return cts
    except Exception as e:
        print(f"Warning: pct list failed on {node_ip}: {e}", file=sys.stderr)
        return []

def sanitize(name):
    return re.sub(r"[^a-zA-Z0-9_]", "_", name)

def generate_diagram(groups, proxmox_topology, hosts_map, proxmox_vm_names):
    lines = []
    lines.append("```mermaid")
    lines.append("graph LR")
    lines.append("")

    # Infrastructure chain
    lines.append("    ONT[ONT]")
    lines.append("    Router[\"router-net<br/>192.168.1.1<br/>OpenWrt\"]")
    lines.append("    Switch[Switch]")
    lines.append("    ONT -->|Fiber| Router")
    lines.append("    Router --> Switch")
    lines.append("    netgate_net[\"netgate-net<br/>192.168.1.6<br/>pfSense\"]")
    lines.append("    Switch --> netgate_net")
    lines.append("")
    lines.append("    ha_net[\"ha-net<br/>192.168.1.125 / 192.168.1.135<br/>Home Assistant\"]")
    lines.append("    Switch --> ha_net")
    lines.append("")

    # Proxmox nodes and their VMs — no subgraph box
    for node_name, node_data in proxmox_topology.items():
        node_ip = PROXMOX_NODES[node_name]
        safe_node = sanitize(node_name)
        lines.append(f'    {safe_node}["{node_name}<br/>{node_ip}"]')
        lines.append(f"    Switch --> {safe_node}")

        for vm in node_data.get("vms", []):
            if vm["status"] != "running":
                continue
            vm_ip = next((ip for ip, hn in hosts_map.items() if hn == vm["name"]), "")
            os_label = get_os_label(vm["name"])
            label = f'{vm["name"]}<br/>{vm_ip}<br/>{os_label}' if vm_ip else f'{vm["name"]}<br/>{os_label}'
            safe_vm = sanitize(vm["name"])
            lines.append(f'    {safe_vm}["{label}"]')
            lines.append(f"    {safe_node} --> {safe_vm}")

        for ct in node_data.get("lxc", []):
            if ct["status"] != "running":
                continue
            ct_ip = next((ip for ip, hn in hosts_map.items() if hn == ct["name"]), "")
            os_label = get_os_label(ct["name"])
            label = f'{ct["name"]}<br/>{ct_ip}<br/>{os_label} (LXC)' if ct_ip else f'{ct["name"]}<br/>{os_label} (LXC)'
            safe_ct = sanitize(ct["name"])
            lines.append(f'    {safe_ct}["{label}"]')
            lines.append(f"    {safe_node} --> {safe_ct}")

        lines.append("")

    # All other hosts — directly off Switch, no group bubbles
    # Skip anything already shown in Proxmox topology or explicitly skipped
    # Build IP->hostname reverse map for inventory lookups
    ip_to_inventory = {}
    for group, hosts in groups.items():
        for hostname, ip in hosts:
            ip_to_inventory[ip] = hostname

    # Build set of IPs used by Proxmox VMs so we can exclude by IP too
    proxmox_vm_ips = set()
    for node_data in proxmox_topology.values():
        for vm in node_data.get("vms", []):
            vm_ip = next((ip for ip, hn in hosts_map.items() if hn == vm["name"]), "")
            if vm_ip:
                proxmox_vm_ips.add(vm_ip)
        for ct in node_data.get("lxc", []):
            ct_ip = next((ip for ip, hn in hosts_map.items() if hn == ct["name"]), "")
            if ct_ip:
                proxmox_vm_ips.add(ct_ip)

    seen = set(proxmox_vm_names)
    seen.update(PROXMOX_NODES.keys())

    for group, hosts in groups.items():
        if group in SKIP_GROUPS:
            continue
        for hostname, ip in hosts:
            if hostname in seen or hostname in SKIP_HOSTS:
                continue
            # Skip if this host's IP is used by a Proxmox VM
            if ip in proxmox_vm_ips:
                continue
            seen.add(hostname)
            safe = sanitize(hostname)
            os_label = get_os_label(hostname)
            lines.append(f'    {safe}["{hostname}<br/>{ip}<br/>{os_label}"]')
            lines.append(f"    Switch --> {safe}")
    lines.append("")

    # Styling
    lines.append("    classDef infra fill:#4a4a8a,stroke:#9999cc,color:#fff")
    lines.append("    classDef proxmox fill:#5a3e00,stroke:#e8a000,color:#fff")
    lines.append("    classDef vm fill:#1a3a2a,stroke:#4caf50,color:#fff")
    lines.append("    classDef linux fill:#1d3557,stroke:#457b9d,color:#fff")
    lines.append("    classDef windows fill:#6d3a3a,stroke:#c1666b,color:#fff")
    lines.append("    classDef bsd fill:#5c4a1e,stroke:#d4a017,color:#fff")
    lines.append("    classDef network fill:#3a3a3a,stroke:#888,color:#fff")
    lines.append("    classDef other fill:#4a2d5a,stroke:#9b72cf,color:#fff")
    lines.append("")
    lines.append("    class ONT,Router,Firewall,Switch infra")

    for node_name, node_data in proxmox_topology.items():
        lines.append(f"    class {sanitize(node_name)} proxmox")
        for vm in node_data.get("vms", []):
            if vm["status"] == "running":
                lines.append(f"    class {sanitize(vm['name'])} vm")
        for ct in node_data.get("lxc", []):
            if ct["status"] == "running":
                lines.append(f"    class {sanitize(ct['name'])} vm")

    # Style flat hosts by OS
    seen2 = set(proxmox_vm_names)
    seen2.update(PROXMOX_NODES.keys())
    for group, hosts in groups.items():
        if group in SKIP_GROUPS:
            continue
        for hostname, ip in hosts:
            if hostname in seen2 or hostname in SKIP_HOSTS:
                continue
            if ip in proxmox_vm_ips:
                continue
            seen2.add(hostname)
            style = "linux"
            if hostname.endswith("-win"):
                style = "windows"
            elif hostname.endswith("-bsd"):
                style = "bsd"
            elif hostname.endswith(("-net", "-media", "-droid", "-mac")):
                style = "network"
            lines.append(f"    class {sanitize(hostname)} {style}")

    lines.append("```")
    return "\n".join(lines)

def main():
    print("📖 Parsing inventory...")
    groups = parse_inventory(INVENTORY_FILE)

    print("🗺️  Building hosts map...")
    hosts_map = build_hosts_map()

    print("🔍 Querying Proxmox nodes...")
    proxmox_topology = {}
    for node_name, node_ip in PROXMOX_NODES.items():
        print(f"  → {node_name} ({node_ip})")
        vms = get_proxmox_vms(node_ip)
        lxc = get_proxmox_lxc(node_ip)
        proxmox_topology[node_name] = {"vms": vms, "lxc": lxc}
        print(f"    VMs: {len(vms)}, LXC: {len(lxc)}")

    proxmox_vm_names = set()
    for node_data in proxmox_topology.values():
        for vm in node_data.get("vms", []):
            proxmox_vm_names.add(vm["name"])
        for ct in node_data.get("lxc", []):
            proxmox_vm_names.add(ct["name"])

    print("📊 Generating diagram...")
    diagram = generate_diagram(groups, proxmox_topology, hosts_map, proxmox_vm_names)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"# Network Diagram\n\n_Last update: {timestamp}_\n\n{diagram}\n"
    OUTPUT_FILE.write_text(content)
    print(f"✅ Network diagram written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()


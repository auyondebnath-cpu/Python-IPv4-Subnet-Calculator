import ipaddress

def calculate_subnet(ip_cidr : str) -> dict:
    "Calculates subnet information from a given IPv4 CIDR notation."
    network = ipaddress.ip_network(ip_cidr, strict=False)

    network_address= str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    netmask = str(network.netmask)
    prefixlen = network.prefixlen
    total_addresses = network.num_addresses

    first_usable = int(network.network_address) + 1
    last_usable = int(network.broadcast_address) - 1
    usable_count = total_addresses - 2 if total_addresses > 2 else 0

    return {
        "ip_cidr": ip_cidr,
        "network": network_address,
        "broadcast": broadcast_address,
        "netmask": netmask,
        "prefixlen": prefixlen,
        "total_addresses": total_addresses
    }
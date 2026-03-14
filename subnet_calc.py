import ipaddress

def calculate_subnet(ip_cidr : str) -> dict:
    "Calculates subnet information from a given IPv4 CIDR notation."
    network = ipaddress.ip_network(ip_cidr, strict=False)

    network_address= str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    netmask = str(network.netmask)
    prefixlen = network.prefixlen
    total_addresses = network.num_addresses

    return {
        "ip_cidr": ip_cidr,
        "network": network_address,
        "broadcast": broadcast_address,
        "netmask": netmask,
        "prefixlen": prefixlen,
        "total_addresses": total_addresses
    }
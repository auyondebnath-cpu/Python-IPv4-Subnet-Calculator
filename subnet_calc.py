import ipaddress

def calculate_subnet(ip_cidr: str) -> dict:
    """Calculates subnet information from IPv4/IPv6 CIDR."""
    network = ipaddress.ip_network(ip_cidr, strict=False)

    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    netmask = str(network.netmask)
    prefixlen = network.prefixlen
    total_addresses = network.num_addresses

    first_usable_int = int(network.network_address) + 1
    last_usable_int = int(network.broadcast_address) - 1
    usable_count = total_addresses - 2 if total_addresses > 2 else 0

    return {
        "ip_cidr": ip_cidr,
        "network": network_address,
        "broadcast": broadcast_address,
        "netmask": netmask,
        "prefixlen": prefixlen,
        "total_addresses": total_addresses,
        "version": "IPv6" if ":" in ip_cidr else "IPv4",
        "first_usable": str(ipaddress.ip_address(first_usable_int)),
        "last_usable": str(ipaddress.ip_address(last_usable_int)),
        "usable_count": usable_count
    }
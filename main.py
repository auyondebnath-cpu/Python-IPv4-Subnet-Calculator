from subnet_calc import calculate_subnet

def main():
    print("Welcome to the Subnet Calculator!")
    while True:
        ip_cidr = input("IP/CIDR (IPv4/IPv6, q=quit): ").strip()
        if ip_cidr.lower() == 'q':
            print("Goodbye!")
            break
        try:
            result = calculate_subnet(ip_cidr)
            print_subnet(result)
            print()
        except ValueError:
            print("Invalid input. Please enter a valid IPv4 CIDR notation (e.g., 192.168.1.10/24).")
        except Exception as e:
            print(f"An error occurred: {e}\n")

def print_subnet(info: dict):
    if 'first_usable' not in info:  # NEW safety check
        print("❌ Missing required fields")
        return
    print(f"\n{'='*50}")  # Header line
    print(f"Input:        {info['ip_cidr']} ({info.get('version', 'IPv4')})")  # Add version
    print(f"Network:      {info['network']}")
    print(f"Broadcast:    {info['broadcast']}")
    print(f"Netmask:      {info['netmask']}/{info['prefixlen']}")
    print(f"Total addrs:  {info['total_addresses']:,}")  #"address" → "addrs" + comma format
    print(f"First usable: {info['first_usable']}")
    print(f"Last usable:  {info['last_usable']}")
    print(f"Usable hosts: {info['usable_count']:,}")  #"count" → "hosts" + comma format
    print(f"{'='*50}\n")  # Footer + spacing

if __name__ == "__main__":
    main()
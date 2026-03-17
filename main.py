from subnet_calc import calculate_subnet

def main():
    print("Welcome to the Subnet Calculator!")
    while True:
        ip_cidr = input("Enter IPv4 CIDR (e.g. 192.168.1.10/24, q to quit): ")
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
    print(f"\nInput:       {info['ip_cidr']}")
    print(f"Network:       {info['network']}")
    print(f"Broadcast:     {info['broadcast']}")
    print(f"Netmask:       {info['netmask']} /{info['prefixlen']}")
    print(f"Total address: {info['total_addresses']}\n")
    print(f"First usable:  {info['first_usable']}")
    print(f"Last usable:   {info['last_usable']}")
    print(f"Usable count:  {info['usable_count']}")

if __name__ == "__main__":
    main()
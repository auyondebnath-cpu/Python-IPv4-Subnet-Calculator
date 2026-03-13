from subnet_calc import calulate_subnet

def main():
    print("Welcome to the Subnet Calculator!")
    while True:
        ip_cidr = input("Enter IPv4 CIDR (e.g. 192.168.1.10/24, q to quit): ")
        if ip_cidr.lower() == 'q':
            break
        results = calulate_subnet(ip_cidr)
        print(results)

if __name__ == "__main__":
    main()
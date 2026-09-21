import ipaddress

def subnet(network):
    net = ipaddress.ip_network(network)

    print("Network address: ", net.network_address)
    print("Broadcast address: ", net.broadcast_address)
    print("Subnet mask: ", net.netmask)
    print("Total addresses: ", net.num_addresses)
    print("Usable hosts: ", net.num_addresses - 2)




print("Subnetting Made Easy !!!")
network = input("Enter the ip address [x.x.x.x/24]: ")
subnet(network)

#print(subnet(ip_addr))


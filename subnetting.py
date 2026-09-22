import ipaddress
import math 

def subnet(network):
    net = ipaddress.ip_network(network)

    print("Network address: ", net.network_address)
    print("Broadcast address: ", net.broadcast_address)
    print("Subnet mask: ", net.netmask)
    print("Total addresses: ", net.num_addresses)
    print("Usable hosts: ", net.num_addresses - 2)

def network_based(network, net_req):
    net = ipaddress.ip_network(network)
    pwr = 0
    while 2**pwr < net_req:      
        pwr += 1
    # pwr is now the number of bits to add
    subnets = list(net.subnets(prefixlen_diff=pwr))
    for s in subnets:
        print(s)
    
def host_based(network, host_req):
    net = ipaddress.ip_network(network)
    # host bits needed for host_req hosts (+2 for network & broadcast)
    host_bits = 0
    while 2**host_bits < host_req + 2:
        host_bits += 1
    new_prefix = net.max_prefixlen - host_bits
    subnets = list(net.subnets(new_prefix=new_prefix))
    for s in subnets:
        print(s)



print("Subnetting Made Easy !!!")
network = input("Enter the ip address [x.x.x.x/24]: ")
choice = int(input("Network requiremnt: 1\nHost requiremnet: 2\n--->"))
match choice:
    case 1:
        network_requirement = int(input("Enter number of required networks: "))
        network_based(network, network_requirement)
    case 2:
        host_requirement = int(input("Enter number of required host: "))
        host_based(network, host_requirement)
    case _:
        subnet(network)



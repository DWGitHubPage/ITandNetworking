# Python 3.9.5
# The ipaddress module.


import ipaddress

# To find out whether your ip address is IPv4 or IPv6 in IDLE shell.
# A ValueError is raised if address isn't either with the following below.

ipaddress.ip_address('10.1.10.26') # Put your ip address in the parenthesis.


# Return an IPv4 or IPv6Network object.

ipaddress.ip_network('10.1.10.26')

# Return an IPv4Interface or IPv6Interface.

ipaddress.ip_interface('10.1.10.26')

# The name of the reverse DNS PTR (Pointer) record for the IP address.

ipaddress.ip_address('10.0.1.26').reverse_pointer

# Returns a string representation of the IP address.

'{:#b}'.format(ipaddress.IPv4Address('10.1.10.26'))

# To interoperate with networking interfaces such as the socket module, addresses
# must be converted to strings or integers.

str(ipaddress.IPv4Address('10.1.10.26'))

int(ipaddress.IPv4Address('10.1.10.26'))

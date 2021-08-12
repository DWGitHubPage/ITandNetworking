# Python 3.9.5
# How to check whether IPv4 or IPv6 address is valid or not.

import os, ipaddress 
 
os.system('cls')
 
while True:
    ip = input('Enter IP address: ')
    try: 
        print(ipaddress.ip_address(ip))
        print('IP Valid.')
    except: 
        print:('-' *50)
        print('IP is not valid.')
    finally: 
        if ip =='q':
           print('Script Finished.')
           break
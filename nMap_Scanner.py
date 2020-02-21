import nmap
def ns1():
    ns= nmap.portscanner()
    print('Version: ' + ns.nmap_version())
    print('Basic Scan info: ' + ns.scaninfo())
    print('All hosts: ' + ns.all_hosts())
    ip= str(input('input your ip: '))
def start():
    in1= int(input('Hello! select the action: /n 1. state of ip /n  2. protocol available /n 3. key of protocol /n 4. see the open port /n 5. see scan results.'))
    if in1== 1:
        ns1()
        print(ns[ip].state())
    
    elif in1== 2:
        ns1()
        print(ns[ip].allprotocols())
  
    elif in1== 3:
        ns1()
        in2= str(input('give your protocol, ex. ftp tcp, etc.: '))
        print(ns[ip][in2].keys())
  
    elif in1== 4:
        ns1()
        in2= int(input('port to be checked: '))
        print(ns[ip].has_tcp(in2))
             
    elif in1== 5:
        in2= int(input('scan range: '))
        ns.scan(ip, in2)
        ns.command_line
    else:
        print('Please select a valid option.')
        ns1()
        start()
start()

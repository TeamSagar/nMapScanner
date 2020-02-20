import nmap
def ns():
  ns= nmap.PortScanner()
  print('Version: ' + ns.nmap_version())
  print('Basic Scan info: ' + ns.scaninfo())
  print('All hosts: ' + ns.all_hosts())
  ip= str(input('input your ip: ')
def start():
  in1= int(input('Hello! select the action: /n 1. state of ip /n  2. protocol available /n 3. key of protocol /n 4. see the open port'))
  if in1= 1:
    ns()
    
  elif in1= 2:
    ns()
  
  elif in1= 3:
    ns()
  
  elif in1= 4:
    ns()
  else:
    print('Please select a valid option.')
    ns()
    start()

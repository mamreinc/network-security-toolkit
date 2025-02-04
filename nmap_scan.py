import nmap
import argparse

def scan_network(target, options):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=options)
    
    for host in nm.all_hosts():
        print(f'Host: {host} ({nm[host].hostname()})')
        print(f'State: {nm[host].state()}')
        
        for proto in nm[host].all_protocols():
            print(f'Protocol: {proto}')
            ports = nm[host][proto].keys()
            
            for port in ports:
                print(f'Port: {port}	State: {nm[host][proto][port]["state"]}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Nmap Network Scanner")
    parser.add_argument("target", help="Target IP address or subnet")
    parser.add_argument("options", help="Nmap scan options (e.g., -p 1-65535 -sV -sC)")
    args = parser.parse_args()
    
    scan_network(args.target, args.options)


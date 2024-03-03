from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gethostbyaddr, setdefaulttimeout

def conScan(targetHost, targetPort):
    """
    Attempts to connect to a specified port on a target host.
    
    
    Args:
    - target_host (str): The hostname or IP address of the target.
    - target_port (int): The port number to attempt to connect to.
    
    
    Prints the status of the connection attempt.
    """
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((targetHost, targetPort))
        print('[+] {}/tcp open'.format(targetPort))
        connection_socket.close()
    except Exception as e:
        print('[-] {}/tcp closed or unreachable - {}'.format(targetPort, e))

def portScan(targetHost, targetPorts):
    """
    Scans a list of ports on a specified host.
    
    
    Args:
    - target_host (str): The hostname or IP address of the target to scan.
    - target_ports (List of ints): A list of port numbers to scan.
    
    
    Attempts to resolve the target's hostname to an IP address, and scans each specified port.
    """
    try:
        targetIP = gethostbyname(targetHost)
    except Exception as e:
        print('[-] Cannot resolve {}: {}'.format(targetHost, e))
        return
    
    try:
        targetName = gethostbyaddr(targetIP)[0]
        print('\n[+] Scan result of: {}'.format(targetName))
    except Exception as e:
        print('\n[+] Scan result of: {}'.format(targetIP))
    
    
    setdefaulttimeout(1)
    
    
    for targetPort in targetPorts:
        print('Scanning Port: {}'.format(targetPort))
        conScan(targetHost, int(targetPort))


if __name__ == '__main__':
    portScan('ginandjuice.shop', [20,21,22,23,25,53,67,68,69,80,
                                  110,123,137,139,143,443,445,465,587,1433,
                                  1521,3306,3389,8080,8443])
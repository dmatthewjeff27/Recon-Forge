import socket

class PortScanner:
    def scan(self, host, ports):
        open_ports = []
        for port in ports:
            try:
                s = socket.socket()
                s.settimeout(1)
                s.connect((host, port))
                open_ports.append(port)
                s.close()
            except:
                pass
        return open_ports

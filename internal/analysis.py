import nmap3


class Analysis(object):
    """use analysis object to scan your hosts

    Args:
        object (_type_): python base object
    """
    def __init__(self, host):
        self.nmap = nmap3.Nmap()
        self.host = host
    
    def port_scan(self):
        pass
    
    def dns_scan(self):
        pass
    
    def os_scan(self):
        pass
    
    def version_scan(self):
        pass
    
    def vulen_scan(self):
        pass
    
    def ping_scan(self):
        pass
    
    def syn_scan(self):
        pass

    def tcp_scan(self):
        pass
    
    def udp_scan(self):
        pass

import nmap3


class Analysis(object):
    """use analysis object to scan your hosts

    Args:
        object (_type_): python base object
    """
    def __init__(self, host):
        self.nmap = nmap3.Nmap()
        self.nmap2 = nmap3.NmapScanTechniques()
        self.host = host
    
    def port_scan(self):
        return self.nmap.scan_top_ports(self.host)
    
    def dns_scan(self):
        return self.nmap.nmap_dns_brute_script(self.host)
    
    def os_scan(self):
        return self.nmap.nmap_os_detection(self.host)
    
    def version_scan(self):
        return self.nmap.nmap_version_detection(self.host)
    
    def vulen_scan(self):
        return self.nmap.nmap_version_detection(self.host, args="--script vulners --script-args mincvss+5.0")
    
    def ping_scan(self):
        return self.nmap2.nmap_ping_scan(self.host)
        
    def syn_scan(self):
        return self.nmap2.nmap_syn_scan(self.host)

    def tcp_scan(self):
        return self.nmap2.nmap_tcp_scan(self.host)
    
    def udp_scan(self):
        return self.nmap2.nmap_udp_scan(self.host)

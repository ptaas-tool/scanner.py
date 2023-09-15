import nmap3
import json


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
        v = []
        res = self.nmap.scan_top_ports(self.host)
        
        for key in res:
            if res[key]['osmatch']:
                v.append('os version')
        
        return v
    
    def dns_scan(self):
        print(json.dumps(self.nmap.nmap_dns_brute_script(self.host), indent=2))
        #self.nmap.nmap_dns_brute_script(self.host)
        return []
    
    def os_scan(self):
        #self.nmap.nmap_os_detection(self.host)
        return []
    
    def version_scan(self):
        #self.nmap.nmap_version_detection(self.host)
        return []
    
    def vulen_scan(self):
        #self.nmap.nmap_version_detection(self.host, args="--script vulners --script-args mincvss+5.0")
        return []
    
    def ping_scan(self):
        #self.nmap2.nmap_ping_scan(self.host)
        return []
        
    def syn_scan(self):
        #self.nmap2.nmap_syn_scan(self.host)
        return []

    def tcp_scan(self):
        #self.nmap2.nmap_tcp_scan(self.host)
        return []
    
    def udp_scan(self):
        #self.nmap2.nmap_udp_scan(self.host)
        return []
